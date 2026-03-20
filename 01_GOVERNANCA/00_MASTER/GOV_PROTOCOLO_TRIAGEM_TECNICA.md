# Protocolo de Triagem Técnica e Sincronização de Ativos (v1.0)

Este protocolo define os critérios para catalogação, redação e intercomunicação de ativos de pesquisa e engenharia no Projeto **Mulheres Que Tecem a Floresta (WTF)**.

## 1. Nomenclatura e Tipologia de Ativos

Todo documento promovido da Triagem Bruta deve seguir a taxonomia institucional:

| Sigla | Categoria | Descrição |
| :--- | :--- | :--- |
| **MEM-TEC** | Memorando Técnico | Documento detalhado com a consolidação exaustiva de dados brutos e bibliografia. |
| **NT-ENG** | Nota Técnica | Documento de síntese para suporte à tomada de decisão ou anexo de projeto. |
| **GOV-DIR** | Diretriz de Governança | Regras operacionais, protocolos de higiene e normas internas. |

> [!IMPORTANT]
> Evite termos procedurais internos (como "Surgical Triage") nos metadados de arquivos oficiais.

## 2. Protocolo de "Sync-Link" (Sincronização Bibliográfica)

Para garantir a integridade do acervo, toda referência deve ser rastreável:

- **Links Absolutos**: Referências a arquivos locais devem usar o URI completo `file:///...`.
- **Ancoragem Bibliográfica**: Toda Nota Técnica deve citar explicitamente o Memorando Técnico de origem.
- **Catálogo de Ouro**: As referências externas (PDFs, Teses, Artigos) devem ser listadas com DOI ou link permanente na seção final de cada documento.

## 3. Critérios de Triagem "Cirúrgica"

1. **Preservação de Dados (SGMAS)**: Prioridade absoluta para coleta de dados básicos: **Populações**, **Coordenadas Geográficas**, **Estados/Municípios**, **Quantificações** e **Estatísticas**. Proibido resumir ou omitir métricas científicas.
2. **IA-Free (Higienização)**: Remoção de introduções redundantes, apologias a modelos de linguagem e boilerplate corporativo.
3. **Cruzamento de Fontes**: Sempre que possível, cruzar os dados brutos com o Memorial Técnico do Projeto e o "Custo Amazônia".

## 4. Estrutura Padrão do Memorando (MEM-TEC)

```markdown
---
projeto: Mulheres Que Tecem a Floresta (WTF)
instituicao: Consórcio UnB/UFAC/UFRR
tipo: Memorando Técnico
referencia: TAK-MEM-XXX-2026
status: CONSOLIDADO
---
# Título do Documento
## 1. Diagnóstico Detalhado ...
## 2. Metodologia e Dados ...
## 3. Implicações Orçamentárias (Custo Amazônia) ...
## 4. Sincronização e Bibliografia (Sync-Link) ...
```
