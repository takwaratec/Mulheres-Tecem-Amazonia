# --- EXPLICAÇÃO DIDÁTICA PARA FABIO ---
# O QUE FAZ: Este é o seu "Laboratório de Prompts". Ele abre um canal direto com o cérebro 
# do Gemini 2.5-flash para você testar ideias rápidas, fazer perguntas sobre o projeto 
# ou pedir para a IA explicar um conceito técnico complexo.
# 
# POR QUE É NECESSÁRIO: É a forma mais barata e rápida de validar ideias antes de rodar 
# os geradores de artigos automáticos em massa.
#
# COMO EXPLORAR NO DIA-A-DIA: Use para "brainstorming" sobre as invenções T01-T12.
# COMO PEDIR AOS AGENTES: "Abra o gemini_lab.py e me ajude a pensar sobre a Balsa a Vapor".

import os
from google import genai

# 1. Configuração (Puxando a chave do seu ambiente seguro)
API_KEY = os.environ.get("GOOGLE_API_KEY")
client = genai.Client(api_key=API_KEY)
MODEL_ID = "models/gemini-2.5-flash"

def perguntar_ao_ravi(pergunta):
    print(f"🧠 Ravi pensando...")
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=f"Contexto: Projeto Mulheres Que Tecem a Floresta (MQTF).\nPergunta: {pergunta}"
        )
        return response.text
    except Exception as e:
        return f"Erro na conexão com o cérebro da IA: {e}"

if __name__ == "__main__":
    print("--- MQTF GEMINI LAB (RAVI) ---")
    while True:
        user_input = input("\nFabio: ")
        if user_input.lower() in ["sair", "exit"]: break
        resposta = perguntar_ao_ravi(user_input)
        print(f"\nRavi: {resposta}")
