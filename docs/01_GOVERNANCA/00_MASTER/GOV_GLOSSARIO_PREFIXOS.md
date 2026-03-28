---
projeto: Mulheres Que Tecem a Floresta
instituicao: Consórcio UnB/UFRR/UFAC
tipo: Governança e Estratégia
referencia: GOV_GLOSSARIO_PREFIXOS
status: Status Ready
author:
- name: Consórcio UnB/UFRR/UFAC
date: '2026-03-26'
---

![Status: Consolidado](https://img.shields.io/badge/Status-Consolidado-brightgreen)

<p align="right"><i>"O real não está na saída nem na chegada: ele se dispõe para a gente é no meio da travessia."<br>— Guimarães Rosa</i></p>

### <img src="../../../../assets/patterns/square_05_red.svg" width="22px"> Ficha Técnica e Metadados
*   **Projeto**: Mulheres Que Tecem a Floresta (MQTF)
*   **Instituição**: Consórcio UnB / UFRR / UFAC
*   **Referência**: GOV_GLOSSARIO_PREFIXOS.md
*   **Status**: Status Consolidado
*   **Autor**: Consórcio UnB / UFRR / UFAC
*   **Data**: 27 de Março de 2026

# Glossário de Prefixos e Protocolo de Status (Mulheres que Tecem a Floresta)

Este documento define a taxonomia oficial para a organização do acervo técnico e documental do projeto.

## 1. Prefixos de Diretoria e Gestão (GOV/BUDGET)

| Prefixo | Nome | Descrição |
| :--- | :--- | :--- |
| **GOV-MEM** | Memorando de Gestão | Documentos âncora de estratégia institucional e orçamentária. |
| **GOV-DIR** | Diretriz de Governança | Normas operacionais, protocolos de ética e regras de colaboração. |
| **BUDGET** | Orçamento e Logística | Relatórios financeiros, tranches e alocação de recursos. |

## 2. Prefixos de Pesquisa e Engenharia (PES/ENG/BIO)

| Prefixo | Categoria | Descrição / Especialidades |
| :--- | :--- | :--- |
| **PES** | Pesquisa Geral | Levantamentos, revisões bibliográficas e estudos de base. |
| **PES-BB** | Pesquisa: Bambu | Estudos específicos sobre *Guadua spp.* e manejo florestal. |
| **PES-PV** | Pesquisa: PU Vegetal | Desenvolvimento de biopolímeros (Mamona/Resinas). |
| **ENG** | Engenharia | Projetos mecânicos, térmicos e elétricos. |
| **ARQ** | Arquitetura | Projetos de infraestrutura e canteiro-escola. |
| **BIO** | Bioconstrução | Técnicas construtivas de baixo impacto e materiais locais. |
| **BQT** | Briquetes | Processamento de biomassa e densificação energética. |
| **VP** | Vapor | Termodinâmica e propulsão fluvial (Mecânica de Vapor). |
| **MD** | Mem. Descritivo | Detalhamento exaustivo para fins de Patente Social. |

## 3. Protocolo de Status (Visual Badges)

Utilizaremos badges dinâmicos para indicar a prontidão do documento para o fluxo oficial:

| Status | Badge Markdown | Significado |
| :--- | :--- | :--- |
| **Status Ready** | `` | **Pronto**: Higienizado e sincronizado (Biblio/Zenodo). |
| **Em Revisão** | `` | **Aguardando**: Em fase de auditoria editorial ou técnica. |
| **Consolidado** | `` | **Finalizado**: Documento mestre aprovado. |
| **Rascunho** | `` | **Draft**: Fase inicial de redação. |

## 4. Estrutura do Cabeçalho YAML (Modelo Final)

```yaml
projeto: Mulheres Que Tecem a Floresta 
instituicao: Consórcio UnB/UFRR/UFAC
tipo: [CATEGORIA DO GLOSSÁRIO]
referencia: [PREFIXO]-[ID]-[ANO]
status: Status Ready
author:
- <img src="../../../../assets/icons/human_11_black.svg" width="18px"> name: [NOME DO AUTOR ou Consórcio UnB/UFRR/UFAC]
  affiliation: [APENAS SE HOUVER DOI]
  orcid: [APENAS SE HOUVER DOI]
date: '2026-03-24'
doi: [SE EXISTIR]
```
> [!IMPORTANT]
> **Regras de Autoria e Afiliação**:
> 1. **Documentos de Governança/Orçamento**: Não possuem autoria individual. O campo `author.name` deve ser preenchido como `Consórcio UnB/UFRR/UFAC`.
> 2. **Inventos com DOI**: Possuem autoria individual (`Institucional, Fabio Resck`), `affiliation` e `orcid` completos.
> 3. **Inventos SEM DOI**: Possuem autoria individual (`Institucional, Fabio Resck`), mas **Omitir** o campo `affiliation` para manter a flexibilidade da Patente Social até a publicação definitiva.

## 5. Estratégia de Revisão e "Mão à Obra"

Seguiremos o fluxo de revisão por blocos de diretórios para garantir o rigor editorial:

1.  **Bloco 1: 04_GESTAO_OPERACIONAL (Invenções T01-T12)**: Prioridade máxima para alinhamento de patentes sociais.
2.  **Bloco 2: 01_GOVERNANCA**: Padronização dos documentos mestre e orçamentários.
3.  **Bloco 3: 03_DOSSIE_BNDES**: Higienização final para submissão institucional.
4.  **Bloco 4: 02_DIAGNOSTICO%20DE%20AREA**: Estudos, pesquisas e bibliografia.

**Cada ciclo de revisão inclui:**
- <img src="../../../../assets/icons/human_16_black.svg" width="18px"> Aplicação do cabeçalho YAML padronizado.
- <img src="../../../../assets/icons/human_09_black.svg" width="18px"> Inserção do badge `Status Ready` abaixo do título H1.
- <img src="../../../../assets/icons/human_07_black.svg" width="18px"> Higiene Editorial (Substituição de "WTF" e reset de versões para v1.0).
- <img src="../../../../assets/icons/human_20_black.svg" width="18px"> Correção de tabelas Markdown.
> [!NOTE]
> O badge de status deve ser colocado logo abaixo do título principal (#) no corpo do documento Markdown.

---

---

---

---

---
<p align="center"><img src="../../../../assets/logo_BQTF/logo_mqtf_soberana.svg" width="40px"><br><b>Mulheres Que Tecem a Floresta — MQTF</b><br><i>"Soberania não se pede, se exerce."</i></p>