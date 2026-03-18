# Workflow: "DA SOMBRA PARA A LUZ"

Este workflow gerencia a transição segura de documentos auditados da Sombra (`01_SOMBRA_AUDITORIA/`) para a "Luz" (Pasta `docs/`), garantindo a integridade dos DOIs e a paridade da versão v2.0 para o release Zenodo.

## Regras de Integridade:
- **Base de Conhecimento**: A pasta `01_SOMBRA_AUDITORIA/` contém toda a base de conhecimento técnica. **NUNCA** apague arquivos na Sombra, mesmo que não existam em `docs/`.
- **Coleção Auditada**: A pasta `docs/` contém apenas a coleção auditada e publicada.
- **Isolamento de Menu**: Arquivos em `01_SOMBRA_AUDITORIA/` não devem ser incluídos em menus do MkDocs ou GitHub Pages.

## Processo para o Agente:

1. **Auditoria de Prontidão**:
   - Verifique se os arquivos na Sombra possuem status "Auditado". O conteúdo deve seguir rigorosamente o padrão **Advocacy 5.1**.

2. **Preparação para Publicação**:
   - Mude a versão no frontmatter de `2.2.2` para `2.0`.
   - Certifique-se de que los links relativos apontam para a estrutura final em `docs/`.
   - Garanta que as badges de DOI estão apontando para o Master DOI da Coleção.

3. **Deploy em Lote**:
   - Copie (NUNCA mova/apague da origem) os arquivos da Sombra para as respectivas pastas em `docs/`.

4. **Indexação e MkDocs**:
   - Atualize `mkdocs.yml` apenas com o que foi promovido para `docs/`.
   - Atualize o `index.md` de `docs/` com badges e tags v2.0.

5. **Relatório e Pré-Commit**:
   - Gere um report detalhado das alterações para auditoria humana.
   - O commit (realizado apenas após validação) terá a mensagem: `docs: AUDITADO... PARA RELEASE DE ATUALIZAÇÃO DE VERSÃO ZENODO. (Shadow-to-Luz)`.
