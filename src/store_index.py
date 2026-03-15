from helper import load_pdf_files, text_splitter, download_hugging_face_embeddings
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore


import os
os.chdir("../")

from dotenv import load_dotenv
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_kEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

extracted_data = load_pdf_files("Data/")
text_chunks = text_splitter(extracted_data)
embeddings = download_hugging_face_embeddings()


pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "sanitask"

if not pc.has_index(index_name):
    pc.create_index_for_model(
        name=index_name,
        cloud="aws",
        region="us-east-1",
        embed={
            "model":"llama-text-embed-v2",
            "field_map":{"text": "chunk_text"}
        }
    )



docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding = embeddings
)