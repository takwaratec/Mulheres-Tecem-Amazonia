---
description: Workflow de Integração NotebookLM (nlm) para produção de mídia e estudo profundo.
---

# Workflow: /nlm (NotebookLM Integration)

Este workflow orquestra a preparação de ativos do repositório para processamento pelo **NotebookLM**, permitindo a criação de podcasts, roteiros e sessões de estudo profundo.

## Comandos Operacionais

### 1. Preparar Fontes (/nlm --prepare)
O Agente varre os documentos selecionados e gera arquivos de "Contexto Limpo" na pasta `99_RESTRITO/03_COMUNICACAO/nlm_sources`, removendo metadados YAML excessivos e links quebrados para otimizar o processamento da IA.

### 2. Gerar Roteiro de Áudio (/nlm --script)
Com base em um documento técnico, o Agente gera um roteiro de "Deep Dive" ou "FAQ" no padrão @takwaratec, pronto para alimentar o gerador de Audio Overview do NotebookLM.

### 3. Sincronizar Resultados (/nlm --sync)
Após o uso do CLI `nlm` externo pelo usuário, o Agente ajuda a documentar o link do "Notebook" gerado e os principais insights no repositório.

### 4. Transcrever Mídia (/nlm --transcribe)
O Agente orquestra o uso do OpenAI Whisper para transcrever áudios baixados do NotebookLM. Os arquivos resultantes (.txt) são movidos para `docs/03_COMUNICACAO_MIDIA/transcrições/` para curadoria.

## Regras de Ouro
- **Soberania do Conteúdo**: Toda exportação deve manter a citação ao DOI Master.
- **Higiene Visual**: Sugerir descrições de imagens no estilo Henfil/Warhol para acompanhar os resumos.
- **Protocolo de Voz**: O tom deve ser vibrante mas rigoroso, evitando o "vazio de marketing" corporativo.

// turbo
## Automação
Se o usuário confirmar o uso do CLI `nlm` local, o Agente pode preparar o comando de execução:
`nlm notebook create --name "DeepDive: [TITULO]" --sources [CAMINHO_FONTES]`
