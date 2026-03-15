import requests
import os

PLANTNET_API_KEY = os.getenv("PLANTNET_API_KEY")

def identify_plant(image_path, min_score=0.7):
    url = f"https://my-api.plantnet.org/v2/identify/all?api-key={PLANTNET_API_KEY}"
    try:
        with open(image_path, "rb") as img_file:
            files = {"images": img_file}
            response = requests.post(url, files=files)

        if response.status_code != 200:
            return {"scientific_name": "Inconnue",
                    "message": "Impossible de contacter PlantNet."}

        data = response.json()
        results = data.get("results", [])

        # Vérifier score minimal
        for r in results:
            score = r.get("score", 0)
            if score >= min_score:
                scientific_name = r["species"]["scientificNameWithoutAuthor"]
                return {"scientific_name": scientific_name, "message": "Plante identifiée avec succès."}

        # Si aucun résultat fiable
        return {"scientific_name": "Inconnue",
                "message": "Plante non identifiée avec un niveau de confiance suffisant."}

    except Exception as e:
        return {"scientific_name": "Inconnue",
                "message": f"Erreur identification: {str(e)}"}
    """
    Identifie une plante à partir d'une image via PlantNet.
    Si la plante est inconnue ou non identifiée, renvoie un message clair pour l'utilisateur.
    """
    url = f"https://my-api.plantnet.org/v2/identify/all?api-key={PLANTNET_API_KEY}"

    try:
        with open(image_path, "rb") as img_file:
            files = {"images": img_file}
            print("Using PlantNet API Key:", PLANTNET_API_KEY)
            response = requests.post(url, files=files)

        if response.status_code != 200:
            print("PlantNet API error:", response.status_code, response.text)
            return {
                "scientific_name": "Inconnue",
                "message": (
                    "Impossible de contacter le service PlantNet. "
                    "Veuillez réessayer plus tard ou soumettre une autre image."
                )
            }

        data = response.json()
        print("PlantNet API response:", data)

        if not data.get("results"):
            # Plante non identifiée
            return {
                "scientific_name": "Inconnue",
                "message": (
                    "La plante n'a pas pu être identifiée. "
                    "Veuillez soumettre une image plus claire ou contacter un expert local."
                )
            }

        # Si PlantNet a trouvé un résultat
        best_match = data["results"][0]
        scientific_name = best_match["species"]["scientificNameWithoutAuthor"]

        return {
            "scientific_name": scientific_name,
            "message": "Plante identifiée avec succès."
        }

    except Exception as e:
        print("Error during PlantNet identification:", str(e))
        return {
            "scientific_name": "Inconnue",
            "message": (
                f"Une erreur est survenue lors de l'identification de la plante : {str(e)}. "
                "Veuillez réessayer avec une autre image."
            )
        }