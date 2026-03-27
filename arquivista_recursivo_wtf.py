import os
import shutil
import time
from google import genai

# 1. Configuração do Cliente
client = genai.Client(api_key=os.environ.get("AIzaSyDnUer8X3QiY0dJtK26xL9z8hGxbtm3R8A"))
MODEL_ID = "models/gemini-2.5-flash"

# 2. Definição de Rotas (Ajustadas para sua estrutura real)
ORIGEM_RAIZ = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/01_RAW_TRANSCRIPTS"
DESTINO_BASE = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/02_TECHNICAL_REVIEWS"

os.makedirs(DESTINO_BASE, exist_ok=True)

def classificar_e_limpar(conteudo, nome_arquivo):
    # Prompt de Elite para Triagem e Categorização Dinâmica
    prompt = f"""
    Atue como Bibliotecário Científico do Projeto Mulheres Que Tecem a Floresta.
    Analise o arquivo: {nome_arquivo}

    TAREFA 1: Avalie a relevância. Se for pessoal, vazio ou não-científico, responda 'DESCARTAR'.

    TAREFA 2: Defina Categoria/Subcategoria. 
    Ex: 'Bambu/Manejo', 'Bambu/Ensaios', 'Bioeconomia/Amazonia', 'Saneamento/Povos_Indigenas', 'PU_Vegetal/Propriedades'.

    TAREFA 3: Gere um Markdown (.md) limpo com:
    - Cabeçalho WTF (Ref: PES-TEC-{int(time.time()) % 10000}-2026)
    - Título, Autores e Resumo em Português
    - Tabelas de dados técnicos preservadas junto com o conteúdo textual íntegral. Sinalizar a existência de gráficos e imagens.
    - Incluir Bibliografia completa ABNT, DOI-sync.
    - Tag final: #CATEGORIA: Assunto/Subassunto - Caso exista diretório pré estabelecido, respeite-o e salve dentro. Caso contrário, crie um novo diretório com o nome da categoria.

    TEXTO BRUTO:
    {conteudo[:18000]}
    """
    try:
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text
    except Exception as e:
        return f"ERRO API: {e}"

def executar_garimpo_recursivo():
    print(f"🚀 Iniciando varredura recursiva em: {ORIGEM_RAIZ}")
    
    # os.walk percorre todas as subpastas automaticamente
    for raiz, diretorios, arquivos in os.walk(ORIGEM_RAIZ):
        txt_files = [f for f in arquivos if f.endswith('.txt')]
        
        for nome in txt_files:
            caminho_completo = os.path.join(raiz, nome)
            print(f"🔍 Analisando: {nome}...")

            with open(caminho_completo, 'r', encoding='utf-8') as f:
                texto = f.read()

                # --- INÍCIO DA TRAVA DE SEGURANÇA ---
            tamanho_caracteres = len(texto) 
            limite_alerta = 100000  # 100 mil caracteres (~25-30 páginas)
            
            if tamanho_caracteres > limite_alerta:
                print(f"⚠️  ARQUIVO GRANDE DETECTADO: {nome} ({tamanho_caracteres} caracteres)")
                texto = texto[:80000] + "\n\n[CONTEÚDO CORTADO POR TAMANHO EXCESSIVO]"
                print(f"✂️  Texto reduzido para os primeiros 80k caracteres.")
            # --- FIM DA TRAVA DE SEGURANÇA ---

                

            resultado = classificar_e_limpar(texto, nome)

            if "DESCARTAR" in resultado.upper()[:20]:
                print(f"🗑️  Ignorado: {nome}")
                continue

            # Extração da Categoria para criar a pasta
            try:
                # Busca a linha da categoria no final ou topo do resultado
                linha_cat = [l for l in resultado.split('\n') if "#CATEGORIA:" in l][-1]
                cat_relativa = linha_cat.split(":")[1].strip().replace(" ", "_")
            except:
                cat_relativa = "Outros/Geral"

            # Criar a estrutura de subpastas no destino
            caminho_final_pasta = os.path.join(DESTINO_BASE, cat_relativa)
            os.makedirs(caminho_final_pasta, exist_ok=True)

            # Salvar o arquivo lapidado
            nome_saida = nome.replace('.txt', '.md')
            with open(os.path.join(caminho_final_pasta, nome_saida), 'w', encoding='utf-8') as f_out:
                f_out.write(resultado)
            
            print(f"✅ Arquivado em {cat_relativa}: {nome_saida}")
            time.sleep(1.2) # Pausa de segurança

if __name__ == "__main__":
    executar_garimpo_recursivo()

# python arquivista_recursivo_wtf.py