import os
import shutil
import time
from google import genai

# 1. Configuração do Cliente
client = genai.Client(api_key=os.environ.get("AIzaSyDnUer8X3QiY0dJtK26xL9z8hGxbtm3R8A"))
MODEL_ID = "models/gemini-2.5-flash"

# 2. Caminhos das Pastas
PASTA_QUARENTENA = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/01_RAW_TRANSCRIPTS/99_QUARENTENA"
PASTA_LAPIDADOS = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/01_RAW_TRANSCRIPTS/01_CIENTIFICO"
TEMAS_CHAVE = ["Tanino", "Pellets", "Biochar", "briquetes", "biodegradação", "biomassa", "bioenergia", "biocombustíveis"]

os.makedirs(PASTA_LAPIDADOS, exist_ok=True)

def avaliar_e_lapidar(nome_arquivo, conteudo):
    # Prompt Único: Filtra e, se relevante, já gera a ficha
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
    

    TEXTO: {conteudo[:5000]}
    """
    
    try:
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text
    except Exception as e:
        return f"ERRO: {e}"

def executar():
    arquivos = [f for f in os.listdir(PASTA_QUARENTENA) if f.endswith('.txt')]
    print(f"🚀 Iniciando triagem de {len(arquivos)} arquivos...")

    for nome in arquivos:
        caminho = os.path.join(PASTA_QUARENTENA, nome)
        with open(caminho, 'r', encoding='utf-8') as f:
            texto = f.read()

        resultado = avaliar_e_lapidar(nome, texto)

        if "IRRELEVANTE" in resultado.upper():
            print(f"🌑 Pulado: {nome}")
        else:
            nome_saida = f"FICHA_{nome.replace('.txt', '.md')}"
            with open(os.path.join(PASTA_LAPIDADOS, nome_saida), 'w') as f_out:
                f_out.write(resultado)
            print(f"✅ Lapidado: {nome_saida}")
        
        time.sleep(1) # Evita bloqueio por excesso de velocidade

if __name__ == "__main__":
    executar()


# python triagem_e_lapidacao.py