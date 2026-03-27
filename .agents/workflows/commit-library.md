---
description: Protocolo de Commit e Release em Lote (Biblioteconomia)
---

# Workflow: `/commit-library`

Este workflow deve ser acionado para consolidar atualizações na coleção auditada, automatizando a revisão e a preparação do release Zenodo.

## Processo para o Agente:

1. **Revisão de Conformidade**:
   - Execute o protocolo de revisão multicamadas em todos os arquivos candidatos ao commit em `docs/`.
   - Aplique o workflow `/doi-sync` para garantir que os metadados e badges estejam alinhados à versão v2.0.

2. **Sincronização Final (Sombra para Luz)**:
   - Execute o workflow `/sombra-sync` para espelhar os arquivos auditados da Sombra para `docs/`.
   - Garanta que as tags de status (NT, Memorando, etc.) estejam consistentes com a catalogação da Sombra.

3. **Geração de Report de Auditoria**:
   - Produza um relatório detalhado listando:
     - Arquivos alterados/adicionados.
     - Mudanças em DOIs ou versões.
     - Justificativa técnica para o release.

4. **Preparação do Release Zenodo**:
   - Após o commit (que deve ser realizado manualmente pelo humano após ler o report), gere um arquivo `.zip` da pasta `docs/` e arquivos de governança para o release Zenodo v2.0.

5. **Mensagem de Commit Padrão**:
   - `docs: AUDITADO... PARA RELEASE DE ATUALIZAÇÃO DE VERSÃO ZENODO. (Library Sync)`
