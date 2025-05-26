import requests

def responder(texto):
    payload = {
        "model": "llama3",
        "prompt": texto,
        "stream": False
    }
    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        return response.json().get("response", "Desculpe, não entendi.")
    except Exception as e:
        return f"Erro na IA: {e}"
