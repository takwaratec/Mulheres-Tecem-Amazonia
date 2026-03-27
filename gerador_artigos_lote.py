import os
import time
from google import genai

# 1. Configuração da API
# Nota: A chave de API deve ser mantida em variável de ambiente por segurança.
API_KEY = os.environ.get("GEMINI_API_KEY") or "AIzaSyDnUer8X3QiY0dJtK26xL9z8hGxbtm3R8A"
client = genai.Client(api_key=API_KEY)
MODEL_ID = "models/gemini-2.0-flash" # Retornado para a versão estável solicitada

# 2. Definição de Perfis de Processamento
PERFIS = {
    "engenharia": {
        "dir_source": "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/02_TECHNICAL_REVIEWS/Tecnoveg-Imperveg",
        "dir_dest": "04_PESQUISA_ANDAMENTO/Resenhas-tecnicas",
        "system_prompt": "Editor Científico de uma revista de Engenharia de Materiais (Qualis A1).",
        "sections": [
            "TÍTULO acadêmico",
            "RESUMO (Abstract)",
            "INTRODUÇÃO (Polímeros vegetais e aderência)",
            "MATERIAIS E MÉTODOS (PU Vegetal/Mamona, normas EN 1542, EN 13687)",
            "RESULTADOS E DISCUSSÃO (Tabelas e metáforas dos 1.1/1.3 MPa)",
            "CONCLUSÃO (Viabilidade técnica)"
        ]
    },
    "antropologia": {
        "dir_source": "DOCLING_PDF-MD/DOCLING_PDF-MD",
        "dir_dest": "02_DIAGNOSTICO DE AREA",
        "system_prompt": "Antropólogo Sênior e Historiador de Arte Indígena Amazônica.",
        "sections": [
            "TÍTULO (Foco em Patrimônio e Identidade)",
            "INTRODUÇÃO (Grafismo como linguagem e proteção)",
            "ANÁLISE ETNOGRÁFICA (Dados dos documentos analisados)",
            "TABELA DE SIGNIFICADOS (Comparando grafismos e etnias)",
            "CONCLUSÃO (Sublimação de culturas e preservação)",
            "BIBLIOGRAFIA (Padrão ABNT baseado nas fontes)"
        ]
    }
}

# 3. Catálogo de Vetores
DIR_VETORES = "PESQUISA_GRAFISMO/CATALOGO_GRAFISMOS_VETOR"

def indexar_vetores():
    """Mapeia SVGs para suas respectivas páginas de origem."""
    index = {}
    if not os.path.exists(DIR_VETORES):
        return index
    
    for nome in os.listdir(DIR_VETORES):
        if nome.endswith(".svg"):
            # Ex: recorte_10_Lux_Vidal_Etnolinguistica_p131_0.svg -> p131
            partes = nome.split("_")
            for p in partes:
                if p.startswith("p") and p[1:].isdigit():
                    if p not in index:
                        index[p] = []
                    index[p].append(nome)
                    break
    return index

def redigir_documento(conteudo, profile_name, tema_central, tonica):
    profile = PERFIS.get(profile_name)
    if not profile:
        return f"Erro: Perfil '{profile_name}' não encontrado."

    sections_str = "\n    ".join([f"- {s}" for s in profile['sections']])
    
    # Busca vetores disponíveis se for o perfil de antropologia
    vetores_info = ""
    if profile_name == "antropologia":
        index = indexar_vetores()
        vetores_disponiveis = []
        for pg, files in index.items():
            vetores_disponiveis.append(f"{pg}: {', '.join(files[:3])}")
        
        vetores_info = f"""
    ### ICONOGRAFIA DISPONÍVEL (VETORES SVG):
    Você pode inserir ícones do catálogo usando a sintaxe Markdown:
    `![Grafismo](path/to/vetor.svg){{ .svg-custom-color }}`
    
    Catálogo por página indexada:
    {chr(10).join(vetores_disponiveis[:20])} 
    
    Nota: Use o caminho completo: {DIR_VETORES}/[nome_do_arquivo].svg
    """

    prompt = f"""
    Atue como {profile['system_prompt']}
    Sua tarefa é redigir um documento estruturado baseado no conteúdo fornecido.

    ### PARÂMETROS:
    - TEMA CENTRAL: {tema_central}
    - TÔNICA/ESTILO: {tonica}
    - IDIOMA: Português do Brasil.

    {vetores_info}

    ### ESTRUTURA OBRIGATÓRIA:
    {sections_str}

    ### REGRAS ESPECÍFICAS:
    - Se Antropologia: Integre ícones SVG do catálogo acima sempre que citar conteúdos das páginas correspondentes. 
    - Exemplo: Se citar a p. 115, use um SVG que contenha "p115" no nome.
    - Mantenha o rigor dos dados citados nas fontes.

    CONTEÚDO BASE:
    {conteudo}
    """

    # Lógica de Retry com espera progressiva (Estabilizada)
    for tentativa in range(5):
        try:
            response = client.models.generate_content(model=MODEL_ID, contents=prompt)
            return response.text
        except Exception as e:
            if "429" in str(e):
                tempo_espera = (tentativa + 1) * 30
                print(f"⚠️ Cota atingida (429). Ravi tirando um cochilo de {tempo_espera}s...")
                time.sleep(tempo_espera)
            else:
                print(f"❌ Erro inesperado: {e}")
                time.sleep(10)
    
    return "Falha total após retentativas. Verifique o Google AI Studio."

def executar_processamento(profile_name, tema, tonica, consolidar=False):
    profile = PERFIS.get(profile_name)
    if not profile:
        print(f"❌ Perfil {profile_name} inválido.")
        return

    os.makedirs(profile['dir_dest'], exist_ok=True)
    arquivos = [f for f in os.listdir(profile['dir_source']) if f.endswith(".md")]
    
    # Filtro opcional para o caso de antropologia (evitar arquivos sistêmicos)
    if profile_name == "antropologia":
        arquivos = [f for f in arquivos if any(s in f for s in ["Huni", "Lux", "Rossandra"])]

    print(f"🚀 Iniciando Processamento [{profile_name}]...")
    
    if consolidar:
        print(f"📚 Consolidando {len(arquivos)} arquivos em um único relatório...")
        conteudo_total = ""
        for nome in arquivos:
            with open(os.path.join(profile['dir_source'], nome), 'r', encoding='utf-8') as f:
                conteudo_total += f"\n--- FONTE: {nome} ---\n" + f.read()
        
        resultado = redigir_documento(conteudo_total, profile_name, tema, tonica)
        nome_saida = f"WTF-DIAG-001_Patrimonio_Imaterial_Consolidado.md"
        with open(os.path.join(profile['dir_dest'], nome_saida), 'w', encoding='utf-8') as f_out:
            f_out.write(resultado)
        print(f"✅ Consolidação finalizada: {nome_saida}")
    else:
        for nome in arquivos:
            print(f"✍️ Processando: {nome}")
            with open(os.path.join(profile['dir_source'], nome), 'r', encoding='utf-8') as f:
                conteudo = f.read()
            resultado = redigir_documento(conteudo, profile_name, tema, tonica)
            nome_saida = f"RELATORIO_{profile_name.upper()}_{nome}"
            with open(os.path.join(profile['dir_dest'], nome_saida), 'w', encoding='utf-8') as f_out:
                f_out.write(resultado)
            print(f"✅ Arquivo concluído: {nome_saida}")
            time.sleep(2)

if __name__ == "__main__":
    # Exemplo de uso para Patrimônio Imaterial (Consolidado)
    tema_cultura = "Patrimônio Imaterial e Sublimação de Culturas: Grafismos Huni Kuĩ e Kaiowá"
    tonica_cultura = "Foco na preservação da identidade, linguagem simbólica e resistência através da estética."
    
    # Para o caso solicitado pelo usuário:
    executar_processamento("antropologia", tema_cultura, tonica_cultura, consolidar=True)