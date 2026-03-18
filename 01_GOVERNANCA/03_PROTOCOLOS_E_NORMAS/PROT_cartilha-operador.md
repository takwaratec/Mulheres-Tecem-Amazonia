# Cartilha do Operador: Projeto Mulheres Que Tecem a Floresta (Mulheres que Tecem a Floresta)

Bem-vindo à dinâmica operacional do Consórcio UnB/UFAC/UFRR. Este guia orienta a gestão de ativos digitais, triagem de materiais e protocolos de publicação sob a arquitetura **PAR 5.1**.

## 1. Fluxo de Triagem de Materiais Brutos

Sempre que receber novos arquivos (PDFs técnicos, Planilhas BNDES ou Históricos de WhatsApp), siga esta rotina:

1.  **Entrada**: Mova os arquivos brutos para a pasta `99_RESTRITO/02_TRIAGEM_BRUTA/`.
2.  **Comando**: No chat com o agente, digite `/triage`.
    - Use `/triage --robust` para PDFs com tabelas e layouts complexos.
3.  **Processamento**: O agente irá extrair o texto, categorizar e gerar um rascunho em Markdown.
4.  **Saída**: Os arquivos formatados para revisão cairão em:
    - **Governança/WhatsApp**: `01_SOMBRA_AUDITORIA/04_PROJETO_WTF/01_GOVERNANCA/`
    - **Técnico/PDFs**: `01_SOMBRA_AUDITORIA/04_PROJETO_WTF/02_TECNICO/`

## 2. Estrutura de Diretórios (Sombra vs. Docs)

O repositório opera em dois níveis de visibilidade:

- **01_SOMBRA_AUDITORIA (Pesquisa Ativa/R&D)**:
    - Onde o trabalho é "sujo" e iterativo.
    - Contém os arquivos `WTF_` em fase de rascunho ou auditoria.
    - **NÃO FICA VISÍVEL NO SITE PÚBLICO.**
- **docs/ (Lançamento/Release)**:
    - Onde os arquivos são "promovidos" após revisão humana.
    - Sincronizado com o MkDocs e Zenodo.
    - **É A VERDADE PÚBLICA DO PROJETO.**

## 3. Identidade Visual e Fotografia (Protocolo PVIT)

Ao solicitar a geração de imagens via `/imagem`, especifique o modo:

- **Modo Sebastião Salgado**: Para projeções futuristas e impacto social (P&B, grão pesado, foco em texturas).
- **Modo Henfil/Warhol**: Para cartilhas didáticas, manuais de montagem e esquemas simplificados (Cores vibrantes, pedagógico).
- **Modo CAD**: Para plantas baixas e memoriais de equipamentos (Engenharia pura).

## 4. Catalogação e Citação

Todos os arquivos do projeto devem portar o prefixo `WTF_`.

### Badges de Cabeçalho (Automáticos)
- `Projeto: Mulheres que Tecem a Floresta`
- `Powered by PAR 5.1`
- `Consórcio: UnB-UFAC-UFRR`

### Citação Obrigatória
> "Institucional, F.; CRUZ, T.; [SOBRENOME], S.; [SOBRENOME], G.; [SOBRENOME], V. [et al.]. **Mulheres Que Tecem a Floresta**. v1.0. 2026. Baseado na arquitetura técnica PAR 5.1."

## 5. Backups e Sincronia
- Arquivos em `docs/` são espelhos dos backups Zenodo.
- Nunca delete arquivos da Sombra sem garantir que a versão final já foi promovida para `docs/`.
