# MASTER_RULES — Governança Digital Takwara

Este documento é a autoridade suprema para a operação de agentes de IA na Plataforma Amazônia Regenerativa, resolvendo conflitos entre protocolos anteriores.

## 1. Regra de Ouro: Fluxo de Trabalho e Locking
- **Locking da Pasta `docs/`**: A pasta `docs/` é estritamente de **LEITURA** para agentes de IA para conteúdo de texto. 
    - *Exceção*: Atribuição de metadados de cabeçalho (YAML), rodapé, badges e versão é permitida quando identificado erro de conformidade pré-commit.
- **Shadow Staging**: Todo o trabalho de pesquisa, redação e revisão ocorre em `01_SOMBRA_AUDITORIA/`.
- **Batch Promotion**: A promoção de arquivos de `01_SOMBRA_AUDITORIA/` para `docs/` ocorre apenas em **Lote**, após auditoria humana.
- **Zenodo Release**: Após o commit de atualização de versão em `docs/`, o agente deve criar o arquivo `.zip` correspondente para o release Zenodo.

## 2. Padrão de Versionamento Diferenciado e Visibilidade
- **Versão de Publicação (Zenodo)**: Fixa em **v2.0 (Consolidada)**. Todos os arquivos promovidos para `docs/` devem portar o cabeçalho de versão 2.0.
- **Versão de Trabalho (Interna)**: **v2.2.2**. Arquivos em `01_SOMBRA_AUDITORIA/` indicam status de auditoria/catalogação.
- **Visibilidade**: Commits em `01_SOMBRA_AUDITORIA` são permitidos apenas para backup na raiz. O conteúdo da Sombra **NUNCA** deve aparecer no MkDocs, GitHub Pages ou `index.md` público (exceto após promoção para `docs/`).

## 3. Imutabilidade, Paridade e Auditoria de Lote
- **Corpo do Texto**: Imutável para blogs (`07_`) e documentos com DOI.
- **Metadados (Frontmatter)**: Edição autorizada apenas para paridade (Links, DOI, Tags v2.0).
- **Catalogação na Sombra**: Tudo o que entra em `01_SOMBRA_AUDITORIA` deve estar catalogado com tags e status definidos (Pesquisa, Rascunho, Complemento, Nota Técnica (NT), Memorando, Memorial Descritivo). 
- **Relacionamento de Ativos**: Cada arquivo na Sombra deve estar relacionado a um relatório, boletim ou memorando publicado (ou finalidade específica).
- **Comprometimento Ético**: Agentes **NUNCA** devem solicitar autorização de commit ao autor. Nada é commitado sem avaliação humana prévia e report detalhado.

## 4. Identidade Visual (Módulo E)
- **Material Técnico/Memoriais**: Imagens realistas (CAD).
- **Cartilhas/Didáticos**: Versão ilustrada (Sketched/Henfil/Warhol).
- **Procedimento**: O agente deve **SEMPRE** perguntar qual estilo utilizar para cada imagem solicitada via integração "nlm".
- **Moldura**: Pass-partout branco e assinatura **Takwara 2026** (canto inferior esquerdo).

## 5. Regras de Segurança e Mentoria (Firewall)
- **Protocolo de Triage e Gestão Compartilhada**: 
    - **Prof. Tania** (Mentoria Global): Validação de Soberania e Estratégia.
    - **Prof. Sônia** (Açaí-Castanhas): Autoridade técnica em Bioeconomia de base florestal.
    - **Prof. Geórgia** (Artesanato): Guardiã da Identidade Visual e Design Social.
    - **Prof. Vanessa** (Financeiro/Auditoria): Controle de paridade e transparência fiscal.
- **Alerta de Mentoria**: É proibido ignorar ou desconsiderar solicitações de **Mentoria de Gestão**. Se detectado, o Agente deve emitir um alerta crítico ao Operador.
- **Segurança**: Dados da pasta `99_RESTRITO/` não podem ser citados em documentos públicos.
- **Commit**: Restrito a Biblioteconomia ou Humano após report detalhado.
