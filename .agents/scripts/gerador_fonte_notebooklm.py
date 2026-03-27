# --- EXPLICAÇÃO DIDÁTICA PARA FABIO ---
# O QUE FAZ: Este script é o seu "Integrador de Fontes". Ele pega dezenas de resenhas técnicas 
# e laudos de laboratório e os compacta em um único arquivo (.md) otimizado para o NotebookLM.
# 
# POR QUE É NECESSÁRIO: O NotebookLM trabalha melhor quando recebe um "Dossiê de Fonte" 
# bem organizado com sumários e matrizes de dados, em vez de muitos arquivos pequenos picados.
#
# COMO EXPLORAR NO DIA-A-DIA: Use para criar as bases de conhecimento que você sobe no NotebookLM.

import os
import time
from google import genai

client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
MODEL_ID = "models/gemini-2.5-flash"

DIR_REVIEWS = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/02_TECHNICAL_REVIEWS"
DIR_SAIDA = "docs/04_PESQUISA_ANDAMENTO/Resenhas-tecnicas"

def gerar_dossie(conteudos):
    prompt = f"Consolide estes reviews em um único relatório para NotebookLM:\n\n" + "\n---\n".join(conteudos)
    try:
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text
    except Exception as e: return str(e)

if __name__ == "__main__":
    textos = []
    for root, dirs, files in os.walk(DIR_REVIEWS):
        for f in files:
            if f.endswith(".md"):
                with open(os.path.join(root, f), 'r') as file: textos.append(file.read())
    
    dossie = gerar_dossie(textos)
    os.makedirs(DIR_SAIDA, exist_ok=True)
    with open(os.path.join(DIR_SAIDA, f"DOSSIE_FONTE_NOTEBOOKLM_{int(time.time())}.md"), 'w') as f_out:
        f_out.write(dossie)
    print("✅ Dossie para NotebookLM gerado com sucesso!")
