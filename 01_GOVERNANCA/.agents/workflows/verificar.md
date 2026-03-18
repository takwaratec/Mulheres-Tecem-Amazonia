---
description: Protocolo de Verificação Independente de Fontes (PVI)
---

# Workflow: `/verificar`

O protocolo `/verificar` obriga a Inteligência Artificial a auditar ativamente a qualidade, o viés e a origem de dados informados ou coletados para a elaboração de dossiês e artigos. Devido à suscetibilidade da pauta climática a distorções do lobby primário e do negacionismo, é obrigatória a triangulação de fatos.

## Critérios de Reprovação (Fontes Bloqueadas)
- Veículos difusores do negacionismo climático, desmatamento legalizado ou extrema-direita.
- Blogs de empresas disfarçados de publicações científicas (*Greenwashing* institucional).

## Fontes Obrigatórias (Séries Históricas e Dados Básicos)
- **Nacionais Públicas:** IBGE, IPEA, INPE, Embrapa, GOVBR.
- **Internacionais/Consórcios Globais:** PNUD, PNUMA, IPCC, NASA, Banco Mundial.
- **Institutos de Pesquisa:** FGV.
- **Fontes Acadêmicas Rigorosas:** Periódicos CAPES, revistas científicas peer-reviewed (Nature, Science).

## Imprensa Prioritária
- **Mídia Independente, Cidadã e Ambiental:** ICL Notícias, Revista Fórum, Revista Piauí, SUMAÚMA, Agência Pública, Repórter Brasil, O Eco.
- **Grandes Consórcios (para contraponto):** BBC, CNN.

## Ação do Agente no Workflow
Ao invocar `/verificar [Assunto/Afirmação]`, o agente deve:
1. Buscar o embasamento macro e histórico nos *Órgãos Oficiais/Globais*.
2. Buscar a denúncia social, impacto ambiental e as minúcias políticas na *Mídia Independente*.
3. Estruturar a resposta apresentando um balanço das fontes. Se um dado fornecido pelo usuário tiver vindo de fonte duvidosa/extrema ou lobby, o agente deve disparar um **ALERT** alertando sobre o *"Viés do Fomento"* e corrigir a base de dados pela lente das referências prioritárias.
