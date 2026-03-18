---
description: Varre o repositório em busca de link-rot nas evidências de denúncia
---

# Workflow: `/audit-links`

Como a Plataforma monitora ativamente FDDs, ONGs de fachada e fundos públicos que costumam promover greenwashing e desinformação legal (como no PL 6.289/2019 e a manobra da COP30), os URLs citados em dossiês e artigos frequentemente saem do ar. O `audit-links` automatiza a caçada a links quebrados antes que o acervo sofra perdas probatórias.

## Instrução para o Agente:

1. **Scripts Nativos:** Crie (na primeira execução) ou execute um script Python na infraestrutura que leia todos os arquivos `.md` das pastas `01` até `07` e `99`.
2. **Scraper de URLs:** O script deve fazer um web request `GET` ou `HEAD` (usando cabeçalhos `User-Agent` regulares) em cima de todos as URLs externas (iniciadas em `http`).
3. **Tabelando Falhas:** Mapeie todo link que retornar *Status Code* `404` (Não encontrado), `403` (Proibido) ou que lançar `ConnectionError`.
4. **Relatório Restrito:** Grave o resultado consolidado no arquivo restrito `docs/99_RESTRITO/REPORTE_LINKS_QUEBRADOS.md`. O formato deve ser em tabela `[Arquivo Afetado] | [URL Quebrada] | [Status Code]`.
5. **Alternativa *Wayback*:** Opcionalmente (se o script permitir), para os links retornando erro, o script deve invocar uma busca na API aberta da *Wayback Machine* (Internet Archive) e sugerir no relatório o link perene (salvo no tempo).

**Comando final do Agente:** Ao término, notifique o autor para acessar a pasta `99` e aprovar as substituições.
