# Protocolo de Atuação — Plataforma Amazônia Regenerativa

Este agente deve seguir rigorosamente as "Regras de Ouro" definidas no `GOV_GEMINI.md`:

## 1. Princípios Técnicos
- Foco absoluto em **Bambu Nativo + PU Vegetal**.
- Proibição de CCA, CCB e tratamentos tóxicos.
- Soluções de baixo carbono (*low-carbon by design*).
- Uso do **Sistema Takwara** (não confundir com Sistema Ripper/Spin).
- **Citações Limpas**: Links internos devem ser formais: `[Nome](caminho.md)`.
- **Placeholder Zero**: Proibido deixar `XXXXXXX` em DOIs ou datas.
- **Início Direto**: Sem prefácios ou introduções "gentis" da IA no corpo do arquivo.

## 2. Segurança e Operação
- **NUNCA** comitar arquivos em `docs/99_RESTRITO/` ou pastas `_PRIVADO`.
- **docs/ Locking**: A pasta `docs/` é READ-ONLY para agentes. Edições são permitidas apenas para metadados (headers/badges) pré-commit.
- **Sombra Staging**: Todo o trabalho ativo ocorre em `01_SOMBRA_AUDITORIA/`. Arquivos lá devem ser categorizados (NT, Memorando, etc.).
- **Promoção em Lote**: A migração para `docs/` ocorre via `/sombra-sync` após auditoria humana.
- Diferenciar claramente **Parceria Institucional (UnB)** de **Propriedade Tecnológica (Fabio Takwara)**.

## 3. Regras Universais de Publicação e Commit (TODOS OS AGENTES)
- **Comprometimento Ético**: Agentes NUNCA realizam commits sem uma avaliação humana prévia baseada em report detalhado.
- **Projetos de Engenharia (`08_`)**: Devem ser compartilhados apenas memoriais jurídicos validados.
- **Zenodo Release**: Automatizar a criação do `.zip` após commit de release v2.0.

## 5. Identidade Visual & IA Generativa (Módulo E)
- **Estilo Dinâmico**: Perguntar sempre qual estilo (Realista CAD ou Sketched Warhol) via "nlm" para cada imagem.
- **Branding**: Imagens com pass-partout branco e assinatura "Takwara 2026" (canto inf. esq.).
