import os
import sys
import time
from google import genai

# 1. Configuração do Cliente e Modelo
client = genai.Client(api_key=os.environ.get("AIzaSyDnUer8X3QiY0dJtK26xL9z8hGxbtm3R8A"))
MODEL_ID = "models/gemini-2.5-flash"

# 2. Definição das Pastas
PASTA_BRUTA = "99_RESTRITO/02_TRIAGEM_BRUTA/WA_MAM/Naval_Ribeirinhos/MARINHA-AM.pdf"
PASTA_DESTINO = "01_GOVERNANCA/00_MASTER/Bibliografia_de_Regencia"

# Criar pasta de destino se não existir
os.makedirs(PASTA_DESTINO, exist_ok=True)

def processar_arquivo(caminho_entrada, nome_arquivo):
    print(f"💎 Lapidando: {nome_arquivo}...")
    
    with open(caminho_entrada, 'r', encoding='utf-8') as f:
        texto_bruto = f.read()

    # O SEU PROMPT PADRÃO OURO
    prompt = f"""
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

    ### 4. RELAÇÃO COM O PROJETO (CONEXÃO WTF)
    - Como isso beneficia as mulheres extrativistas?
    - Quais as diretrizes para o projeto e a bioeconomia?

    ### 5. Extrair Bibliografia citada no texto
    - Liste todas as referências bibliográficas citadas no texto.
    - Formate como ABNT.
    

    TEXTO BRUTO:
    {texto_bruto}
    """

    try:
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        
        nome_saida = f"FICHA_{nome_arquivo.replace('.txt', '.md')}"
        caminho_saida = os.path.join(PASTA_DESTINO, nome_saida)
        
        with open(caminho_saida, 'w', encoding='utf-8') as f_out:
            f_out.write(response.text)
        
        print(f"✅ Concluído: {nome_saida}")
        
    except Exception as e:
        print(f"❌ Erro ao processar {nome_arquivo}: {e}")

def executar_lote():
    arquivos = [f for f in os.listdir(PASTA_BRUTA) if f.endswith('.txt')]
    
    if not arquivos:
        print("📭 Nenhun arquivo .txt encontrado na pasta bruta.")
        return

    print(f"🚀 Iniciando processamento de {len(arquivos)} arquivos...")
    for arquivo in arquivos:
        caminho_completo = os.path.join(PASTA_BRUTA, arquivo)
        processar_arquivo(caminho_completo, arquivo)
        time.sleep(2) # Pequena pausa para evitar limite de taxa (Rate Limit)

if __name__ == "__main__":
    executar_lote()

# python lapidar_lote.py