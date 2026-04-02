---
projeto: Mulheres Que Tecem a Floresta
instituicao: Consórcio UnB/UFRR/UFAC
tipo: Memorial Descritivo (T10)
referencia: ENG-MD-010-2026
status: Ready
author:
- name: Consórcio UnB/UFRR/UFAC
date: '2026-04-01'
---

![Status: Ready](https://img.shields.io/badge/Status-Ready-brightgreen)

<p align="right"><i>"Ciência é a investigação da verdade."<br>— Carlos Chagas</i></p>

### <img src="../../../../../../assets/patterns/square_05_red.svg" width="22px"> Ficha Técnica e Metadados
*   **Projeto**: Mulheres Que Tecem a Floresta (MQTF)
*   **Instituição**: Consórcio UnB / UFRR / UFAC
*   **Referência**: Memorial Descritivo — Catamarã Utilitário Solar T10 (Fase 1)
*   **Status**: Ready (Consolidado)
*   **Autor**: Consórcio UnB / UFRR / UFAC
*   **Data**: 01 de Abril de 2026

---

# <img src="../../../../../../assets/patterns/square_title_red.svg" width="30px"> Memorial Descritivo: Catamarã Utilitário Solar — Elo de Engenharia Social (T10)

## 1. Contexto e Justificativa

A Bacia Amazônica, especialmente os eixos dos Rios Juruá e Purus, enfrenta um regime hidrológico de sazonalidade extrema. Durante os períodos de vazante (maio a outubro), profundidades inferiores a **0,5 metro** impedem a navegação de embarcações de carga convencionais, resultando em ciclos anuais de isolamento, desabastecimento e perda de produção agrícola e extrativista. A frequência e severidade dessas secas intensificam-se a cada ano, tornando obsoletos os projetos navais dimensionados para calados superiores a 1,0 metro.

A **Balsa Catamarã T10** surge como um **Veículo Utilitário Solar** — o elo físico da Engenharia Social MQTF entre o **Canteiro Escola** e as comunidades isoladas. O dispositivo transporta **Unidades BSM (Banheiro Seco Modular)** e kits de bioarquitetura, opera como plataforma de atendimento itinerante (saúde, educação, assistência social) e escoa produção perecível sob cadeia de frio solar. O beneficiamento primário de ativos (açaí, castanha, farinha) ocorre em pontos estratégicos em terra firme, mantendo a embarcação como veículo utilitário de calado mínimo e máxima agilidade.

O conceito inspira-se no benchmark de micro-mobilidade solar urbana de Londres (Hari Pontoon) — embarcações de bambu com propulsão 100% fotovoltaica e custo operacional de combustível zero — adaptado às condições hidrológicas e sociais da Amazônia profunda.

---

## 2. Engenharia de Materiais e Arquitetura Naval

### 2.1 Especificações Dimensionais e Verificação Hidrostática (Fase 1)

**Arranjo Geral:**

| Parâmetro | Especificação | Justificativa |
|:---|:---|:---|
| **Comprimento (LOA)** | 12,0 metros | Manobrabilidade em rios sinuosos e estreitos. |
| **Boca Máxima (B)** | 4,8 metros | Estabilidade transversal sob carga de convés. |
| **Calado de Projeto (T)** | **0,5 metros** | Acesso em vazante extrema (Alto Juruá e Purus). |

**Geometria Individual de Cada Casco (Tipo Pontão Plano):**

| Parâmetro | Valor | Nota |
|:---|:---|:---|
| **Largura do casco (b)** | 1,18 m | Fundo plano, seção retangular com borda arredondada. |
| **Comprimento na linha d'água (Lwl)** | 12,0 m | ≈ LOA (proa em rampa suave, sem bulbo). |
| **Calado (T)** | 0,5 m | Condição de carga máxima operacional. |
| **Coeficiente de Bloco (Cb)** | 0,85 | Típico de pontão plano / flat-bottom craft. |
| **Volume deslocado por casco** | 12,0 × 1,18 × 0,5 × 0,85 = **6,02 m³** | — |
| **Volume deslocado total** | 2 × 6,02 = **12,04 m³** | — |
| **Deslocamento (Δ)** | **12,0 Toneladas** | ρ água doce = 1.000 kg/m³. |
| **Espaçamento entre cascos** | 4,8 − (2 × 1,18) = **2,44 m** | Espaço livre para câmara fria sob convés e passagem. |

**Balanço de Massa (Condição de Carga Máxima):**

| Componente | Massa (kg) | % do Δ |
|:---|:---|:---|
| Casco + convés (biocompósito monolítico) | 2.500 | 21,5% |
| Sistema solar (16 painéis × 25 kg) | 400 | 3,4% |
| Baterias LiFePO4 (2 × 200 kg) | 400 | 3,4% |
| Motores elétricos (2 × 50 kg) | 100 | 0,9% |
| Travessas + teto (colmos inteiros de bambu) | 450 | 3,9% |
| Câmara fria (envelope + compressores) | 350 | 3,0% |
| Instrumentação + elétrica + amarrações | 200 | 1,7% |
| **Peso Leve (Lightship)** | **4.400** | **37,8%** |
| Carga útil (4 BSM + 2 kits) | 4.400 | 36,7% |
| Câmara fria carregada (1.740 kg produto) | 1.740 | 14,5% |
| Tripulação + consumíveis (4 pessoas) | 400 | 3,4% |
| Reserva de margem | 1.060 | 9,1% |
| **Deslocamento Total (Δ)** | **12.000** | **100%** |

> [!NOTE]
> O casco tipo pontão plano (flat-bottom) é consistente com a operação em águas rasas — minimiza o calado e maximiza a estabilidade de plataforma sob carga de convés. A relação L/B de cada casco (12,0 / 1,18 = **10,2**) é típica de catamarãs de trabalho fluvial.

### 2.2 Estrutura Monolítica em Biocompósitos (Zero Aço Estrutural)

A inovação estrutural reside na construção de um **casco monolítico** inteiramente em biocompósito, integrado a câmaras de refrigeração, muratas de proteção e cobertura treliçada — sem qualquer elemento metálico estrutural. O processo construtivo segue seis estágios:

1. **Travessas transversais e convés**: Colmos inteiros de bambu *Guadua weberbaueri* (diâm. 8–12 cm, comprimento 4,8 m) interligam os dois flutuadores. Sobre eles, esteira contínua de ripas de bambu. Fusão monolítica com **Mamonex RD70** (PU vegetal). Acabamento antiderrapante em areia/PU.

2. **Câmaras de refrigeração distribuídas no casco**: Em lugar de uma câmara única sob convés, **câmaras modulares em filas** são moldadas diretamente no corpo dos cascos, integralmente confeccionadas em **PU + bambu + fibras** (ou areia, quando disponível por assoreamento). As câmaras funcionam simultaneamente como **bancos de convés**, dada a resistência comprovada do compósito à corrosão e ao atrito pesado. Os **condensadores de refrigeração ficam embutidos na parte inferior do casco**, em contato permanente com a água do rio (~27°C), mantendo a temperatura do dissipador sempre estável e resfriada.

   | Vantagem | Câmara Única (anterior) | Câmaras Distribuídas (atual) |
   |:---|:---|:---|
   | **ΔT condensador** | 30°C (ar a 35°C → 5°C) | **22°C** (água a 27°C → 5°C) |
   | **Eficiência COP** | ~2,5 (ar-ar) | **~3,5** (água-ar) → economia ~30% |
   | **Redundância** | Falha única = perda total | Falha parcial, demais operam |
   | **Dupla função** | Espaço dedicado | **Bancos de convés** |
   | **Distribuição de peso** | Concentrado sob convés | **Distribuído nos cascos** |

3. **Muratas de contra sol**: Painéis verticais em **PU + bambu + fibras** nas laterais, protegendo as câmaras de radiação solar direta. Confecção idêntica ao casco: camadas sucessivas de PU expansivo + fibras + impermeabilizante, conferindo isolamento térmico contínuo. Quando há abundância de areia de assoreamento, esta substitui as fibras como agregado no compósito (PU + areia), aumentando a massa térmica.

4. **Treliças de cobertura**: O vão de **4,8 m é vencido por treliças de bambu** (tipo Warren simplificada), eliminando a necessidade de pilares centrais. As treliças são montadas por amarrações com cabo flexível e monolitizadas com PU. Espaçamento entre treliças: ~3,0 m (4 treliças ao longo dos 12 m).

5. **Segmentos de vara + painéis solares**: Os painéis fotovoltaicos são sustentados por **segmentos de vara de bambu** longitudinais, apoiados nas treliças, monolitizados com PU expansivo e camadas sucessivas de fibras impermeabilizantes — conferindo isolamento térmico à cobertura e rigidez estrutural ao teto plano.

6. **Porcas olhal de ancoragem e içamento**: Distribuídas em **malha de 3 × 3 m** ao longo da superfície do teto/treliças, embutidas nos segmentos de vara e monolitizadas com PU. Servem para:
   - Ancoragem de **redes de descanso** (10+ posições flexíveis)
   - **Içamento de carga** (BSM, kits, produtos)
   - Fixação de equipamentos temporários

   | Grade de olhais | Posição |
   |:---|:---|
   | **Longitudinal** | 0m, 3m, 6m, 9m, 12m (5 linhas) |
   | **Transversal** | 0m, 2,4m, 4,8m (3 linhas) |
   | **Total de pontos** | **15 porcas olhal** |

Características do compósito:

- <img src="../../../../../../assets/icons/human_17_black.svg" width="18px"> **Núcleo de Preenchimento**: Mamonex RD70 (Dens. 70 kg/m³). Vedação hidrofóbica e isolamento térmico em corpo único.
- <img src="../../../../../../assets/icons/human_04_black.svg" width="18px"> **Pele Estrutural**: Laminado de Bambu *Guadua weberbaueri* (Dens. 670 kg/m³) com resina de mamona, termorretificado a 160°C.
- <img src="../../../../../../assets/icons/human_05_black.svg" width="18px"> **Densidade Média do Compósito**: **350 kg/m³** — redução de massa de **95%** em relação ao aço naval (7.800 kg/m³) e **87%** em relação ao alumínio (2.700 kg/m³).

> [!IMPORTANT]
> **Política de Zero Aço Estrutural**: Nenhum elemento metálico é utilizado como componente estrutural. Os únicos elementos metálicos são: (a) **porcas olhal** de ancoragem/içamento (peças de fixação, não estruturais), (b) **amarrações com cabo flexível** em pontos específicos, (c) **parafusos de fixação** de equipamentos elétricos.

### 2.3 Tratamento de Interface (Protocolo de Campo)

O tratamento do bambu segue protocolo de neutralização e proteção biológica em dois estágios:

1. **Banho de diquada de cinzas** (2h a 3h): Alcalinização e estabilização de pH com cinzas de madeiras taninosas (angico, barbatimão, aroeira) em vapor saturado.
2. **Banho de ácido pirolenhoso** (30 min): Impregnação antifúngica e bactericida com extrato pirolenhoso (subproduto da carbonização controlada).

O protocolo elimina a dependência de reagentes industriais importados (NaOH, boro) e pode ser executado em fornos ecológicos de campo.

---

## 3. Propulsão Solar Dupla (Fase 1)

A embarcação opera com **dois motores elétricos de 60 HP** (15 kW contínuos cada), configurados para:

- **Operação intercalada**: Um motor por vez, alternando desgaste e estendendo a vida útil. Autonomia de **≈ 4 horas/dia** (média anual) a **≈ 3,5 horas** (pior mês) a velocidade de cruzeiro (6–8 nós).
- **Carga total**: Dois motores simultâneos para transporte de BSM sob correnteza forte ou manobra de precisão. Autonomia de **≈ 1,9 horas/dia** (média anual).
- **Propulsão diferencial**: Controle independente de cada motor permite manobra em rios sinuosos sem leme mecânico, essencial para a navegação no Alto Juruá.

### 3.1 Sistema Fotovoltaico

- <img src="../../../../../../assets/icons/human_12_black.svg" width="18px"> **Teto Solar Plano**: 16 painéis monocristalinos de 450W em layout 4×4 sobre teto estrutural. Potência instalada: **7,2 kWp**.
- <img src="../../../../../../assets/icons/human_09_black.svg" width="18px"> **Geração Diária Efetiva**: 27,0 kWh/dia (média anual, PR=0,75) a 20,5 kWh/dia (pior mês, fevereiro). Fonte: Atlas INPE/LABREN.
- <img src="../../../../../../assets/icons/human_10_black.svg" width="18px"> **Armazenamento**: 2 bancos LiFePO4 48V/400Ah (38,4 kWh nominal, 30,7 kWh utilizáveis a 80% DoD).
- **Orçamento energético diário total**: **57,7 kWh** (média) / **51,2 kWh** (pior mês).

### 3.2 Roadmap (Fase 2)

O sistema de Propulsão a Vapor Uniflow (cogeração com biomassa) será implementado na fase de expansão para rotas transfronteiriças e processamento térmico pesado. As especificações técnicas encontram-se no [Memorial de Patente T10 — Fase 2](ENG-MEM-T10_BALSA-CATAMARA-VAPOR.md).

---

## 4. Captação de Água Pluvial e Potabilização a Bordo

O teto plano do T10 funciona como superfície de captação de água da chuva e condensação de orvalho, alimentando um sistema de armazenamento e potabilização integrado à arquitetura naval.

### 4.1 Dados Pluviométricos — Cruzeiro do Sul (INMET, Normal Climatológica)

| Mês | Precipitação (mm) | Captação Estimada (L) | Período |
|:---|:---|:---|:---|
| Jan | 258 | 8.256 | Chuvoso |
| Fev | 277 | 8.864 | Chuvoso |
| Mar | 299 | 9.568 | Chuvoso |
| Abr | 244 | 7.808 | Chuvoso |
| Mai | 163 | 5.216 | Transição |
| Jun | 87 | 2.784 | Seco |
| Jul | 66 | 2.112 | Seco |
| Ago | 86 | 2.752 | Seco |
| Set | 135 | 4.320 | Transição |
| Out | 215 | 6.880 | Chuvoso |
| Nov | 231 | 7.392 | Chuvoso |
| Dez | 223 | 7.136 | Chuvoso |
| **Anual** | **2.283** | **73.088** | — |

> **Cálculo**: Captação = Precipitação (m) × Área de coleta (40 m²) × Eficiência (0,80). A eficiência de 80% desconta evaporação, respingos e primeira descarga (first-flush).

### 4.2 Balanço Hídrico Diário

| Variável | Cenário Chuvoso (Nov–Abr) | Cenário Seco (Jun–Ago) |
|:---|:---|:---|
| **Captação diária média** | ~260 L/dia | ~85 L/dia |
| **Coleta de orvalho** (painéis solares, noturna) | ~10 L/dia | ~15 L/dia |
| **Total disponível** | ~270 L/dia | ~100 L/dia |
| **Demanda** (4 tripulantes × 15 L + BSM fixa 10 L) | **70 L/dia** | **70 L/dia** |
| **Excedente / Reserva** | +200 L/dia | +30 L/dia |

> [!NOTE]
> **Coleta de orvalho**: Na Amazônia equatorial (umidade relativa >80%), os painéis solares resfriam por radiação noturna, formando condensação superficial. A coleta ocorre naturalmente pelo mesmo sistema de calhas do teto. O rendimento estimado de **0,3–0,4 L/m²/noite** (35 m² de painéis) contribui com 10–15 L/dia adicionais.

### 4.3 Sistema de Captação e Potabilização (4 Estágios)

| Estágio | Componente | Função | Especificação |
|:---|:---|:---|:---|
| **1** | **First-flush diverter** | Rejeita os primeiros 2mm de chuva (lava a superfície do teto) | Válvula automática gravitacional, volume de descarte: 80 L |
| **2** | **Filtro de sedimentos** | Remoção de partículas >50 μm (poeira, folhas, detritos orgânicos) | Filtro-bolsa lavável, troca mensal |
| **3** | **Carvão ativado de coco babaçu** | Adsorção de matéria orgânica, cor, sabor e compostos voláteis | Cartucho de 10″, substituição trimestral |
| **4** | **Esterilização UV solar** | Eliminação de patógenos (E. coli, coliformes, vírus) | Lâmpada UV-C 12W alimentada pelo sistema solar (consumo: 0,3 kWh/dia) |

**Reservatório**: Tanque de **500 litros em PU Vegetal (Mamonex RD70)**, moldado diretamente na aplicação do PU ao casco — integrado à estrutura monolítica. A cavidade do tanque delimita simultaneamente os **pontos de ancoragem dos pilares** da estrutura do platô de cobertura, criando uma relação estrutural entre reservatório, pilares e casco. Indicador de nível IoT integrado. 

> [!TIP]
> **Backup de campo**: Em caso de falha do sistema UV, a potabilização pode ser feita por **fervura solar** (concentradores parabólicos improvisados) ou por aplicação do método SODIS (exposição solar direta em garrafa PET por 6h, validado pela OMS para a faixa equatorial).

### 4.4 Infraestrutura de Coleta no Teto

O teto plano recebe uma **micro-inclinação de 1,5%** (1,5 cm/m) em direção às calhas laterais, imperceptível visualmente mas suficiente para escoamento gravitacional.

- **Calhas laterais**: 2 × 12 m, em bambu laminado resinado (Mamonex RD70), integradas à estrutura do teto.
- **Condutores verticais**: 2 descidas (proa e popa), em tubo de bambu ou PVC reciclado, para o first-flush diverter.
- **Desaguadouro de emergência**: Saída de overflow direta para o rio em caso de tanque cheio.

---

## 5. Impacto Social e Logística Utilitária

O convés do T10 é **totalmente livre de pilares centrais** — o vão de 4,8 m é vencido por treliças de bambu apoiadas nas muratas laterais. A configuração maximiza a flexibilidade operacional:

- <img src="../../../../../../assets/icons/human_11_black.svg" width="18px"> **Logística BSM e Kits**: Capacidade para **4 Unidades BSM de carga** e 2 Kits de Construção por jornada (~4.400 kg). Içamento pelos olhais de teto.
- <img src="../../../../../../assets/icons/human_06_black.svg" width="18px"> **BSM Fixa de Bordo** (popa-bombordo): 1 Unidade BSM permanente para tripulantes e passageiros. Compostagem seca com separação urina/sólidos.
- <img src="../../../../../../assets/icons/human_03_black.svg" width="18px"> **Câmaras Frias Distribuídas (2,9 m³ total)**: Moldadas no corpo dos cascos, com condensadores submersos. Funcionam como **bancos de convés**. Consumo: ~4,2 kWh/dia (COP ~3,5 por resfriamento a água).
- <img src="../../../../../../assets/icons/human_14_black.svg" width="18px"> **Redário Flexível (10+ redes)**: Suspensas entre quaisquer pares de **porcas olhal** (malha 3×3m, 15 pontos). Posições ajustáveis conforme a operação.
- <img src="../../../../../../assets/icons/human_09_black.svg" width="18px"> **Água Potável a Bordo**: Tanque PU 500 L (moldado no casco) com potabilização em 4 estágios. Autonomia: 5–7 dias.
- <img src="../../../../../../assets/icons/human_17_black.svg" width="18px"> **Soberania Energética e Hídrica**: Combustível fóssil: **R$ 0**. Água potável: **R$ 0**.

### 5.2 Arranjo de Convés — Treliças, Olhais e Câmaras-Banco

```
                PROA (1m recuo)
┌──────────────────────────────────────────────┐
│                 TIMONEIRO                    │
│   ⊕─────────────⊕─────────────⊕             │  ← olhais (teto)
│                                              │
│ ▓▓▓  •  câm  •  câm  •  câm  •  câm  •  ▓▓▓│  ← muratas + câm.banco (BB)
│ ▓▓▓                                     ▓▓▓│
│ ▓▓▓     CONVÉS LIVRE (sem pilares)      ▓▓▓│  ← 4,8m vencido por treliças
│ ▓▓▓                                     ▓▓▓│
│ ▓▓▓  •  câm  •  câm  •  câm  •  câm  •  ▓▓▓│  ← muratas + câm.banco (BE)
│                                              │
│   ⊕─────────────⊕─────────────⊕             │  ← olhais (teto)
│                                              │
│   ⊕─────────────⊕─────────────⊕  [BSM FIXA] │  ← olhais (teto)
│                 POPA (1m recuo)    [BB-popa]  │
└──────────────────────────────────────────────┘
 ═══════════ GUARDA-CORPO (perímetro) ═══════════

LEGENDA:
  ⊕   Porca olhal embutida (malha 3×3m) — 15 pontos
  ▓▓▓ Murata de contra sol (PU+bambu+fibras)
  •   Separador de câmaras-banco
  câm Câmara fria distribuída (banco/conservação)
```

**Especificação das treliças:**

| Parâmetro | Valor |
|:---|:---|
| **Tipo** | Warren simplificada (bambu *Guadua*) |
| **Vão** | 4,8 m (apoio nas muratas laterais) |
| **Quantidade** | 4 treliças (a cada 3,0 m) |
| **Altura da treliça** | ~0,4 m (perfil baixo) |
| **Fixação** | Amarrações cabo flexível + PU monolítico |
| **Pé-direito sob teto** | ~2,2 m (livre, sem obstrução) |

**Guarda-corpo (obrigatório — NORMAM-02/DPC):**

| Parâmetro | Especificação NORMAM-02 | Solução T10 |
|:---|:---|:---|
| **Altura mínima** | ≥ 1,0 m | **1,0 m** |
| **Vão inferior** | ≤ 230 mm | **200 mm** |
| **Demais vãos** | ≤ 380 mm | **300 mm** (3 horizontais em bambu) |
| **Material** | Adequado ao serviço | Bambu laminado resinado (Mamonex RD70) |
| **Perímetro total** | Toda a borda aberta | ~30 m (2 × 12m laterais + 2 × 3m proa/popa) |

**Flutuadores de emergência:**

Compartimentos sob o teto (integrados às treliças) abrigam **flutuadores de emergência** (tipo rolo de espuma PU) de liberação rápida por tração manual, distribuídos a cada 3 metros do perímetro.

---

## 5. Enquadramento BNDES / Fundo Amazônia

A inclusão do T10 Solar no portfólio BNDES altera o paradigma de logística passiva para **Logística Ativa e de Apoio Social**. O enquadramento foca na inovação radical dos cascos de biocompósitos e no papel estratégico da embarcação como elo central para instalação de infraestrutura sanitária (BSM) e fortalecimento da soberania nos territórios.

| Parâmetro | Valor |
|:---|:---|
| **CAPEX por unidade (Fase 1, propulsão dupla)** | **R$ 236.100,00** |
| **Valuation de Contrapartida (1.4x)** | **R$ 330.540,00** |
| **OPEX de combustível fóssil** | **R$ 0,00** |
| **Eficiência operacional** | Eliminação total da dependência de diesel na Fase 1. |

A especificação completa de itens e custos encontra-se no [BoM Detalhado T10](ENG-BOM-T10_DETALHADO.md).

---

## 7. Segurança e Conformidade (NORMAM-02/DPC)

A embarcação em sua configuração de Fase 1 (solar/elétrica) opera sem caldeira, sem pressão térmica e sem combustíveis inflamáveis a bordo. **LOA 12m → Embarcação de médio porte** (NORMAM-02/DPC, navegação interior).

### 7.1 Conformidade Regulatória

| Requisito NORMAM-02 | Solução T10 | Status |
|:---|:---|:---|
| **Guarda-corpo** (vão inf. ≤230mm, demais ≤380mm) | Bambu laminado, h=1,0m, vãos 200/300mm | ✅ |
| **Boias salva-vidas** (≥2 unidades, tipo circular ou ferradura) | 2 boias c/ retinida flutuante | ✅ |
| **Coletes salva-vidas** (1 por pessoa a bordo) | 8 coletes (4 tripulantes + 4 passageiros) | ✅ |
| **Flutuadores de emergência** | Rolos de espuma PU em compartimentos sob teto | ✅ |
| **Borda livre** (L<20m, dispensa cálculo formal) | Atendida pelo calado de projeto 0,5m | ✅ |
| **Corredores de acesso** (≥650mm para ≤10m) | 800 mm (entre guarda-corpo e coluna lateral) | ✅ |
| **Certificação elétrica** | BMS integrado (sobre-carga, curto, temperatura) | ✅ |
| **Flutuabilidade redundante** | 2 cascos independentes c/ compartimentação estanque | ✅ |
| **Sem combustível inflamavel** | Propulsão 100% elétrica/solar | ✅ |

### 7.2 Dotação de Salvatagem

| Item | Qtd | Localização |
|:---|:---|:---|
| Boia salva-vidas c/ retinida | 2 | Proa (BB) + Popa (BE) |
| Coletes salva-vidas | 8 | Compartimento sob teto (acesso rápido) |
| Flutuadores de emergência (rolos PU) | 4 | Compartimentos sob teto (a cada 3m do perímetro) |
| Extintor de incêndio (CO2 ou pó químico) | 1 | Junto ao quadro elétrico |
| Kit primeiros socorros | 1 | Timoneiro |

---
<p align="center"><img src="../../../../../../assets/logo_BQTF/logo_mqtf_soberana.svg" width="40px"><br><b>Mulheres Que Tecem a Floresta — MQTF</b><br>Consórcio Científico UnB / UFRR / UFAC<br><i>"Soberania não se pede, se exerce."</i></p>