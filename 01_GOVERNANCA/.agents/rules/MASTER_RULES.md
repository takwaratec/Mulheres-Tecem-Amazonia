# MASTER_RULES — Governança Institucional Mulheres Que Tecem a Floresta

Este documento é a autoridade suprema para a operação de agentes de IA no Projeto Mulheres Que Tecem a Floresta, resolvendo conflitos entre protocolos anteriores.

## 1. Regra de Ouro: Fluxo de Trabalho e Locking
- **Locking da Produção Concluída**: Arquivos nas pastas `01`, `02`, `03` e `05` são estritamente de **LEITURA** para agentes de IA para conteúdo de texto após consolidados. 
    - *Exceção*: Atribuição de metadados de cabeçalho (YAML), rodapé, badges e versão é permitida.
- **Shadow Staging**: Todo o trabalho de pesquisa, redação e revisão ocorre em `04_PESQUISA_ANDAMENTO/`.
- **Batch Promotion**: A promoção de arquivos de `04_PESQUISA_ANDAMENTO/` para as pastas de governança ou técnica ocorre apenas em **Lote**, após auditoria humana.
- **Zenodo Release**: Após a consolidação, o agente deve auxiliar na preparação do pacote para o release Zenodo institucional.

## 2. Padrão de Versionamento e Visibilidade
- **Versão Institucional**: **v1.0 (WTF)**.
- **Versão de Trabalho**: Arquivos em `04_PESQUISA_ANDAMENTO/` indicam status de curadoria/catalogação.
- **Visibilidade**: Conteúdos em `01_GOVERNANCA` e `02_TECNICO` são a base institucional. A pasta `99_RESTRITO` jamais deve ser exposta.

## 3. Imutabilidade e Auditoria
- **Imutabilidade Corpo do Texto**: Imutável para artigos consolidados e documentos com DOI.
- **Metadados (Frontmatter)**: Edição autorizada para paridade de links e tags.
- **Catalogação**: Tudo o que entra em `04_PESQUISA_ANDAMENTO` deve estar catalogado com tags e status definidos (Pesquisa, Rascunho, Nota Técnica, Memorando, Memorial Descritivo). 
- **Comprometimento Ético**: Nada é consolidado sem avaliação humana prévia e report detalhado.

## 4. Identidade Visual (Módulo E)
- **Material Técnico/Memoriais**: Imagens realistas (CAD ou Salgado P&B).
- **Cartilhas/Didáticos**: Versão ilustrada (Henfil/Warhol).
- **Moldura**: Pass-partout branco e assinatura **Projeto WTF 2026** (canto inferior esquerdo).

## 5. Regras de Segurança e Mentoria
- **Consórcio UnB/UFAC/UFRR**:
    - **Mentoria Global**: Validação de Soberania e Estratégia.
    - **Bioeconomia de Base Florestal**: Autoridade técnica em Castanha, Açaí e Artesanato.
    - **Financeiro/Auditoria**: Controle de paridade BNDES Model-01.
- **Segurança**: Dados da pasta `99_RESTRITO/` não podem ser citados em documentos públicos.
- **Regra Temporal (Incorruptível)**: O projeto opera no cenário **Pós-COP30** (2026+). Todas as metas descritas como "futuro para a COP30" devem ser tratadas como legados ou marcos já superados. O foco atual é a consolidação e escala dos resultados.
