# Cartilha do Operador: Projeto Mulheres Que Tecem a Floresta (Mulheres que Tecem a Floresta)

Bem-vindo à dinâmica operacional do Consórcio UnB/UFAC/UFRR. Este guia orienta a gestão de ativos digitais, triagem de materiais e protocolos de publicação sob o **Protocolo Institucional v1.0**.

## 1. Fluxo de Triagem de Materiais Brutos

Sempre que receber novos arquivos (PDFs técnicos, Planilhas BNDES ou Históricos de WhatsApp), siga esta rotina:

1.  **Entrada**: Mova os arquivos brutos para a pasta `99_RESTRITO/02_TRIAGEM_BRUTA/`.
2.  **Comando**: No chat com o agente, digite `/triage`.
    - Use `/triage --robust` para PDFs com tabelas e layouts complexos.
3.  **Processamento**: O agente irá extrair o texto, categorizar e gerar um rascunho em Markdown.
4.  **Saída**: Os arquivos formatados para revisão cairão em:
    - **Dossiês/Artigos**: `01_GOVERNANCA/04_PARECERES_E_RELATORIOS/`
    - **Dados/P&D**: `04_PESQUISA_ANDAMENTO/`

## 2. Estrutura de Diretórios (Sombra vs. Docs)

O repositório opera em dois níveis de visibilidade:

- **04_PESQUISA_ANDAMENTO (Curadoria Ativa/R&D)**:
    - Onde o trabalho é iterativo e rascunhos são gerados.
    - Contém os arquivos `WTF_` e `ENG_` em fase de auditoria.
- **01_GOVERNANCA & 02_TECNICO (Produção Final)**:
    - Onde os arquivos são consolidados após revisão humana.
    - Sincronizado com o Zenodo e anexo ao BNDES Model-01.

## 3. Identidade Visual e Fotografia (Protocolo PVIT)

Ao solicitar a geração de imagens via `/imagem`, especifique o modo:

- **Modo Sebastião Salgado**: Para projeções futuristas e impacto social (P&B, grão pesado, foco em texturas).
- **Modo Henfil/Warhol**: Para cartilhas didáticas, manuais de montagem e esquemas simplificados (Cores vibrantes, pedagógico).
- **Modo CAD**: Para plantas baixas e memoriais de equipamentos (Engenharia pura).

## 4. Catalogação e Citação

Todos os arquivos do projeto devem portar o prefixo `WTF_`.

### Badges de Cabeçalho (Automáticos)
- `Projeto: Mulheres Que Tecem a Floresta`
- `Consórcio: UnB-UFAC-UFRR`

### Citação Obrigatória
> "Coordenação Técnica; CRUZ, T.; [SOBRENOME], S.; [SOBRENOME], G.; [SOBRENOME], V. [et al.]. **Mulheres Que Tecem a Floresta**. v1.0. 2026. Protocolo Institucional."

## 5. Backups e Sincronia
- Arquivos em `docs/` são espelhos dos backups Zenodo.
- Nunca delete arquivos da Sombra sem garantir que a versão final já foi promovida para `docs/`.
