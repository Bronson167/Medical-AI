# =============================
# imports
# =============================
import sys
import types
import os

# =============================
# Windows fix
# =============================
if sys.platform == "win32" and 'pwd' not in sys.modules:
    pwd = types.ModuleType('pwd')
    sys.modules['pwd'] = pwd
    
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from langdetect import detect

from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain_pinecone import PineconeVectorStore



# =============================
# Load env
# =============================
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# =============================
# Flask app
# =============================
app = Flask(__name__, template_folder="templates")
CORS(app)

# =============================
# RAG (Pinecone déjà indexé)
# =============================
index_name = "sanitask"

vectorstore = PineconeVectorStore.from_existing_index(
    index_name=index_name
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)

# =============================
# LLM Groq
# =============================
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    max_tokens=500,
    groq_api_key=GROQ_API_KEY
)

# =============================
# Memory
# =============================
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# =============================
# Prompt
# =============================
system_prompt = """
Tu es un assistant médical spécialisé.

Réponds dans la langue de l'utilisateur.

Contexte:
{context}

Historique:
{chat_history}

Question:
{input}

Réponse claire, simple et utile.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# =============================
# RAG Chain
# =============================
question_answer_chain = create_stuff_documents_chain(llm, prompt)

rag_chain = create_retrieval_chain(
    retriever,
    question_answer_chain
)

# =============================
# ROUTES
# =============================
@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("msg", "").strip()

    try:
        lang = detect(msg)
        language = "créole haïtien" if lang == "ht" else "français"

        history = memory.chat_memory.messages

        response = rag_chain.invoke({
            "input": msg,
            "chat_history": history,
            "language": language
        })

        answer = response.get("answer", "")

        memory.save_context(
            {"input": msg},
            {"output": answer}
        )

        return jsonify({"answer": answer})

    except Exception as e:
        print("Erreur:", e)
        return jsonify({"answer": "Erreur technique"}), 500


# =============================
# MAIN
# =============================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
