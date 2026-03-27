# --- EXPLICAÇÃO DIDÁTICA PARA FABIO ---
# O QUE FAZ: Este é o seu "Motor de Escrita Técnica". Ele pega as resenhas e dados brutos 
# de uma pasta e os transforma em artigos científicos estruturados (Título, Resumo, Introdução, etc.) 
# com perfis específicos: Engenharia ou Antropologia.
# 
# POR QUE É NECESSÁRIO: É fundamental para escalar a produção de conteúdos do portal, 
# garantindo que todos os laudos técnicos do IMPERVEG e estudos etnográficos tenham 
# o mesmo padrão acadêmico de alta qualidade.
#
# COMO EXPLORAR NO DIA-A-DIA: Use para gerar os rascunhos de capítulos do seu Dossiê BNDES.
# COMO PEDIR AOS AGENTES: "Use o gerador_artigos_lote.py com o perfil 'engenharia' para redigir os reviews da pasta Tecnoveg".

import os
import time
from google import genai

# Configuração da API
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
MODEL_ID = "models/gemini-2.5-flash"

PERFIS = {
    "engenharia": {
        "dir_source": "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/02_TECHNICAL_REVIEWS/Tecnoveg-Imperveg",
        "dir_dest": "docs/04_PESQUISA_ANDAMENTO/Resenhas-tecnicas",
        "system_prompt": "Editor Científico de uma revista de Engenharia de Materiais (Qualis A1).",
        "sections": ["TÍTULO acadêmico", "RESUMO", "INTRODUÇÃO", "MATERIAIS E MÉTODOS", "RESULTADOS", "CONCLUSÃO"]
    },
    "antropologia": {
        "dir_source": "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/02_TECHNICAL_REVIEWS/Pesquisa-Etnografica",
        "dir_dest": "docs/04_PESQUISA_ANDAMENTO/Analises-Culturais",
        "system_prompt": "Antropólogo Sênior e Historiador de Arte Indígena Amazônica.",
        "sections": ["TÍTULO", "INTRODUÇÃO", "ANÁLISE ETNOGRÁFICA", "TABELA DE SIGNIFICADOS", "CONCLUSÃO", "BIBLIOGRAFIA"]
    }
}

def redigir_documento(conteudo, profile_name):
    profile = PERFIS.get(profile_name)
    prompt = f"Atue como {profile['system_prompt']}\nEstrutura: {profile['sections']}\nConteúdo: {conteudo}"
    try:
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text
    except Exception as e: return f"Erro: {e}"

def executar_lote(profile_name):
    profile = PERFIS.get(profile_name)
    os.makedirs(profile['dir_dest'], exist_ok=True)
    for nome in os.listdir(profile['dir_source']):
        if nome.endswith(".md"):
            with open(os.path.join(profile['dir_source'], nome), 'r') as f:
                resultado = redigir_documento(f.read(), profile_name)
            with open(os.path.join(profile['dir_dest'], f"ARTIGO_{nome}"), 'w') as f_out:
                f_out.write(resultado)
            print(f"✅ Artigo gerado: {nome}")
            time.sleep(1)

if __name__ == "__main__":
    executar_lote("engenharia")
