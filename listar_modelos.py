from google import genai
import os

client = genai.Client(api_key=os.environ.get("AIzaSyDnUer8X3QiY0dJtK26xL9z8hGxbtm3R8A"))

print("🔎 Listando nomes exatos dos modelos...")

try:
    # Apenas o nome, sem frescura de atributos por enquanto
    for model in client.models.list():
        print(f"✅ Nome: {model.name}")
except Exception as e:
    print(f"❌ Erro: {e}")