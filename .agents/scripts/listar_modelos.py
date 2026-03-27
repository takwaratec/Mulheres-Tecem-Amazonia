# --- EXPLICAÇÃO DIDÁTICA PARA FABIO ---
# O QUE FAZ: Lista quais modelos do Google estão liberados para sua chave.

from google import genai
import os

client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

try:
    for model in client.models.list():
        print(f"✅ {model.name}")
except Exception as e:
    print(f"❌ Erro: {e}")
