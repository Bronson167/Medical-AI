# =============================
# imports
# =============================
# PATCH POUR WINDOWS - À METTRE EN PREMIER
import sys
import types
from datetime import date



import random
from urllib import response
if sys.platform == "win32" and 'pwd' not in sys.modules:
    pwd = types.ModuleType('pwd')
    def getpwuid(uid=None):
        from collections import namedtuple
        import os
        passwd_entry = namedtuple('passwd_entry', 
                                 ['pw_name', 'pw_passwd', 'pw_uid', 
                                  'pw_gid', 'pw_gecos', 'pw_dir', 'pw_shell'])
        username = os.environ.get('USERNAME', 'unknown')
        return passwd_entry(username, 'x', 1000, 1000, '', 
                           f'C:\\Users\\{username}', 'cmd.exe')
    pwd.getpwuid = getpwuid
    sys.modules['pwd'] = pwd
    print("✅ Patch Windows appliqué")

from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
sys.path.append(os.path.dirname(__file__))

from services.haitian_medicinal_plants import HAITIAN_MEDICINAL_PLANTS
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_pinecone import PineconeVectorStore

# from src.helper import download_hugging_face_embeddings  # Note: corrigé embeddingsz -> embeddings

from langchain.memory import ConversationBufferMemory
from langdetect import detect

# Reste du code...

# =============================
# Load environment variables
# =============================
load_dotenv()

from services.plant_identifier import identify_plant
from services.plant_llm_service import analyze_medicinal_properties

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Nouvelle clé Groq

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# =============================
# Préparer les embeddings et le retriever
# =============================
# embeddings = download_hugging_face_embeddings()
index_name = "sanitask"

# docsearch = PineconeVectorStore.from_existing_index(
#     index_name=index_name,
#     embedding=embeddings
# )

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 5})

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# =============================
# Prompt médical spécialisé
# =============================
system_prompt = """
Tu es un assistant médical spécialisé en diagnostic clinique.

Objectif :
- Aider les patients à comprendre leurs symptômes.
- Fournir un triage simple et clair.
- Les réponses doivent être compréhensibles par :
  - un patient non formé
  - un professionnel de santé

Langue :
- Réponds toujours dans la langue de l'utilisateur ({language}), soit français ou créole haïtien.

Méthode de raisonnement :
1. Identifier tous les symptômes mentionnés dans la conversation.
2. Utiliser l'historique complet des symptômes précédemment rapportés.
3. Comparer les symptômes avec des maladies possibles. Si aucun symptôme spécifique n'est fourni, ne fais pas de comparaison ni de diagnostic.
4. Donner seulement les diagnostics plausibles.
5. Prioriser les maladies fréquentes en Haïti :
   - paludisme
   - dengue
   - grippe
   - infections respiratoires
   - typhoïde

Règles médicales importantes :
- Ne jamais donner de faux espoirs ni de diagnostics alarmants sans preuves solides.
- Ne jamais recommander de traitements sans diagnostic clair.
- Ne jamais diagnostiquer une maladie sans symptômes spécifiques.
- Ne jamais inventer de maladies rares si les symptômes sont communs.

Contexte médical :
{context}

Format obligatoire si symptômes spécifiques sont présents :

Résumé des symptômes :
- ...

Maladies possibles :

1. maladie — probabilité approximative
   explication simple

2. maladie — probabilité approximative
   explication simple

3. maladie — probabilité approximative
   explication simple

Niveau d'urgence :
- urgent
- modéré
- faible

Conseil pour le patient :
- Demander plus d'informations si nécessaire.
- conseil simple et clair.

Format obligatoire si symptômes spécifiques ne sont pas présents :
Aucun symptôme spécifique n'a été mentionné. Veuillez fournir plus de détails pour une évaluation précise.

Important :
- Les probabilités doivent être cohérentes et totaliser environ 1.
- Si urgence, conseiller consultation médicale et mentionner la possibilité d'utiliser la section carte pour trouver les centres de santé proches.

"""

# prompt = ChatPromptTemplate.from_messages([
#     ("system", system_prompt),
#     ("human", "{input}")
# ])

# Ajoutez "MessagesPlaceholder" aux imports
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Modifiez la structure du prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="chat_history"), # L'historique sera injecté ici
    ("human", "{input}")
])

# =============================
# LLM Groq (100% gratuit)
# =============================
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    max_tokens=500,
    groq_api_key=GROQ_API_KEY
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


# =============================
# Générateur de conseil santé
# =============================

health_tip_prompt = ChatPromptTemplate.from_template("""
Tu es un éducateur en santé publique en Haïti.

Génère UN seul conseil santé court et utile.

Le conseil peut être basé sur :
- médecine conventionnelle
- médecine traditionnelle haïtienne
- hygiène
- prévention des maladies
- alimentation
- hydratation
- moustiques et paludisme
- dengue
- typhoïde
- santé respiratoire
- santé digestive

Contraintes :

- maximum 2 phrases
- langage simple
- compréhensible par tout le monde
- utile pour la population haïtienne
- S'il n'ya pas de symptômes spécifiques, ne donne pas de conseil, ni de diagnostic, ni de recommandation, ni de probalite.                                              

Répond uniquement avec le conseil.
""")

health_tip_chain = health_tip_prompt | llm


def generate_health_tip():
    try:
        response = health_tip_chain.invoke({})
        return response.content.strip()
    except Exception as e:
        return "Buvez de l'eau propre et lavez-vous les mains régulièrement pour prévenir de nombreuses maladies."
# =============================
# Flask app
# =============================
app = Flask(__name__, template_folder="templates")
CORS(app)

@app.route("/")
def index():
    return render_template("chat.html")



@app.route("/get", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("msg", "").strip()
    
    try:
        # 1. Détection langue
        lang = detect(msg)
        language = "créole haïtien" if lang == "ht" else "français"

        # 2. Charger l'historique proprement (sous forme de liste de messages)
        # C'est l'étape CRUCIALE
        history_messages = memory.chat_memory.messages 

        # 3. Appel à la chaîne
        # On passe 'chat_history' pour le Prompt et 'input' pour la question
        response = rag_chain.invoke({
            "input": msg,
            "chat_history": history_messages,
            "language": language
        })

        answer = response.get("answer", "")

        # 4. Sauvegarder dans la mémoire (Format structuré)
        memory.save_context({"input": msg}, {"output": answer})

        return jsonify({"answer": answer})

    except Exception as e:
        print(f"Erreur : {e}")
        return jsonify({"answer": "Erreur technique"}), 500


    
@app.route("/identify_plant", methods=["POST"])
def plant_endpoint():
    if "image" not in request.files:
        return jsonify({"error": "Aucune image téléchargée"}), 400

    image_file = request.files["image"]
    image_path = f"temp_{image_file.filename}"
    image_file.save(image_path)

    try:
        # 1️⃣ Identifier la plante
        identification = identify_plant(image_path)
        scientific_name = identification.get("scientific_name", "").strip()
        message_id = identification.get("message", "")

        # 2️⃣ Si PlantNet n'a rien trouvé
        if not scientific_name or scientific_name.lower() == "inconnue":
            return jsonify({
                "status": "fail",
                "scientific_name": "Inconnue",
                "message": message_id or "Plante non identifiée"
            }), 404

        # 3️⃣ Chercher dans le dictionnaire local
        dict_info = HAITIAN_MEDICINAL_PLANTS.get(scientific_name, None)

        if dict_info:
            # Si trouvé dans le dictionnaire, récupérer toutes les infos
            analysis = {
                "scientific_name": scientific_name,
                "local_name": dict_info.get("local_name", ""),
                "is_medicinal": dict_info.get("is_medicinal", False),
                "medicinal_uses": dict_info.get("medicinal_uses", []),
                "recommendations": dict_info.get("recommendations", ""),
                "confidence": 1.0
            }
        else:
            # Sinon, appeler le LLM pour générer les infos
            analysis = analyze_medicinal_properties(scientific_name)

        return jsonify({
            "status": "success",
            "scientific_name": scientific_name,
            "analysis": analysis
        }), 200

    except Exception as e:
        print(f"🔥 Erreur Critique Route Plant: {e}")
        return jsonify({"error": "Erreur serveur interne"}), 500

    finally:
        if os.path.exists(image_path):
            os.remove(image_path)
# =============================
# Route conseil santé quotidien
# ==
@app.route("/daily_health_tip", methods=["GET"])
def daily_health_tip():
    """
    Génère un conseil santé court et utile avec l'IA Groq.
    Le conseil est basé sur :
    - médecine conventionnelle
    - médecine traditionnelle haïtienne
    - hygiène
    - prévention des maladies
    - alimentation
    - hydratation
    - moustiques et paludisme
    - dengue
    - typhoïde
    - santé respiratoire et digestive
    """
    try:
        # Appel à la chaîne IA Groq que tu as définie
        tip = generate_health_tip()

        # Nettoyage simple pour éviter les guillemets échappés
        tip = tip.strip('"').strip()

        return jsonify({"tip": tip})

    except Exception as e:
        print(f"Erreur génération conseil santé : {e}")
        # fallback si l'IA échoue
        fallback_tip = "Buvez de l'eau propre et lavez-vous les mains régulièrement pour prévenir de nombreuses maladies."
        return jsonify({"tip": fallback_tip, "error": str(e)}), 500
        
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
