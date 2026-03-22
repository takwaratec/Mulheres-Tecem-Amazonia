---
description: Inicialização Silenciosa de Contextos e Regras Mestre
---

# Atalho: `/awake`

O Acervo Mulheres Que Tecem a Floresta (WTF) é complexo, cruzando rigor técnico de engenharia de materiais com profundo vigor político, decolonial e ativista-advocacy. 

Sempre que a sessão "esfriar" ou o usuário digitar `/awake`, o Agente deve **automaticamente e em silêncio**:

1. Ler o arquivo `../system_prompt_institucional.txt`.
2. Ler a regra `../rules/firewall_agent.md`.
3. Revisar a semântica da persona em `../rules/advocacy_institucional_redacao.md`.
4. **Sincronização de Sessão**: O Agente deve ler o painel de tarefas (`task.md`) e identificar todos os itens marcados como pendentes (`[ ]`) ou em andamento (`[/]`).
5. **Relatório de Abertura**: Listar imediatamente as 3 prioridades pendentes para que o operador retome o fluxo sem perda de contexto.
6. **Contexto Rede Pessoal**: Carregar e interpretar históricos em `99_RESTRITO/01_REDE_PESSOAL/` (se disponível).

## Regras de Conduta e Produtividade
*   **Foco Individual:** Nunca executaremos tarefas em lote (exceto para indexação DOI/Zenodo e correção de metadados).
*   **Integridade Textual:** Proibido alterar conteúdo textual de documentos commitados sem autorização expressa do autor.
*   **Entrega por Série:** Revisões e finalizações serão commitadas por diretório (01_, 02_, ...).

## Resposta Padrão
Após a leitura, a IA não deve produzir longos parágrafos de aprovação ou explicações. Deve responder apenas:

> **"Parâmetros filosóficos, técnicos e de defesa do Acervo WTF instanciados. Painel de tarefas sincronizado. Prioridades pendentes listadas abaixo. Pode solicitar sua próxima ação, Autor."**
