import os
import random
import re
import time
import google.generativeai as genai

# --- CONFIGURAÇÃO DE CHAVE ---
def obter_chave():
    # 1. Tenta carregar do ambiente (VS Code Secret ou Export)
    chave = os.environ.get("GOOGLE_API_KEY")
    
    # 2. Tenta carregar do arquivo .env se não estiver no ambiente
    if not chave or chave.strip() == "":
        if os.path.exists(".env"):
            with open(".env", "r") as f:
                for line in f:
                    if line.startswith("GOOGLE_API_KEY="):
                        chave = line.split("=", 1)[1].strip().strip("'").strip('"')
                        break
    
    if not chave:
        print("❌ ERRO CRÍTICO: GOOGLE_API_KEY não configurada.")
        print("💡 Ação Necessária: Crie um arquivo .env com GOOGLE_API_KEY=sua_chave ou exporte a variável no terminal.")
        return None
    return chave

GEMINI_KEY = obter_chave()
genai.configure(api_key=GEMINI_KEY)

# --- CONEXÃO SOBERANA V2.3 (MULTI-MODEL FALLBACK - ULTRA STABLE) ---
def gerar_conteudo_com_fallback(prompt):
    # Lista de modelos por ordem de prioridade (Flash 1.5 -> Pro 1.5 -> Pro 1.0)
    # Incluímos aliases que funcionam melhor em diferentes níveis de permissão.
    modelos_para_tentar = [
        'gemini-1.5-flash',
        'gemini-1.5-flash-latest',
        'gemini-1.5-pro',
        'gemini-pro' # Este é o fallback definitivo (1.0 Pro)
    ]
    
    ultimo_erro = ""
    
    for nome_modelo in modelos_para_tentar:
        try:
            print(f"🧠 Ravi tentando motor: {nome_modelo}...")
            model = genai.GenerativeModel(nome_modelo)
            response = model.generate_content(
                f"Responda SEMPRE em Português do Brasil.\n\n{prompt}"
            )
            if response.text:
                return response.text
        except Exception as e:
            ultimo_erro = str(e)
            if "404" in ultimo_erro:
                print(f"⚠️ Motor {nome_modelo} indisponível (404). Tentando próximo...")
                continue
            elif "429" in ultimo_erro:
                print(f"⏳ Cota atingida em {nome_modelo}. Esperando 70s...")
                time.sleep(70)
                # Tenta o mesmo modelo de novo uma vez
                try:
                    response = model.generate_content(prompt)
                    if response.text: return response.text
                except: continue
            else:
                print(f"❌ Erro em {nome_modelo}: {ultimo_erro}")
                continue
                
    print(f"❌ FALHA CRÍTICA: Nenhum dos motores ({modelos_para_tentar}) respondeu.")
    print(f"💡 Dica: Verifique se a 'Generative Language API' está ATIVA no console Cloud do projeto.")
    return None
        
# --- CONFIGURAÇÕES DE IDENTIDADE ---
CORES = ["red", "green", "black"]

# --- PERFIS DE TRIAGEM ---
PERFIS = {
    "bioeconomia_master": {
        "dir_source": "_RESEARCH_RAW/BACKUP_LOCAL/99_RESTRITO/02_TRIAGEM_BRUTA/textos para edição/teste artigo",
        "dir_dest": "_RESEARCH_RAW/BACKUP_LOCAL/99_RESTRITO/02_TRIAGEM_BRUTA/textos para edição/teste artigo",
        "modo_fusao": True, 
        "system_prompt": "Estrategista de Bioeconomia e Ecologia Industrial. Una os dados dos relatórios em um artigo técnico coeso para o BNDES.",
        "sections": ["RESUMO EXECUTIVO INTEGRADO", "ANÁLISE DE CADEIAS (AÇAÍ/CASTANHA/BAMBU)", "LOGÍSTICA E ENERGIA", "CONCLUSÃO"],
        "depth": 6
    },
    "engenharia": { 
        "dir_source": "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/02_TECHNICAL_REVIEWS/Tecnoveg-Imperveg",
        "dir_dest": "docs/04_PESQUISA_ANDAMENTO/Resenhas-tecnicas",
        "modo_fusao": True,
        "system_prompt": "Editor Científico de Engenharia de Materiais (Qualis A1). Foco em TRL, tração, cura e normas NBR.",
        "sections": ["TÍTULO", "RESUMO", "MATERIAIS E MÉTODOS", "ANÁLISE DE TRL", "CONCLUSÃO"],
        "depth": 3
    }
}

def aplicar_estetica_mqtf(texto, ref_name, depth_level=1):
    prefixo = "../" * depth_level
    assets_rel = f"{prefixo}assets" if depth_level > 0 else "assets"
    
    metadata = f"""---
projeto: Mulheres Que Tecem a Floresta
instituicao: Consórcio UnB/UFRR/UFAC
tipo: Documento Técnico Consolidado
referencia: {ref_name}
status: Status Ready (revisão padrão)
author:
  - name: Consórcio UnB/UFRR/UFAC
date: '2026-03-29'
---

"""
    linhas = texto.split('\n')
    novas_linhas = []
    cor_idx = 0
    
    for linha in linhas:
        if linha.startswith("# "):
            face = f"face_{random.randint(1, 5)}.svg"
            tag = f'<img src="{assets_rel}/human_face/{face}" width="50px" style="transform: scaleX(-1); filter: invert(27%) sepia(91%) saturate(2352%) hue-rotate(346deg) brightness(104%) contrast(97%);"> '
            novas_linhas.append(f"# {tag} {linha[2:].strip()}")
        elif re.match(r"^[ \t]*[\*\-] ", linha) and "**" not in linha:
            icone = f"icon_{random.randint(1, 20)}.svg"
            cor = CORES[cor_idx % 3]
            cor_idx += 1
            tag = f'<img src="{assets_rel}/icons/{icone}" width="15px"> '
            novas_linhas.append(f"* <span style='color:{cor}'>{tag} {linha[2:].strip()}</span>")
        else:
            novas_linhas.append(linha)

    footer = f'\n\n<p align="center"><img src="{assets_rel}/logo_BQTF/logo_mqtf_soberana.svg" width="40px"><br><b>MQTF</b><br><i>"Soberania não se pede, se exerce."</i></p>'
    return metadata + "\n".join(novas_linhas) + footer

def executar_processamento(profile_name):
    p = PERFIS[profile_name]
    base_dir = os.getcwd()
    source_path = os.path.join(base_dir, p['dir_source'])
    dest_path = os.path.join(base_dir, p['dir_dest'])
    
    if not os.path.exists(source_path):
        print(f"❌ Erro: Pasta {source_path} não encontrada.")
        return

    os.makedirs(dest_path, exist_ok=True)
    arquivos = [os.path.join(source_path, f) for f in os.listdir(source_path) if f.endswith(".md")]

    if not arquivos:
        print(f"⚠️ Alerta: Nenhum arquivo .md encontrado em {source_path}.")
        return

    if p['modo_fusao']:
        print(f"🌀 Consolidando {len(arquivos)} arquivos do perfil: {profile_name}...")
        contexto = ""
        for caminho in arquivos:
            with open(caminho, 'r', encoding='utf-8') as f:
                contexto += f"\n\n--- ORIGEM: {os.path.basename(caminho)} ---\n" + f.read()
        
        prompt = f"Instrução: {p['system_prompt']}\nEstrutura: {p['sections']}\n\nDados:\n{contexto}"
        
        artigo_bruto = gerar_conteudo_com_fallback(prompt)
        
        if artigo_bruto:
            final = aplicar_estetica_mqtf(artigo_bruto, f"Consolidacao_{profile_name}", depth_level=p.get('depth', 1))
            saida = os.path.join(dest_path, f"MASTER_ARTIGO_{profile_name}.md")
            with open(saida, 'w', encoding='utf-8') as f_out:
                f_out.write(final)
            print(f"🏆 VITÓRIA! Arquivo Mestre gerado em: {saida}")
        else:
            print("❌ FALHA CRÍTICA: O Ravi não conseguiu gerar o texto.")

if __name__ == "__main__":
    executar_processamento("bioeconomia_master")