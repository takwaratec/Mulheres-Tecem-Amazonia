import os
from google import genai

def load_google_api_key():
    if os.path.exists(".env"):
        with open(".env", "r") as f:
            for line in f:
                if "GOOGLE_API_KEY=" in line:
                    return line.strip().split("=")[1]
    return os.getenv("GOOGLE_API_KEY")

def list_models():
    api_key = load_google_api_key()
    if not api_key:
        print("API Key not found.")
        return

    client = genai.Client(api_key=api_key)
    print("--- Modelos Disponíveis ---")
    try:
        # No SDK V2 (google-genai), a listagem de modelos é feita via client.models.list()
        for m in client.models.list():
            print(f"ID: {m.name} | Supported: {m.supported_actions}")
    except Exception as e:
        print(f"Erro ao listar: {e}")

if __name__ == "__main__":
    list_models()
