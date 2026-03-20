# Resumo da Sessão: Revisões e Adaptações para a Versão 2.0
**Data:** Março de 2026
**Responsável Operacional:** IA Takwara (Antigravity)
**Diretrizes:** Protocolo Advocacy WTF e "Freio de Agentes"

## 1. Tratamento e Isolamento de Imagens
- Identificamos imagens soltas no acervo de auditoria (ex: diagramas de sistema flexível de montagem, renderizações do Domo Voador, peças P&B padrão Sebastião Salgado).
- Criamos o diretório `01_SOMBRA_AUDITORIA/10_IMAGENS_IA/isoladas`.
- Transferimos as imagens isoladas com o objetivo de deixar a documentação puramente textual e auditar o workflow de imagens separadamente.

## 2. Padrões Visuais (PVIT)
- **Atualização do Regimento Audiovisual (`GOV_regimento-pvit-audiovisual.md`)**:
  - Ajustamos todas as exigências de Landscape (Close-ups e Fotografia) da proporção antiga (15x21) para a nova **proporção 4:3**.
  - Solidificamos as exigências estéticas: "Sebastião Salgado" para fotos críticas de operação e "Henfil" para ilustrações e esquemas pedagógicos.
  - O formato 4:3 substitui o obsoleto padrão de 15:21 em toda a coleção para garantir enquadramento técnico alinhado com relatórios impressos e dispositivos móveis.

## 3. Arquitetura Modular e "Soberania Zero Cimento"
- **Atualizações de Engenharia (`GOV_checklist-detalhes-finos.md`)**:
  - Banimento formalizado do uso de tijolos convencionais e alvenaria cimentícia.
  - Implementação obrigatória da estrutura de "**Domo Voador**" com telhado íngreme, culminando na montagem prioritária de um **Lanternim** (chaminé térmica para resfriamento passivo).
  - Vedações PU: Injeção de PU Expansivo nos miolos das Colunas (agrupadas em 4 varas/Guadua) que formam os **Trilhos Orientadores**, ocultando os fechamentos laterais e dando acabamento estético em que apenas o colmo de bambu e a parede arenosa ficam visíveis.
  - Iluminação PET: Garrafas encravadas verticalmente no galpão, com bico para fora, sempre em arranjos esparsos horizontais.

## 4. Biblioteca de Referências (Protocolo WTF)
- **Sincronizador de Referências (`extract_refs.py`)**: 
  - Desenvolvemos um script que varreu todos os `.md` da base pública `docs/`, capturou as tags de referência bibliográfica nas notas de rodapé de cada texto técnico e converteu a massa de dados num consolidado no Dossiê Estratégico.
  - A unificação habitou a Seção 5.2 do arquivo `BD_referencias-acervo.md`.
- **Dicionário e Advocacy**:
  - Criamos o *Glossário Oficial de Siglas* (`GOV_glossario-siglas.md`). Expandimos isso em versões localizadas (`_en.md`, `_es.md`).
  - Adicionamos emblemas visuais traduzidos e selos DOI.

## 5. Dossiê Fundo Amazônia / BNDES (Sigilo e Padronização)
- Verificamos os descuidos crônicos de atribuição técnica, removendo auto-atribuições não previstas no script (autoria indevida da IA sobre a auditoria do dossiê).
- Corrigimos os caminhos dos *badges* das opções pt/en/es via script Python local (`fix_badges_bndes.py`), validando conformidade estrita (Master DOI Shields.io, Licença CC BY 4.0, Navegação Interligada e Status Ativo/Active).
- **Proteção Contra Vazamentos**: Como a pasta `docs/09_DOSSIE_BNDES` (e a `01_SOMBRA_AUDITORIA/`) comporta as finanças e o mapeamento submetido ao BNDES, a tratamos com **máximo sigilo**.
    - Foram desindexadas da árvore de Commits via comando `git rm -r --cached`.
    - Criptografadas sob monitoramento da lista de restrições do `.gitignore`.
    - Os atalhos, blocos descritivos e *nav* do `mkdocs.yml`, `index.md`, `index_en.md` e `index_es.md` contendo referências diretas a essa seção foram isolados e purgados, garantindo o anonimato digital do Dossiê na Web.
- **Temos garantido que arquivos .md de auditoria jamais sejam empurrados publicamente de maneira inconsequente.**

## 6. Governança Final da Versão 2.0
- Ajustamos toda a sinalética de relatórios legados e `mkdocs.yml` para a insígnia oficial e consolidada de `v2.0` (abandonando o *branch* transitório v2.2.2 criado no *checkout* Zenodo anterior).
- Todo o trânsito da sessão obedeceu ao protocolo "Freio de Agentes", garantindo as alterações na rede *staging* (add docs) sem comitar prematuramente antes do aval definitivo da Coordenação de Governança [Workflow *commit-library*].
