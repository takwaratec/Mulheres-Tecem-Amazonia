import os
import time
from google import genai

# 1. Configuração da API (Recomenda-se usar variável de ambiente)
# os.environ["GOOGLE_API_KEY"] = "SUA_CHAVE_AQUI"
client = genai.Client(api_key=os.environ.get("AIzaSyDnUer8X3QiY0dJtK26xL9z8hGxbtm3R8A"))
MODEL_ID = "models/gemini-2.5-flash"

# 2. Caminhos Estruturados
DIR_BRUTO = "99_RESTRITO/02_TRIAGEM_BRUTA/WA_MAM/Tecnoveg/Tecnoveg-markdown"
DIR_REVIEWS = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/02_TECHNICAL_REVIEWS/Tecnoveg-Imperveg"

os.makedirs(DIR_REVIEWS, exist_ok=True)

def gerar_review_tecnico(texto_bruto, nome_arquivo):
    """
    Envia o texto para a IA com lógica de retentativa (Retry) para erro 503.
    """
    referencia_id = int(time.time()) % 10000
    data_hoje = time.strftime('%d/%m/%Y')

    # Configuração de extração universal e tradução técnica brasileira
    prompt = f"""
    Atue como um Engenheiro de Materiais e Revisor Técnico.
    Sua missão é converter o texto bruto de um laudo em um Review Técnico de alta qualidade.

    ### REGRAS DE TRADUÇÃO E TERMINOLOGIA (PADRÃO BRASIL):
    Substitua sistematicamente os termos originais pelos equivalentes no Brasil:
    - Betão -> Concreto
    - Provetes -> Amostras / Corpos de Prova
    - Suporte -> Substrato
    - Armadura -> Ferragem / Armadura
    - Sais descongelantes -> Sais de degelo
    - Resistência à tração por arrancamento -> Resistência adesiva (Pull-off)

    ### FORMATO DE SAÍDA (Markdown):
    
    # REVIEW TÉCNICO: [Extraia o Nome do Material/Produto]
    **Referência do Review:** PES-REV-{int(time.time()) % 10000}-2026
    **Data do Ensaio:** [Extraia a data original do laudo]
    **Local do Ensaio:** [Extraia a cidade/país e o laboratório original]
    **Órgão Emissor:** [Ex: ITecons, Rocholl, etc.]
    **Solicitante:** [Ex: Tecnoveg]

    ---

    ## 1. Tabelas de Resultados
    [Transcreva fielmente as tabelas de dados, medidas e resultados, aplicando a tradução para Português do Brasil]

    ## 2. Memorando de Avaliação
    [Redija uma análise técnica do desempenho do material.
    - TRADUÇÃO: Use apenas terminologia técnica brasileira.
    - METÁFORAS: Utilize analogias didáticas para explicar resultados complexos para leigos (ex: comparar a aderência a uma "âncora" ou a resiliência a "raízes").
    - FOCO: Seja direto sobre a eficácia do material frente às normas citadas. 
    - RESTRIÇÃO: NÃO faça comentários de associação a projetos externos.]

    ## 3. Notas para Escrita Científica
    - Título sugerido para artigo.
    - 3 Argumentos fortes baseados nos dados para a seção de Discussão.

    ---
    **Autor da Análise:** Fabio Resck Takwara (ORCID: "0009-0002-6044-2583")
    **Data da Revisão:** {time.strftime('%d/%m/%Y')}
    **Local da Análise:** "São Paulo-SP"

    TEXTO BRUTO RECUPERADO:
    {texto_bruto[:40000]}
    """
    # Estratégia de Retentativa (Retry) para lidar com sobrecarga do servidor
    for tentativa in range(3):
        try:
            response = client.models.generate_content(model=MODEL_ID, contents=prompt)
            return response.text
        except Exception as e:
            if "503" in str(e) or "overloaded" in str(e).lower():
                espera = (tentativa + 1) * 15
                print(f"⚠️ Servidor instável (503). Tentativa {tentativa+1}/3. Aguardando {espera}s...")
                time.sleep(espera)
            else:
                return f"❌ Erro Crítico na API: {e}"
    
    return "❌ Erro: O servidor permaneceu indisponível após 3 tentativas."

def processar_tecnoveg():
    print(f"🚀 Verificando pasta de origem: {DIR_BRUTO}")
    
    if not os.path.exists(DIR_BRUTO):
        print(f"❌ ERRO: Caminho não encontrado: {DIR_BRUTO}")
        return

    arquivos = [f for f in os.listdir(DIR_BRUTO) if f.endswith(".md") or f.endswith(".txt")]
    print(f"📂 Encontrados {len(arquivos)} arquivos para processar.")

    for nome in arquivos:
        if nome.startswith("._") or nome.startswith("~"):
            continue
            
        caminho_in = os.path.join(DIR_BRUTO, nome)
        print(f"🔬 Processando: {nome}")

        try:
            with open(caminho_in, 'r', encoding='utf-8') as f:
                conteudo = f.read()

            review_final = gerar_review_tecnico(conteudo, nome)

            nome_saida = f"REVIEW_{nome.replace('.txt', '.md')}"
            caminho_out = os.path.join(DIR_REVIEWS, nome_saida)
                    
            with open(caminho_out, 'w', encoding='utf-8') as f_out:
                f_out.write(review_final)
                    
            print(f"✅ Gerado com sucesso: {nome_saida}")
            time.sleep(3) # Pausa estratégica para evitar 503

        except Exception as e:
            print(f"❌ Falha ao ler arquivo {nome}: {e}")

if __name__ == "__main__":
    processar_tecnoveg()

# python gerador_review_tecnoveg.py