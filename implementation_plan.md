# Plano de Consolidação e Refinamento de Ativos de Engenharia (T01-T10)

Este plano visa a organização exaustiva de todo o material intelectual produzido para as dez invenções (T01-T10), centralizando memoriais, BoMs, diagramas e prompts de geração em diretórios específicos, garantindo que "nenhuma vírgula" do material original seja perdida.

## User Review Required

> [!IMPORTANT]
> A organização proposta move arquivos de diretórios compartilhados (`FLUXO_TECNICO`, `BOLETIM_TECNICO`) para subdiretórios específicos por invenção. Isso mudará a estrutura de caminhos para referências internas.

---

## Proposed Changes

### [Infraestrutura de Invenções]

#### [NEW] [Diretório Mestre](file:///Users/fabiotakwara/Documents/GitHub/UnB/Mulheres-Tecem-Amazonia/04_GESTAO_OPERACIONAL/01_FLUXO_TECNICO/INVENCOES/)
Criação de subdiretórios dedicados para cada ativo de engenharia:
- `T01_FORNO_ECOLOGICO/`
- `T02_REATOR_BIORREFINARIA/`
- `T03_RESINADOR_ROTATIVO/`
- `T04_MISTURADOR_BIOCOMPOSITOS/`
- `T05_PRENSA_CASSETES/`
- `T06_GABARITOS_SOLDA/`
- `T07_PRENSA_SANDUICHE/`
- `T08_TAMBOREADOR/`
- `T10_BALSA_CATAMARA/`

### [Sincronização de Dados e Memoriais]

#### [MOVE/LINK] [Consolidação de Ativos](file:///Users/fabiotakwara/Documents/GitHub/UnB/Mulheres-Tecem-Amazonia/04_GESTAO_OPERACIONAL/01_FLUXO_TECNICO/)
1. **T02 (Reator)**: Mover `aspen-data-sheet-T02.md`, `diagrama-T02-plano2.md` e `TAK-NT-T02-01` para o subdiretório `T02_REATOR_BIORREFINARIA/`.
2. **T10 (Balsa)**: Agrupar `TAK-BOM-T10_DETALHADO.md`, `TAK-MD-010_MEMORIAL-DESCRITIVO-BALSA.md` e `TAK-MEM-T10_BALSA-CATAMARA-VAPOR.md` em `T10_BALSA_CATAMARA/`.
3. **Outros**: Repetir para T01-T08 conforme mapeamento.

### [Preservação de Prompts e Lógica de Geração]

#### [NEW] [Inclusion of Prompts](file:///Users/fabiotakwara/Documents/GitHub/UnB/Mulheres-Tecem-Amazonia/04_GESTAO_OPERACIONAL/01_FLUXO_TECNICO/INVENCOES/)
- Criação de arquivos `PROMPT_DESCRICAO_DETALHADA.md` em cada pasta, contendo os prompts originais de geração utilizados para consolidar o material intelectual (evitando "perda de vírgulas").

---

## Verification Plan

### Automated Tests
- Verificação de links quebrados após a movimentação de arquivos.
- Busca global (grep) para garantir que referências a "T09" foram totalmente migradas para "T10".

### Manual Verification
- Solicitar ao usuário a validação da nova estrutura organizacional no VS Code Explorer.
