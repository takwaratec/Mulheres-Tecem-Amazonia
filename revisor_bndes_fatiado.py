import os
import time
from google import genai

client = genai.Client(api_key="AIzaSyDnUer8X3QiY0dJtK26xL9z8hGxbtm3R8A")
MODEL_ID = "models/gemini-2.0-flash"

def ler_pasta(caminho):
    conteudo = ""
    if os.path.exists(caminho):
        for arq in os.listdir(caminho):
            if arq.endswith(".md"):
                try:
                    with open(os.path.join(caminho, arq), 'r', encoding='utf-8') as f:
                        conteudo += f.read()[:3000] # Leitura bem curta para economizar
                except: continue
    return conteudo

def executar_revisao():
    print("🚀 Iniciando Revisão Fatiada (Evitando Erro 429)...")
    
    caminho_rascunho = "docs/00_MODELO 1 - BNDES/03_CONSOLIDADO_TANIA_DRAFT.md"
    with open(caminho_rascunho, "r", encoding="utf-8") as f:
        rascunho = f.read()

    # Coleta de subsídios reduzida
    autos = ler_pasta("docs/01_GOVERNANCA") + ler_pasta("docs/03_DOSSIE_BNDES")

    # Dividir o rascunho em partes menores (ex: por títulos de seção ##)
    partes = rascunho.split("\n## ")
    revisado_total = ""

    for i, parte in enumerate(partes):
        print(f"🧠 Analisando bloco {i+1} de {len(partes)}...")
        
        prompt = f"Analise este trecho de rascunho frente aos autos do projeto. " \
                 f"Mantenha o texto original e as cores, mas adicione notas técnicas do BNDES ao fim. " \
                 f"\n\nAUTOS: {autos[:5000]}\n\nTRECHO: {parte}"

        try:
            response = client.models.generate_content(model=MODEL_ID, contents=prompt)
            revisado_total += response.text + "\n\n"
            time.sleep(10) # Pausa de 10 segundos entre envios para não estourar a cota
        except Exception as e:
            print(f"⚠️ Erro no bloco {i+1}: {e}")
            revisado_total += parte + "\n\n(ERRO NA REVISÃO DESTA SEÇÃO)\n\n"

    with open("03_CONSOLIDADO_BNDES_REVISADO_V2.md", "w", encoding="utf-8") as f:
        f.write(revisado_total)
    print("✅ Concluído! Arquivo: 03_CONSOLIDADO_BNDES_REVISADO_V2.md")

if __name__ == "__main__":
    executar_revisao()
