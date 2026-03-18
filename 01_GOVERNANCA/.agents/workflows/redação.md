---
description: Protocolo de Redação Técnica e Profissional (IA-Free)
---

Este workflow deve ser acionado sempre que o usuário solicitar a criação ou edição de um artigo, nota técnica ou manual oficial.

### Instruções para o Agente:

1. **Consulta ao Módulo D e Skills**: Leia as regras de documentação profissional no `Protocolo GEMINI` e a **Skill** específica do diretório em `.agents/skills/`.
2. **Padrão Advocacy 5.1**: Aplique rigorosamente as regras em `.agents/rules/advocacy_5_1_redacao.md`.
3. **Higiene de Ativos**:
    - Remova referências a IAs (Perplexity, Gemini, etc.).
    - Elimine âncoras de busca `[^n]` e links soltos.
4. **Escrita Humana**: Comece o conteúdo diretamente, sem introduções robóticas.
5. **Links e Técnica**: Use links internos padrão e garanta que conceitos (Bambu Nativo, Sistema Takwara) sigam a Skill de Tecnologia e o `GEMINI.md`.

// turbo
**Comando Sugerido**: "Aplique o protocolo de redação técnica e Advocacy 5.1 ao arquivo [caminho] focando em [tema]."
