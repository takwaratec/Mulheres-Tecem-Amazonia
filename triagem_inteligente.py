import os
import shutil
from google import genai

# 1. Configuração
client = genai.Client(api_key=os.environ.get("AIzaSyDnUer8X3QiY0dJtK26xL9z8hGxbtm3R8A"))
MODEL_ID = "models/gemini-2.5-flash"

PASTA_QUARENTENA = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/01_RAW_TRANSCRIPTS/99_QUARENTENA"
PASTA_APROVADOS = "04_PESQUISA_ANDAMENTO/Resenhas-tecnicas"

# Assuntos de interesse para o consórcio UnB/UFRR/UFAC
TEMAS_CHAVE = ["Tanino", "Pellets", "Biochar", "briquetes", "biodegradação", "biomassa", "bioenergia", "biocombustíveis"]

os.makedirs(PASTA_APROVADOS, exist_ok=True)

def avaliar_relevancia(texto_curto):
    prompt = f"""
    Analise o fragmento de texto abaixo. 
    Responda apenas 'SIM' se o assunto principal for um destes: {', '.join(TEMAS_CHAVE)}.
    Caso contrário, responda 'NAO'.

    1- Se for relevante, traduza o texto para português.
    2- Se for científico, continue com a lapidação.
    3- Se não for relevante, ignore o arquivo.
    
    Atue como Pesquisador Sênior e Analista de Dados do Projeto WTF. 
    Converta este texto bruto em uma FICHA CIENTÍFICA ESTRUTURADA.
    Evite saudações e informações desnecessárias. No início e no final do texto.

    ### 1. METADADOS E CABEÇALHO
    projeto: Mulheres Que Tecem a Floresta 
    instituicao: Consórcio UnB/UFRR/UFAC
    tipo: Pesquisa: Amazônia Setentrional (PES)
    referencia: PES-TEC-{int(time.time()) % 10000}-2026
    status: Ready
    
    REFERÊNCIA BIBLIOGRÁFICA (ABNT):
    [Extraia do texto: Autor, Ano, Título, Periódico/Local]

- name: Consórcio UnB/UFRR/UFAC
    date: '2026-03-24'

    ### 2. TRADUÇÃO E SÍNTESE TÉCNICA
    - Traduza o resumo (Abstract) se estiver em inglês.
    - Liste 3 palavras-chave em português.

    ### 3. EXTRAÇÃO DE DADOS (TABELA)
    - Apresente os principais dados numéricos/técnicos do texto em uma tabela Markdown, quando houver.
    - Se o documento for um PDF, extraia os dados das tabelas presentes no documento.
    - Extrair coordenadas geográficas, se houver. Pesquisar quando forem na área de abrangência do projeto.

    
    ### 4. Extrair Bibliografia citada no texto
    - Liste todas as referências bibliográficas citadas no texto.
    - Formate como ABNT.
    

    TEXTO BRUTO:


    TEXTO: {texto_curto[:2000]}  # Analisa os primeiros 2000 caracteres
    """
    try:
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return "SIM" in response.text.upper()
    except:
        return False

def executar_triagem():
    arquivos = [f for f in os.listdir(PASTA_QUARENTENA) if f.endswith('.txt')]
    print(f"🔎 Analisando {len(arquivos)} arquivos na quarentena...")

    for nome_arquivo in arquivos:
        caminho_origem = os.path.join(PASTA_QUARENTENA, nome_arquivo)
        
        with open(caminho_origem, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        if avaliar_relevancia(conteudo):
            print(f"✅ Relevante: {nome_arquivo}")
            # Move para a pasta de aprovados para posterior lapidação
            shutil.copy(caminho_origem, os.path.join(PASTA_APROVADOS, nome_arquivo))
        else:
            print(f"🌑 Ignorado: {nome_arquivo}")

if __name__ == "__main__":
    executar_triagem()


# python triagem_inteligente.py