import os
import json
from langchain_groq import ChatGroq
from services.haitian_medicinal_plants import HAITIAN_MEDICINAL_PLANTS

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3,
    max_tokens=500,
    groq_api_key=GROQ_API_KEY
)

def analyze_medicinal_properties(scientific_name):
    prompt_template = f"""
You are an expert in medicinal plants and Caribbean ethnobotany.

The plant has been identified with the scientific name: {scientific_name}.

Your task is to determine if this plant is used in traditional medicine in Haiti.

IMPORTANT RULES:
- All text values must be written in **French**.
- The **local_name** must correspond to the **common name used in Haiti (Creole or French if known)**.
- The **recommendations** must be a **short explanation describing how the plant is traditionally used in Haitian medicine** (for example: infusion, decoction, leaf application, etc.).
- The **medicinal_uses** must contain a list of common health conditions the plant is traditionally used for.
- If the plant is **not medicinal**, set "is_medicinal" to false and leave "medicinal_uses" as an empty list.
- The **confidence** must be a number between **0 and 1** representing the certainty of the identification.

Return STRICTLY a valid JSON with the following structure:

{{
  "scientific_name": "",
  "local_name": "",
  "is_medicinal": true/false,
  "medicinal_uses": [],
  "recommendations": "",
  "confidence": 0-1
}}

IMPORTANT:
- Return ONLY the JSON.
- Do NOT add explanations.
- Do NOT add text before or after the JSON.
"""

    raw_text = ""
    try:
        # Appel LLM
        response = llm.invoke(prompt_template)

        # L'objet retourné par LangChain est un AIMessage. 
        # On extrait uniquement le texte via l'attribut .content
        raw_text = response.content

        # Nettoyer les éventuels caractères superflus (markdown ```json ... ```)
        first_brace = raw_text.find("{")
        last_brace = raw_text.rfind("}")

        if first_brace != -1 and last_brace != -1 and last_brace > first_brace:
            json_text = raw_text[first_brace:last_brace+1]
            try:
                analysis = json.loads(json_text)
            except json.JSONDecodeError:
                analysis = {"error": "Impossible de parser la réponse LLM", "raw": raw_text}
        else:
            analysis = {"error": "Réponse LLM ne contient pas de JSON", "raw": raw_text}

        return analysis

    except Exception as e:
        return {"error": f"Erreur serveur LLM: {str(e)}", "raw": raw_text}