---
description: Protocolo Editorial para Relatórios de Denúncia e Advocacy
---

Este workflow deve ser utilizado exclusivamente para o processamento de relatórios de denúncia e materiais de alto impacto para Advocacy (ex: COP30).

### Instruções de Execução:

1. **Protocolo de Âncoras (Módulo D)**:
   - Converta TODAS as citações `[^n]` para o padrão inline: `[(Fonte, Ano)](URL)`.
   - Remova a lista de notas de rodapé ao final do documento.

2. **Garantia de Endpoints Precisos**:
   - Valide se os links apontam para o documento final (ex: PDF da Lei, Ata da Câmara), não para páginas genéricas.
   - Adicione metadados de "Data de Acesso" se necessário na bibliografia consolidada.

3. **Rigor Técnico e Isenção**:
   - Elimine qualquer tom qualitativo gerado por IA que não esteja embasado em fatos.
   - Recorra ao `GEMINI.md` Módulo A para validar os termos técnicos (Bambu Nativo, PU Vegetal).

4. **Sincronização**:
   - Certifique-se de que as melhorias estruturais sejam aplicadas simultaneamente às versões em Inglês e Espanhol.

5. **Atualização do BD de Denúncia (Módulo F)**:
   - Após a conclusão do relatório, atualize obrigatoriamente o [BD_denuncias-advocacy.md](../../Arquivo%20Takwara/04_ADVOCACY_POLITICA/BD_denuncias-advocacy.md).
   - Realize o **Protocolo de Verificação de Inércia (V.I.)**: valide se houveram mudanças de status em órgãos governamentais ou tribunais antes de consolidar a nova evidência.

// turbo
**Comando Sugerido**: "/denúncia [arquivo]" - Aplica o rigor total, formatação de âncoras e sincronização com o Banco de Dados de Advocacy.
