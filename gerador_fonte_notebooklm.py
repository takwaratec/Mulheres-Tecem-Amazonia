import os
import time
from google import genai

# 1. Configuração da API
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
MODEL_ID = "models/gemini-2.5-flash"

# 2. Caminhos
DIR_REVIEWS = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/02_TECHNICAL_REVIEWS/Tecnoveg-Imperveg"
DIR_FONTE_NLM = "04_PESQUISA_ANDAMENTO/Resenhas-tecnicas"

os.makedirs(DIR_FONTE_NLM, exist_ok=True)

def gerar_dossie_consolidado(lista_conteudos, tema_geral):
    """
    Consolida reviews em um único arquivo de fonte otimizado para NotebookLM.
    """
    contexto_reviews = "\n\n--- INÍCIO DE DOCUMENTO DE FONTE ---\n\n".join(lista_conteudos)
    
    prompt = f"""
    Atue como um Especialista em Gestão de Conhecimento e Engenharia.
    Sua tarefa é organizar uma COLETÂNEA DE EVIDÊNCIAS TÉCNICAS para ser processada no NotebookLM.

    ### OBJETIVO:
    Criar um documento de fonte único que correlacione os ensaios do IMPERVEG RQI 132.

    ### ESTRUTURA DO DOCUMENTO:
    1. SUMÁRIO EXECUTIVO: Resumo de todos os laudos (Aderência, Permeabilidade e Ciclos Térmicos).
    2. METODOLOGIA UNIFICADA: Explique que os testes foram realizados no ITecons (Coimbra) e liste as normas brasileiras equivalentes (ABNT).
    3. MATRIZ DE DADOS: Organize os resultados (MPa, Sd, µ) em seções claras.
    4. INTERPRETAÇÃO TÉCNICA (METÁFORAS): Mantenha as explicações didáticas (âncora, escudo, seiva) pois o NotebookLM as usará para explicar o material a leigos.
    5. ANÁLISE CRÍTICA: Discuta a performance global e a questão da soberania tecnológica (fuga para validação no exterior).

    ### REGRAS DE OURO:
    - Tradução: "Betão" para "Concreto", "Provetes" para "Amostras".
    - Mantenha IDs de Referência (Ex: PES-REV-XXXX) para que o NotebookLM possa citar as fontes.

    DADOS DOS REVIEWS:
    {contexto_reviews[:65000]}
    """

    try:
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text
    except Exception as e:
        return f"Erro na geração da fonte: {e}"

def executar_preparacao_nlm():
    print(f"📂 Lendo reviews para o NotebookLM...")
    
    arquivos = [f for f in os.listdir(DIR_REVIEWS) if f.endswith(".md")]
    conteudos = []

    for nome in arquivos:
        with open(os.path.join(DIR_REVIEWS, nome), 'r', encoding='utf-8') as f:
            conteudos.append(f.read())

    if not conteudos:
        print("⚠️  Nenhum review encontrado.")
        return

    print(f"🧠 Consolidando {len(conteudos)} laudos em uma fonte única para NotebookLM...")
    dossie = gerar_dossie_consolidado(conteudos, "Performance Global PU Vegetal Mamona")

    nome_saida = f"DOSSIE_FONTE_NOTEBOOKLM_{int(time.time())}.md"
    with open(os.path.join(DIR_FONTE_NLM, nome_saida), 'w', encoding='utf-8') as f_out:
        f_out.write(dossie)
            
    print(f"✅ Fonte preparada: {nome_saida}")

if __name__ == "__main__":
    executar_preparacao_nlm()