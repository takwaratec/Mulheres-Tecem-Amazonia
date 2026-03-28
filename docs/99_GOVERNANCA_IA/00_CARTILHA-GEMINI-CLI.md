---
## 🏗️ 1. O "Be-a-Bá" de Ativação (Sempre que abrir o Terminal)

Toda vez que você abrir o terminal para trabalhar no projeto, o Ravi precisa saber em qual "caixa de ferramentas" mexer.

```bash
# 1. Entre na pasta do projeto
cd ~/Documents/GitHub/UnB/Mulheres-Tecem-Amazonia

# 2. Ative o ambiente virtual (O facão do Ravi)
source venv/bin/activate

# 3. Garanta que a chave da API está viva na sessão
export GOOGLE_API_KEY='AIzaSyDnUer8X3QiY0dJtK26xL9z8hGxbtm3R8A'
```
---

![Status: Em Revisão](https://img.shields.io/badge/Status-Em_Revisão-yellow)

<p align="right"><i>"A força do lugar é a força do mundo."<br>— Milton Santos</i></p>

### <img src="../../../assets/patterns/square_05_red.svg" width="22px"> Ficha Técnica e Metadados
*   **Projeto**: Mulheres Que Tecem a Floresta (MQTF)
*   **Instituição**: Consórcio UnB / UFRR / UFAC
*   **Referência**: 00_CARTILHA-GEMINI-CLI.md
*   **Status**: Status Em Revisão
*   **Autor**: Consórcio UnB / UFRR / UFAC
*   **Data**: 27 de Março de 2026

## <img src="../../../assets/icons/human_01_red.svg" width="18px"> Cartilha de Uso: Gemini 2.5 no Terminal (Projeto WTF)
Companheiro, vamos colocar ordem na casa. O Ravi (seu Mac) e o Antigravity (seu servidor/ambiente de desenvolvimento) precisam dessa batida ritmada para o **Consórcio UnB/UFRR/UFAC** funcionar como uma linha de produção de alta precisão.

Aqui está o seu **Manual de Operações WTF 2026**.



## <img src="../../../assets/icons/human_01_red.svg" width="18px"> 2. Catálogo de Scripts: O que usar e quando?

| Script | Onde está | Quando usar? |
| :--- | :--- | :--- |
| **`gemini_lab.py`** | Raiz do projeto | **Documentos Isolados**: Para fazer perguntas rápidas ou testes únicos em um texto. |
| **`triagem_e_lapidacao.py`** | Raiz do projeto | **Produção em Massa**: Quando você tem dezenas de `.txt` na quarentena e quer filtrar e resenhar tudo de uma vez. |
| **`listar_modelos.py`** | Raiz do projeto | **Diagnóstico**: Se o Gemini parar de responder, use para ver quais modelos sua chave permite (atualmente usamos o `gemini-2.5-flash`). |

## <img src="../../../assets/icons/human_01_red.svg" width="18px"> 3. Extração de PDFs com Docling

O Docling é o seu "tradutor de hieróglifos". Ele entende que um PDF tem colunas e tabelas e limpa isso para a IA.

**Como ativar e usar:**
```bash
# O Docling geralmente está em um ambiente separado para não dar conflito
source ~/venv_docling/bin/activate

# Comando para converter um arquivo isolado:
docling "caminho/do/seu/arquivo.pdf" > "99_RESTRITO/02_TRIAGEM_BRUTA/nome_do_arquivo.txt"

# Comando para converter uma pasta inteira (Lote):
docling "99_RESTRITO/02_TRIAGEM_BRUTA/WA_MAM/Tecnoveg/" --output "99_RESTRITO/02_TRIAGEM_BRUTA/WA_MAM/Tecnoveg/Tecnoveg-markdown/"

# Ative o venv do docling
source ~/Documents/GitHub/UnB/Mulheres_Bioeconomia_Amazonia/venv_docling/bin/activate

# Converta para MD em vez de TXT
docling "99_RESTRITO/02_TRIAGEM_BRUTA/WA_MAM/Tecnoveg/ARG063-24 aderência pull-off.pdf" --to md > "99_RESTRITO/02_TRIAGEM_BRUTA/WA_MAM/Tecnoveg/Tecnoveg-markdown/LAUDO_ESTRUTURADO.md"
```

## <img src="../../../assets/icons/human_01_red.svg" width="18px"> 4. Prompts Específicos para Documentos Isolados

Ao usar o `python gemini_lab.py "$(cat arquivo.txt) --- [PROMPT]"`, use estes modelos:

### **A. Para Artigos Científicos (Bambu/PU/Pirolenhoso)**
> "Extraia os metadados (Autor, Ano, Título) e crie uma **tabela de propriedades físico-químicas**. Traduza o abstract e conecte o resultado com a viabilidade de implantação em cooperativas de mulheres na Amazônia Setentrional."

### **B. Para Relatórios de Máquinas (Ex: UNNI/Equipamentos)**
> "Analise a capacidade produtiva e liste os **gargalos de infraestrutura** (energia, peças, manutenção). Avalie a ergonomia para o trabalho feminino e sugira adaptações para o contexto da floresta."

### **C. Para Escritos das Mentoras (Sônia/Tania/Geórgia)**
> "Identifique os conceitos-chave de **Tecnologia Social ou Governança**. Transforme este texto em uma diretriz de campo para o projeto WTF, mantendo o tom pedagógico e ancestral."

## <img src="../../../assets/icons/human_01_red.svg" width="18px"> 5. Dicas de Produtividade com o Gemini CLI

1.  **Use o `>` para salvar**: Em vez de ler no terminal, salve direto:
    `python gemini_lab.py "..." > docs/analise_v1.md`
2.  **O "Double Check"**: Se uma tabela técnica parecer estranha, peça:
    `"Refaça a tabela acima focando apenas nas unidades de medida (SI) e valide os valores de densidade."`
3.  **Tradução Reversa**: Se estiver escrevendo um artigo para o consórcio em inglês, mande seu rascunho em português e peça:
    `"Traduza para inglês acadêmico (Nature/Science style) e mantenha os termos técnicos de bioeconomia."`

## <img src="../../../assets/icons/human_01_red.svg" width="18px"> O Próximo Passo
Notei que você tem **110 arquivos** na quarentena. O script `triagem_e_lapidacao.py` que corrigimos é a sua melhor ferramenta agora. 

**Deseja que eu prepare um comando do Docling que já direcione todos os PDFs da sua pasta de bibliografia direto para a quarentena, deixando o terreno pronto para o "Garimpo Digital"?** <img src="../../../assets/icons/human_01_red.svg" width="18px"><img src="../../../assets/icons/human_01_red.svg" width="18px">
### 1. Reativação do Ambiente (Sempre ao abrir o terminal)
Para que o Ravi reconheça o Python 3.12 e a biblioteca `google-genai` do projeto:

```bash
cd ~/Documents/GitHub/UnB/Mulheres-Tecem-Amazonia
source venv/bin/activate
export GOOGLE_API_KEY='SUA_CHAVE_AQUI'
```

### 2. O Prompt "Mestre" para Extração Técnica
Para o artigo de *Handroanthus chrysotrichus*, use este comando que combina **tradução**, **extração bibliográfica** e **tabelas de propriedades físicas**:

```bash
python gemini_lab.py "$(cat '01_GOVERNANCA/01_COLABORADORES/Bibliografia_Equipe/relacionadas/+DESMATAMENTO+E+SUSTENTABILIDADE+AMAZONIA.txt') --- 

Atue como Pesquisador Sênior em Engenharia Florestal e Bioeconomia. 

1. CABEÇALHO DO PROJETO:
projeto: Mulheres Que Tecem a Floresta
instituicao: Consórcio UnB/UFRR/UFAC
tipo: Pesquisa: Amazônia Setentrional (PES)
referencia: PES-TEC-007-2026
status: Ready

2. IDENTIFICAÇÃO BIBLIOGRÁFICA:
   Extraia: Autores, Ano, Título Original, Periódico e Local.

- <img src="../../../assets/icons/human_03_black.svg" width="18px"> name: Consórcio UnB/UFRR/UFAC
date: '2026-03-24'

3. TRADUÇÃO E SÍNTESE TÉCNICA:
   Traduza o resumo para português e explique a relevância da modificação térmica para a durabilidade da madeira juvenil.

4. EXTRAÇÃO DE DADOS (TABELA):
   Crie uma tabela Markdown com as principais Propriedades Físico-Mecânicas encontradas (Ex: Densidade, MOE, MOR) antes e depois da modificação térmica.

5. CONCLUSÃO PARA O PROJETO:
   Como esse estudo sobre Ipê-amarelo juvenil pode ser aplicado no manejo de espécies secundárias ou plantios de recuperação na Amazônia Setentrional?"
```

### 3. Modelos de Prompt para outras tarefas

| Objetivo | Prompt Modelo (Injetar no `gemini_lab.py`) |
| :--- | :--- |
| **Resumo Executivo** | `"Gere um resumo executivo de 5 pontos focando em viabilidade econômica deste arquivo: [TEXTO]"` |
| **Identificar Gargalos** | `"Analise este manual de máquinas e liste em uma tabela os requisitos de energia e possíveis pontos de falha na floresta: [TEXTO]"` |
| **Glossário Indígena** | `"Extraia todos os termos em línguas indígenas citados neste documento e crie um glossário com a tradução contextual para o português: [TEXTO]"` |

### <img src="../../../assets/icons/human_01_red.svg" width="18px">️ Dica de Ouro: O Arquivo `.zshrc`
Se você não quiser digitar o `export GOOGLE_API_KEY` toda vez, rode este comando uma única vez:
```bash
echo "export GOOGLE_API_KEY='AIzaSyDnUer8X3QiY0dJtK26xL9z8hGxbtm3R8A'" >> ~/.zshrc
source ~/.zshrc
```
## AUDIOS EM MASSA

import os
import time
from google import genai
from pathlib import Path

# 1. Configuração do Cliente
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
MODEL_ID = "models/gemini-1.5-flash" # Flash é excelente e rápido para áudio

# 2. Extensões de áudio suportadas
EXTENSOES_AUDIO = ('.mp3', '.wav', '.m4a', '.aac', '.ogg')

def transcrever_audio(caminho_audio, nome_arquivo):
    print(f"<img src="../../../assets/icons/human_01_red.svg" width="18px">️ Enviando para transcrição: {nome_arquivo}...")
    
    try:
        # Carrega o arquivo de áudio
        with open(caminho_audio, "rb") as f:
            audio_data = f.read()

        # Prompt para transcrição e nomeação inteligente
        prompt = """
        Atue como um transcritor especializado em bioeconomia e saberes ancestrais.
        1. Transcreva o áudio na íntegra.
        2. Ao final, sugira um NOME DE ARQUIVO curto e técnico baseado no assunto principal.
           Formato: 'ASSUNTO_RESUMIDO_ANO' (Ex: MANEJO_BAMBU_2026).
        3. Identifique os interlocutores se possível.
        """

        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[
                prompt,
                {"mime_type": "audio/mpeg", "data": audio_data} # Ajuste o mime_type se necessário
            ]
        )
        return response.text
    except Exception as e:
        return f"ERRO na transcrição: {e}"

def executar_transcricao_recursiva(diretorio_raiz):
    print(f"<img src="../../../assets/icons/human_01_red.svg" width="18px"> Iniciando varredura de áudios em: {diretorio_raiz}")
    
    for raiz, dirs, arquivos in os.walk(diretorio_raiz):
        # Ignora pastas de transcrição já criadas para não entrar em loop
        if "transcricao" in raiz:
            continue

        audio_files = [f for f in arquivos if f.lower().endswith(EXTENSOES_AUDIO)]
        
        if not audio_files:
            continue

        # Cria a subpasta 'transcricao' no diretório atual se houver áudios
        pasta_transcricao = Path(raiz) / "transcricao"
        pasta_transcricao.mkdir(exist_ok=True)

        for nome in audio_files:
            caminho_completo = Path(raiz) / nome
            
            resultado = transcrever_audio(caminho_completo, nome)
            
            # Tenta extrair o nome sugerido pela IA ou usa o original
            try:
                sugestao_nome = resultado.split("NOME DE ARQUIVO:")[1].strip().split('\n')[0]
                nome_limpo = "".join(x for x in sugestao_nome if x.isalnum() or x in "._- ")
                nome_saida = f"{nome_limpo}.txt"
            except:
                nome_saida = f"TRANSCRICAO_{nome.rsplit('.', 1)[0]}.txt"

            caminho_saida = pasta_transcricao / nome_saida
            
            with open(caminho_saida, 'w', encoding='utf-8') as f_out:
                f_out.write(resultado)
            
            print(f" Arquivado em: {caminho_saida}")
            time.sleep(2) # Pausa para estabilidade da API

if __name__ == "__main__":
    # Defina aqui a pasta onde estão as gravações das mentoras/entrevistas
    PASTA_AUDIOS = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/03_AUDIOS_BRUTOS"
    executar_transcricao_recursiva(PASTA_AUDIOS)

---

---

---

---

---

---

---
<p align="center"><img src="../../../assets/logo_BQTF/logo_mqtf_soberana.svg" width="40px"><br><b>Mulheres Que Tecem a Floresta — MQTF</b><br><i>"Soberania não se pede, se exerce."</i></p>