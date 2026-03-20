import os, glob, json, urllib.request, ssl, time

import re
# --- Configurações de Ambiente ---
context = ssl._create_unverified_context()
ORIGEM_BASE = '04_PESQUISA_ANDAMENTO/TRANSCRIPT'
DESTINO_MD = '04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/02_TECHNICAL_REVIEWS'
API_KEY = os.getenv('GOOGLE_API_KEY')

# --- Prompt Estratégico (Padrão BNDES) ---
PROMPT_ESTRATEGICO = """Atue como Estrategista Sênior e Projetista BNDES. 
Analise o texto técnico fornecido e extraia informações para um Resumo Estratégico e Comparativo de P&D.
O objetivo é fundamentar a defesa do projeto "Mulheres Que Tecem a Floresta" e nortear o CAPEX (investimentos).

Responda RIGOROSAMENTE no formato:
---
title: "Resumo Estratégico e Comparativo P&D - [Nome Curto do Documento]"
status: "Ativo"
tags: ["P&D", "[Tag1]", "[Tag2]", "[Tag3]"]
---

# Resumo Estratégico de Pesquisa e Desenvolvimento (P&D)
**Gestão de Componente:** [Identifique o componente: Açaí, Castanha, Bioinsumos, Bambu, ou Engenharia].

[Breve parágrafo de síntese dos ativos de informação e norteamento estratégico].

---

## 1. Informação Complementar e Defesa do Projeto

### 1.1. [Tecnologia/Conceito Identificado]
- [Descrição sucinta da viabilidade técnica baseada no texto].
  - **Argumento de Defesa**: [Como isso justifica a existência ou a escolha técnica do projeto perante o BNDES].

---

## 2. Comparativo de Valores e Norteamento Estratégico (Equipamentos)

### 2.1. Escala Aprovada e Legitimação
- [Cite referências de órgãos como Embrapa, INPA ou Universidades que legitimam essa tecnologia].

### 2.2. Referências de CAPEX / Maquinário
- [Identifique máquinas, marcas ou sistemas citados e como eles ancoram as rubricas orçamentárias].
- **Norteamento Estratégico Mestre:** [Justificativa final para a alocação de recursos e modernização da infraestrutura].

---
*Anexos e Documentos Originais (*.pdf) encontram-se dispostos na pasta `02_PESQUISA_DESENVOLVIMENTO` para consulta da coordenação técnica do componente R&D.*
"""

# --- Configurações de Filtro ---
SKIP_KEYWORDS = [
    'FABIO RESCK', 'RESCK', 'MEMORANDO', 'MEMO', 'EMAIL', 'GMAIL', 
    'DENUNCIA', 'QUEIXA', 'COMPROVANTE', 'CERTIFICADO', 'ADVERTENCIA',
    'FORMULÁRIO', 'RECURSOS HUMANOS', 'FINANCEIRO', 'MANIFESTAÇÃO',
    'CONVOCAÇÃO', 'REGIMENTO', 'RETRETACAO', 'ADVERTENCIA'
]
QUARANTINE_DIR = '04_PESQUISA_ANDAMENTO/TRANSCRIPT/QUARANTINE_NON_TECHNICAL'

def slugify(text):
    import re
    text = text.lower()
    # Substituir caracteres especiais e acentos
    import unicodedata
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '_', text)
    return text.strip('_')

# Use recursive glob to catch files in subdirectories
for arq_path in glob.glob(f'{ORIGEM_BASE}/**/RAW_*.txt', recursive=True):
    nome_base_lower = os.path.basename(arq_path).upper()
    
    # Check if file should be skipped based on filename
    skip = any(kw in nome_base_lower for kw in SKIP_KEYWORDS)
    
    if skip:
        print(f"🚫 Filtrando (Arquivístico): {nome_base_lower}")
        try:
            os.rename(arq_path, f"{QUARANTINE_DIR}/{os.path.basename(arq_path)}")
        except Exception as e:
            print(f"⚠️ Erro ao mover {arq_path} para quarentena: {e}")
        continue

    nome_base = os.path.basename(arq_path).replace('.txt', '').replace('RAW_', '')
    nome_slug = slugify(nome_base)
    dest_path = f'{DESTINO_MD}/WTF_RES_{nome_slug}.md'

    if os.path.exists(dest_path):
        print(f"⏩ Pulando (Já existe): {nome_base}")
        continue

    print(f"🔬 Extraindo Ciência: {nome_base}...")
    
    try:
        with open(arq_path, 'r', encoding='utf-8', errors='ignore') as f:
            # Read full file for deeper analysis if not too huge
            texto = f.read()[:20000] # Increased context window
            
            # Check content for Fabio Resck as a safety measure
            if "FABIO RESCK" in texto.upper():
                print(f"🚫 Filtrando (Conteúdo Restrito): {nome_base}")
                os.rename(arq_path, f"{QUARANTINE_DIR}/{os.path.basename(arq_path)}")
                continue

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro:generateContent?key={API_KEY}"
        data = {"contents": [{"parts": [{"text": f"{PROMPT_ESTRATEGICO}\n\nTexto: {texto}"}]}]}
        
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
        
        with urllib.request.urlopen(req, context=context) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            markdown_cientifico = res_data['candidates'][0]['content']['parts'][0]['text']
            
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(markdown_cientifico)
            print(f"✅ Ficha Estratégica Atualizada!")
            time.sleep(1) # Cota segura para Nível Pago 1

    except Exception as e:
        print(f"⚠️ Erro em {nome_base}: {e}")