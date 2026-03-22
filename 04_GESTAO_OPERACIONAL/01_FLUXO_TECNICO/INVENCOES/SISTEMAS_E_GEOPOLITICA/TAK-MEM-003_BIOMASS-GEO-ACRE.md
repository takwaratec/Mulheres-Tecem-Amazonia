---
projeto: Mulheres Que Tecem a Floresta (WTF)
instituicao: Consórcio UnB/UFAC/UFRR
tipo: Memorando Técnico
referencia: TAK-MEM-003-2026
status: CONSOLIDADO
author:
- affiliation: Universidade de Brasília / Núcleo Takwara
  name: Takwara, Fabio Resck
  orcid: 0000-0001-8815-3885
---

# Memorando Técnico: Biomassa, Georreferenciamento e Governança de Bambuzais (Acre)

## 1. Contexto Biogeográfico e Biomassa

A região sudoeste da Amazônia (Acre, sudeste do Peru e noroeste da Bolívia) abriga a maior extensão contínua de bambus arborescentes do mundo, cobrindo cerca de **180.000 km²** apenas no estado do Acre. 

### 1.1. Classificação e Domínio
As florestas são classificadas em quatro tipologias principais (fisionomias do IBGE):
- **Floresta Aberta com Bambu Dominante**: Onde o bambu (*Guadua* spp.) suprime a regeneração de outras espécies arbóreas.
- **Floresta Aberta com Bambu Esparso**: Presença significativa mas não dominante.
- Estoque de Biomassa: Estimativas variam de **106,6 a 143,6 Mg/ha** (biomassa seca acima do solo).
- Espécies Chave: *Guadua sarcocarpa* (taboca-mandioca) e *Guadua weberbaueri* (taboca-brava).

### 1.2. Dinâmica de Vida e Morte (Mastragem)
- Ciclo de Floração: Fenômeno de monocarpia (floração e morte síncrona) com ciclo estimado entre **27 e 28 anos**.
- Impacto: A morte em massa cria clareiras que alteram radicalmente a assinatura espectral da floresta, detectável por sensores orbitais.

## 2. Metodologia de Sensoriamento Remoto (Geoprocessamento)

O mapeamento exaustivo no Acre utiliza uma combinação de sensores e algoritmos para separar o "ruído" da floresta densa:

- **Sensores Orbitais**: Landsat (TM/ETM+/OLI), MODIS (NDVI/EVI para séries temporais) e dados de radar (SAR) para penetração na cobertura de nuvens.
- **Algoritmos de Classificação**:
    - **SAM (Spectral Angle Mapper)**: Mede a similaridade espectral entre o pixel e um alvo de referência (endmember). Acurácia superior a 90% na distinção de manchas de bambu.
    - **MAXVER (Máxima Verossimilhança)**: Classificador estatístico robusto para mapeamento de uso e cobertura.
    - **MINDIS (Mínima Distância)**: Utilizado em áreas de transição.
- **Série Temporal**: O uso de índices de vegetação (NDVI/EVI) permite monitorar a senescência e a rebrota pós-floração, crucial para o planejamento do manejo.

## 3. Ecossistema Institucional e Governança (Acre)

O sucesso do Projeto WTF depende da articulação com os detentores do saber técnico e territorial:

| Instituição/Ator | Papel Estratégico | Expertise Específica |
| :--- | :--- | :--- |
| **UFAC (Botânica/Geoprocessamento)** | P&D e Inventário | Dr. Evandro Ferreira e equipe (mapeamento de tabocais). |
| **IFAC (Tecnologia Aplicada)** | Formação e Inovação | Uso do bambu em celulose, nanotecnologia e bioconstrução. |
| **IMAC (Órgão Ambiental)** | Regulação e Licenciamento | Gestão da IN 10/2015 (Manejo Sustentável de Bambu). |
| **CPI-Acre (Comissão Pró-Índio)** | Mediação em TIs | Apoio à gestão territorial em Terras Indígenas (Nukini, Nawa). |
| **AMAAIAC** | Agentes Agroflorestais | Validação de campo por AAFIs (Agentes Agroflorestais Indígenas). |
| **SEICT / SEEPA** | Fomento e Indústria | Articulação com o Plano de Desenvolvimento Sustentável do Acre. |

## 4. Legislação e Manejo (IN 10/2015)

O Acre é pioneiro na regulamentação do manejo de bambu nativo (Instrução Normativa IMAC nº 10/2015).
- **Diretriz**: Permite a exploração comercial sem a necessidade de supressão da floresta (manejo de impacto reduzido).
- **Rastreabilidade**: Integração obrigatória com o SINAFLOR para emissão de DOFs (Documento de Origem Florestal).

## 5. Dados Básicos para SGMAS (Geolocalização e Populações)

Para fins de integração com o Sistema de Gestão e Monitoramento (SGMAS), os dados de referência para a região do Alto Juruá são:

### 5.1. Municípios Foco (Acre)

| Município | População (IBGE 2024) | Coordenadas Sede | Status SGMAS |
| :--- | :--- | :--- | :--- |
| **Cruzeiro do Sul** | 98.382 | 7° 37' 51" S, 72° 40' 12" O | Ativo |
| **Mâncio Lima** | 20.329 | 7° 37' 20" S, 72° 53' 32" O | Ativo |
| **Rodrigues Alves** | 15.537 | 7° 44' 31" S, 72° 38' 49" O | Ativo |
| **Porto Walter** | 11.275 | 8° 16' 08" S, 72° 44' 38" O | Ativo |
| **M. Thaumaturgo** | 17.951 | 8° 56' 27" S, 72° 47' 31" O | Ativo |

### 5.2. Territórios Indígenas (TIs)

- **TI Nukini**: 32.581,94 ha | População: ~900 (2023) | SIRGAS 2000 UTM 18 S.
- **TI Nawa**: Delimitação aprovada (2026) | População: > 300.

## 6. Bibliografia e Referências de Dados (Sync-Link)

1. **Ferreira, E. J. L. (2014)**: *O bambu no Acre: ecologia, economia e potencial*. [Acessar PDF (Auditoria)](../../../../01_SOMBRA_AUDITORIA/04_PROJETO_WTF/01_GOVERNANCA/01_COLABORADORES/Bibliografia_Equipe/Ferreira_2014_Bambu_Acre.pdf)
2. **Carvalho, A. L. (2015)**: *Mapeamento de bambuzais por sensoriamento remoto*. [TAK-MEM-003](TAK-MEM-003_BIOMASS-GEO-ACRE.md)
3. **Nelson, B. W. (2001)**: *Dinâmicas de clareiras e ciclos de floração*. (Science/INPA Data).
4. **IMAC (2015)**: *Instrução Normativa nº 10/2015 - Manejo Sustentável de Bambu*. [Base Regulatória](../../../../01_GOVERNANCA/02_JURIDICO/IN_10_2015_IMAC.pdf)
5. **Relatórios AMAAIAC/CPI-Acre**: Etnomapeamento e gestão florestal em terras indígenas. [TAK-MEM-003-REF](TAK-MEM-003_BIOMASS-GEO-ACRE.md)

---
**Nota Final**: Esta consolidação exaustiva serve como o "Documento Bruto Higienizado". As Notas Técnicas de suporte ao Projeto WTF devem citar este arquivo como fonte primária de dados.

*Redigido em 19 de Março de 2026.*
*Aprovação: Coordenação Técnica (Acre/UnB).*
