---
projeto: Mulheres Que Tecem a Floresta
instituicao: Consórcio UnB / UFRR / UFAC
tipo: Documentação Técnica
referencia: ENG-MEM-T01_FORNO-ECOLOGICO.md
status: Em Revisão
---

<p align="right"><i>"A educação é o direito de todos e dever do Estado."<br>— Anísio Teixeira</i></p>

### <img src="../../../../assets/patterns/square_05_red.svg" width="22px">&nbsp; Ficha Técnica e Metadados
*   **Projeto**: Mulheres Que Tecem a Floresta (MQTF)
*   **Instituição**: Consórcio UnB / UFRR / UFAC
*   **Referência**: ENG-MEM-T01_FORNO-ECOLOGICO.md
*   **Status**: Em Revisão

![Status: Em Revisão](https://img.shields.io/badge/Status-Em_Revisão-yellow)

# Memorial Técnico: Forno Ecológico T01 — Unidade Comunitária Replicável

**Módulo Base de Bioeconomia, Soberania Energética e Purificação de Água**

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.18827106-blue.svg)](https://doi.org/10.5281/zenodo.18827106)
[![Licença: CC BY 4.0](https://img.shields.io/badge/Licenca-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

---

## 1. Campo da Invenção e Estratégia

O **Forno Ecológico T01** é uma unidade térmica compacta e replicável, projetada para ser multiplicada em diversos pontos comunitários, conferindo **autonomia energética e instrumental** para melhoria de cadeias de produção, conforto térmico e **purificação de água**.

O sistema integra em um único corpo construtivo:

- <img src="../../../../assets/icons/human_05_black.svg" width="18px"> **Geração de vapor** (serpentina inox no riser) para tratamento de bambu e pasteurização de água
- <img src="../../../../assets/icons/human_17_black.svg" width="18px"> **Geração de energia** (módulos TEG na carenagem cerâmica) para bombas, ventilador, iluminação e sensores
- <img src="../../../../assets/icons/human_09_black.svg" width="18px"> **Condensação de pirolenhoso** (chaminé resfriada por plenum d'água) para defensivo agrícola e conservante de bambu
- <img src="../../../../assets/icons/human_04_black.svg" width="18px"> **Secagem de fibras** (ar quente soprado via plenum) por soprador externo

O T01 é a versão artesanal e de baixo CAPEX do sistema. Sua escala industrial (T02) difere apenas no **tamanho da fornalha** e na adição de uma **Retorta de Ativação Interna (RAI)** para produção de carvão ativado para filtros.

---

## 2. Arquitetura do Sistema — Estrutura de Confinamento e Carenagem

### 2.1 Encapsulamento Geral

O sistema é encapsulado em uma **carenagem externa** (tambor metálico de aço, chapa 2,3 mm) que isola o ambiente externo do calor intenso e confere suporte estrutural. A **base é suspensa**, permitindo a entrada de ar primário por baixo e a ejeção central de cinzas para fora do recinto.

### 2.2 Universo Sujo vs. Universo Limpo

A inovação reside na **separação hermética** dos dois fluxos de gases:

- <img src="../../../../assets/icons/human_04_black.svg" width="18px"> **Universo Sujo (Combustão)**: O riser em "L" confina a queima da biomassa, onde os gases atingem temperaturas de até **525°C**. Os voláteis e a fumaça são direcionados hermeticamente para o condensador.
- <img src="../../../../assets/icons/human_19_black.svg" width="18px"> **Universo Limpo (Plenum)**: Um trocador de calor (plenum) envolve o riser. O ar é forçado por uma **ventoinha automotiva (12V)** regulada por **PWM via Arduino**, garantindo calor limpo para secagem e climatização sem contato com a fumaça.

### 2.3 Corte Transversal

```
              ┌─── CARENAGEM EXTERNA (tambor aço 2,3mm) ───┐
              │  ░░░░░░░░░░░ ISOLAMENTO ░░░░░░░░░░░░░░░░░ │
              │  ░ PU vegetal + cinzas (camadas) ░░░░░░░░░ │
              │  ░ ┌─── Lã de rocha (30mm) ───┐ ░░░░░░░░░ │
              │  ░ │ ┌── Fibra cerâmica (30mm) ─┐ │ ░░░░░ │
              │  ░ │ │ ╔═══ TEG (8 módulos) ═══╗ │ │ ░░░░ │
              │  ░ │ │ ║     (lado quente)     ║ │ │ ░░░░ │
              │  ░ │ │ ╠═══════════════════════╣ │ │ ░░░░ │
              │  ░ │ │ ║  ┌─────────────┐      ║ │ │ ░░░░ │
              │  ░ │ │ ║  │   RISER      │      ║ │ │ ░░░░ │
              │  ░ │ │ ║  │  Ø 150mm     │      ║ │ │ ░░░░ │
              │  ░ │ │ ║  │  ⟳ SERPENT.  │      ║ │ │ ░░░░ │
              │  ░ │ │ ║  │  ⟳ Inox 304  │      ║ │ │ ░░░░ │
              │  ░ │ │ ║  │  ⟳ 10 esp.   │      ║ │ │ ░░░░ │
              │  ░ │ │ ║  └─────────────┘      ║ │ │ ░░░░ │
              │  ░ │ │ ╚═══════════════════════╝ │ │ ░░░░ │
              │  ░ │ └──────────────────────────┘ │ ░░░░░ │
              │  ░ └──────────────────────────────┘ ░░░░░ │
              │  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
              └────────────────────┬──────────────────────┘
                                   │
              ┌────────────────────┴──────────────────────┐
              │         CÂMARA DE COMBUSTÃO               │
              │       (Magazine briquetes lateral)        │
              ├──────────────────────────────────────────┤
              │  ▼  BASE SUSPENSA (grade de cinzas)  ▼   │
              └──────────────────────────────────────────┘
                         ↑ AR PRIMÁRIO ↑
```

**Camadas (do centro para fora):**

| Camada | Material | Espessura | Função |
|:---|:---|:---|:---|
| **1. Riser** | Tubo inox 304 (Ø 150mm, h = 600mm) | 2 mm | Canal de tiragem ascendente |
| **2. Serpentina** | Inox 304 (Ø tubo 15mm, 10 espiras) | — | Geração de vapor (flash tube) |
| **3. Fibra cerâmica** | Manta cerâmica 1260°C (CFD-Validated) | **30 mm** | Proteção TEGs + Eficiência Térmica (11,15% gain) |
| **4. Módulos TEG** | BiTe/PbTe 40×40mm (8 unidades) | — | Calor → eletricidade (sem fuligem) |
| **5. Lã de rocha** | Manta mineral | **30 mm** | Isolamento 2° (proteção estrutural) |
| **6. PU + cinzas** | PU vegetal + cinzas (camadas) | ~20 mm | Isolamento complementar + massa térmica |
| **7. Carenagem metálica** | Aço carbono (tambor Ø ~450mm) | **2,3 mm** | Estrutura externa + proteção |

---

## 3. Dimensionamento do Rocket Stove (Câmara Ampliada para Briquetes)

### 3.1 Cálculos Dimensionais (Proporção 1:2:4)

| Parâmetro | Cálculo | Valor |
|:---|:---|:---|
| **Diâmetro do sistema** | Definido | **Ø 150 mm** (6") |
| **Área da seção transversal** | π × (0,075)² | **176 cm²** |
| **Câmara de alimentação (h)** | 1 × Ø (mín.) | **300 mm** (ampliada para **400 mm** para briquetes) |
| **Túnel de combustão (L)** | 2 × Ø | **300 mm** |
| **Riser (H)** | 4 × Ø | **600 mm** (mínimo para tiragem eficiente) |
| **Potência térmica estimada** | Briquetes 5.500 kcal/kg, 2–3 kg/h | **~12–16 kW térmicos** |

### 3.2 Câmara de Combustão Ampliada

A câmara de combustão do T01 é **ampliada lateralmente** em relação a um rocket stove convencional, permitindo a queima de **briquetes de biomassa compactada** (Ø 70mm × 200mm, PCS 4.500–6.200 kcal/kg). A alimentação é por **gravidade lateral** (magazine inclinado a 30°), permitindo operação semi-contínua sem abertura da câmara.

| Parâmetro | Valor |
|:---|:---|
| **Dimensão da câmara** | 200mm (L) × 200mm (P) × 400mm (H) |
| **Volume útil** | ~16 litros |
| **Capacidade de briquetes** | 3–4 unidades (2–3 kg) |
| **Autonomia por carga** | ~45–60 minutos |
| **Temperatura no riser** | 600–900°C |
| **Temperatura na serpentina** | 200–400°C (zona de vapor) |

---

## 4. Serpentina de Vapor (Flash Tube)

### 4.1 Dimensionamento

| Parâmetro | Valor | Justificativa |
|:---|:---|:---|
| **Material** | **Inox 304** | Resiste a 850°C sem degradação (cobre falha a 400°C) |
| **Diâmetro do tubo** | 15 mm (Ø ext.) | Padrão hidráulico, fácil conformação |
| **Diâmetro da hélice** | 150 mm (= Ø riser) | Envolvente ao riser interno |
| **Espiras** | 10 | Comprimento total: ~4,7 m de tubo |
| **Passo entre espiras** | 60 mm | Altura total: 600 mm (= altura do riser) |
| **Alimentação** | Gravitacional (coluna d'água suspensa) | Sem bomba — tanque elevado a 1,5–2,0 m |
| **Produção de vapor** | ~15–25 L/h de vapor a 100–140°C | Eficiência sustentada por Fluência Térmica |

### 4.3 Fluência Térmica e Desempenho CFD

O design do T01 integra os achados de simulação de dinâmica de fluidos computacional (CFD) para maximizar a transferência de calor:

- **Destaque Científico**: Conforme resenhado em **[RES_rocket-stove.md](../../../../02_DIAGNOSTICO DE AREA/02_ESTUDOS_E_PESQUISAS/RES_rocket-stove.md)**, a aplicação de isolamento em fibra cerâmica (30mm) eleva a temperatura na interface de trabalho para **452,94°C** (ganho de 11,15%).
- **Fluência da Serpentina**: Esta temperatura crítica garante que o gradiente térmico entre os gases de exaustão e a serpentina inox seja máximo, forçando a fluência do vapor através das 10 espiras sem condensação prematura, mesmo em ambientes amazônicos de alta umidade.
- **Estabilidade**: O isolamento atua como uma "bateria térmica", estabilizando a produção de vapor necessária para o protocolo soberano de 2-3h de banho.

### 4.2 Usos do Vapor

| Aplicação | Descrição |
|:---|:---|
| **Tratamento de bambu** | Vapor saturado + EP (20%) para imunização fungicida/bactericida |
| **Pasteurização de água** | Vapor conduzido por serpentina imersa em tanque d'água → potabilização |
| **Secagem de fibras** | Vapor residual aquece ar no plenum para secagem convectiva |

> [!IMPORTANT]
> **Purificação de água**: A serpentina do riser pode pasteurizar água ao aquecê-la acima de 75°C por 15 minutos. Um circuito secundário de água potável, alimentado por gravidade e passando pela serpentina, pode produzir **~20 L/h de água pasteurizada** — autonomia hídrica para uma comunidade de 20–30 pessoas.

---

## 5. Geração de Energia — Módulos TEG (Seebeck)

### 5.1 Princípio

Os módulos Termoelétricos (TEG) são fixados na **face externa da carenagem cerâmica**, aproveitando o calor radiante **sem contato com fuligem** — conferindo maior vida útil. A carenagem cerâmica protege os TEGs de choque térmico direto e de partículas.

### 5.2 Dimensionamento

| Parâmetro | Valor |
|:---|:---|
| **Temperatura lado quente** | ~300–400°C (superfície da carenagem) |
| **Temperatura lado frio** | ~80–100°C (dissipador com lã de rocha) |
| **ΔT efetivo** | ~200–300°C |
| **Potência por módulo** | ~10–15 W (módulos BiTe 40×40mm) |
| **Quantidade de módulos** | **8 módulos** (circunferência da carenagem) |
| **Potência total TEG** | **80–120 W** |

### 5.3 Alocação de Potência

| Consumidor | Potência (W) | Função |
|:---|:---|:---|
| Bomba de circulação d'água (plenum → serpentina enterrada) | 30–40 | Resfriamento do condensador de pirolenhoso |
| Soprador/ventilador externo | 25–35 | Empurra ar quente para dutos de secagem (plenum) |
| Iluminação LED | 10–15 | Iluminação do posto de trabalho |
| Termosensores + IoT | 5–10 | Monitoramento de temperatura (riser, vapor, câmaras) |
| **Total** | **70–100 W** | **Margem: 20–30% de reserva** |

> [!NOTE]
> **Bateria de buffer**: Um banco de 12V/20Ah (LiFePO4) armazena a geração contínua dos TEGs, permitindo operação dos equipamentos mesmo durante interrupções de alimentação do forno. Autonomia de buffer: ~2h sem fogo.

---

## 6. Condensação de Pirolenhoso — Sistema Gravitacional

### 6.1 Circuito de Condensação

```
 CHAMINÉ (gases quentes da pirólise)
     │
     ▼
 ┌──────────────┐
 │  PLENUM DE   │ ← Tambor de 200L cheio d'água
 │  RESFRIAMENTO│    (chaminé passa por dentro)
 │         │    Gases resfriam de ~300°C → ~40°C
 └──────┬───────┘
        │ (condensado por gravidade)
        ▼
 ┌──────────────┐
 │   SIFÃO      │ ← Separação líquido (EP) / gás (não-condensáveis)
 │  DECANTADOR  │
 └──────┬───┬───┘
        │   │
        ▼   ▼
   EP (líq) Gases → retorno ao queimador (retroalimentação térmica)
   coleta
   em bombona
```

### 6.2 Resfriamento do Plenum

A água do plenum (tambor 200L) aquece progressivamente. A **bomba de circulação** (alimentada pelos TEGs) circula essa água por uma **serpentina enterrada** a ~0,5–1,0 m de profundidade, onde o solo (~22–25°C na Amazônia) funciona como dissipador de calor permanente.

| Parâmetro | Valor |
|:---|:---|
| **Volume do plenum** | 200 L (tambor padrão) |
| **Serpentina enterrada** | PEAD Ø 25mm, 15–20 m de comprimento |
| **Profundidade** | 0,5–1,0 m |
| **Temperatura do solo (Amazônia)** | ~22–25°C |
| **Capacidade de dissipação** | ~2–3 kW térmicos |
| **Bomba de circulação** | 12V DC, 30W (alimentada por TEG) |
| **Produção de EP** | ~3–5 L/h (40–45% de rendimento da biomassa) |

> [!TIP]
> **Rendimento do pirolenhoso**: A condensação gravitacional com plenum d'água mantém eficiência de captura de ~85–90% dos voláteis condensáveis. O sifão decantador separa o EP bruto (pH ~2,5) do alcatrão pesado. Após 90 dias de maturação, o EP está pronto para uso como defensivo agrícola (diluição 1:200) ou conservante de bambu.

---

## 7. Secagem de Fibras — Plenum de Ar Quente e Automação

A **ventoinha automotiva (12V)** — posicionada a distância segura da junta cerâmica — **sopra ar ambiente para dentro do plenum** (pressão positiva), onde ele aquece ao circular entre o isolamento e a carenagem metálica. O ar quente limpo é então direcionado por dutos para câmaras de secagem.

### 7.1 Controle Térmico por Arduino

O coração da automação é o equilíbrio entre massa de ar e energia térmica. A lógica é **inversamente proporcional**:

- **Mais velocidade (mais ar)** → ar se mistura ao calor e dissipa → **temperatura de saída menor**
- **Menos velocidade (menos ar)** → ar permanece mais tempo em contato com superfícies quentes (riser a ~476°C) → **temperatura de saída maior**

| Componente | Função |
|:---|:---|
| **Arduino Nano** | Controlador central (leitura + PWM) |
| **Termopar Tipo-K + MAX6675** | Leitura em tempo real da temperatura (riser, vapor, plenum) |
| **MOSFET IRF520** | Módulo de potência para ajuste PWM da ventoinha |
| **Ventoinha automotiva 12V** | Impulsão de ar limpo para o plenum (pressão positiva) |

> [!WARNING]
> **Proteção do motor da ventoinha**: A hélice deve ficar a distância segura (>100mm) da junta cerâmica. Ela **sopra** ar para dentro do plenum (não suga), criando pressão positiva que empurra o ar quente pelos dutos — protegendo o motor de superaquecimento.

### 7.2 Especificações de Secagem

| Parâmetro | Valor |
|:---|:---|
| **Temperatura do ar de secagem** | 60–80°C (regulada por PWM) |
| **Vazão da ventoinha** | 50–120 L/min (variável) |
| **Câmara de secagem** | Tambor de 200L (reuso) |
| **Tempo de secagem (briquetes)** | ~4–6 horas |
| **Tempo de secagem (fibras finas)** | ~2–3 horas |

---

## 8. Escalabilidade — Relação T01 ↔ T02

| Característica | T01 (Artesanal) | T02 (Industrial) |
|:---|:---|:---|
| **Função primária** | Vapor + EP + secagem + água | Carvão ativado para filtros |
| **Câmara de combustão** | 16 L (briquetes) | 60–100 L (briquetes + lenha) |
| **Riser** | Ø 150mm × 600mm | Ø 250mm × 1200mm |
| **Serpentina** | 10 espiras (4,7 m inox) | 20 espiras (15,7 m inox) |
| **TEG** | 8 módulos (80–120 W) | 16 módulos (160–240 W) |
| **Retorta (RAI)** | Não possui | Sim — Ativação a 600–800°C |
| **Produção de EP** | 3–5 L/h | 10–15 L/h |
| **CAPEX estimado** | **R$ 12.850** | R$ 35.000–55.000 |
| **Replicabilidade** | **Alta** — construção comunitária | Média — requer soldagem técnica |

---

## 9. BoM Detalhada — Unidade T01 (Custo Amazônia)

> [!WARNING]
> **Markup Amazônia**: Os preços incluem sobrecusto logístico de **40–60%** sobre valores de centros produtores (Sul/Sudeste), conforme levantamento de mercado para a rota Manaus–Rio Branco. Materiais industrializados (inox, eletrônicos, TEGs) sofrem o maior impacto.

### Módulo 1 — Núcleo Térmico (Riser + Serpentina + Câmara)

| Cód | Item | Descrição | Qtd | Unid | Custo (R$) |
|:---|:---|:---|:---|:---|:---|
| 1.1 | Riser Inox 304 | Tubo Ø150mm × 600mm, esp. 2mm | 1 | Un | 480 |
| 1.2 | Serpentina Inox 304 | Tubo Ø15mm × 4,7m, 10 espiras, conformado | 1 | Un | 580 |
| 1.3 | Tijolos Refratários | Câmara de combustão ampliada + base | 35 | Un | 525 |
| 1.4 | Argamassa Refratária | Selagem de juntas e assentamento | 10 | kg | 180 |
| 1.5 | Grade de Cinzas | Aço galvanizado perfurado (base suspensa) | 1 | Un | 150 |
| 1.6 | Magazine de Briquetes | Duto inclinado 30° (alim. gravitacional) | 1 | Un | 120 |
| | **Subtotal Módulo 1** | | | | **2.035** |

### Módulo 2 — Carenagem e Isolamento

| Cód | Item | Descrição | Qtd | Unid | Custo (R$) |
|:---|:---|:---|:---|:---|:---|
| 2.1 | Carenagem Metálica | Tambor aço Ø~450mm, chapa 2,3mm (reuso industrial) | 1 | Un | 180 |
| 2.2 | Fibra Cerâmica 1260°C | Manta isolante 30mm (envolvente do riser) | 1 | m² | 280 |
| 2.3 | Lã de Rocha | Manta mineral 30mm (isolamento secundário) | 1,5 | m² | 240 |
| 2.4 | PU Vegetal + Cinzas | Camadas externas de isolamento complementar | 1 | Kit | 180 |
| 2.5 | Suportes e Fixação | Cantoneiras, parafusos, chapas de montagem | 1 | Kit | 150 |
| | **Subtotal Módulo 2** | | | | **1.030** |

### Módulo 3 — Geração Termoelétrica (TEG)

| Cód | Item | Descrição | Qtd | Unid | Custo (R$) |
|:---|:---|:---|:---|:---|:---|
| 3.1 | Módulos TEG | BiTe 40×40mm, 15W cada (importados) | 8 | Un | 960 |
| 3.2 | Dissipadores TEG | Alumínio anodizado (lado frio, 8 unidades) | 8 | Un | 240 |
| 3.3 | Pasta Térmica | Composto de interface (alta temperatura) | 1 | Un | 45 |
| 3.4 | Bateria Buffer | LiFePO4 12V/20Ah + proteção BMS | 1 | Un | 580 |
| 3.5 | Controlador de Carga | Regulador DC-DC (TEG → bateria) | 1 | Un | 220 |
| 3.6 | Fiação 12V | Cabos silicone alta temperatura + conectores | 1 | Kit | 120 |
| | **Subtotal Módulo 3** | | | | **2.165** |

### Módulo 4 — Condensação e Pirolenhoso

| Cód | Item | Descrição | Qtd | Unid | Custo (R$) |
|:---|:---|:---|:---|:---|:---|
| 4.1 | Chaminé Inox | Duto Ø100mm, saída 45° + descida 90° | 1 | Kit | 380 |
| 4.2 | Tambor Plenum 200L | Reuso (condensador gravitacional) | 1 | Un | 80 |
| 4.3 | Isolamento Plenum | Lã de rocha + PU vegetal (envolvente do tambor) | 1 | Kit | 180 |
| 4.4 | Serpentina Enterrada | PEAD Ø25mm × 20m + conexões + escavação | 1 | Kit | 350 |
| 4.5 | Bomba DC 12V | Circulação d'água plenum → serpentina enterrada | 1 | Un | 220 |
| 4.6 | Sifão Decantador | PVC + bombona PEAD 20L (coleta EP + alcatrão) | 1 | Kit | 120 |
| 4.7 | Duto Retorno Gases | Tubo p/ gases não-condensáveis → queimador | 1 | Un | 80 |
| | **Subtotal Módulo 4** | | | | **1.410** |

### Módulo 5 — Ventilação e Secagem (Plenum Limpo)

| Cód | Item | Descrição | Qtd | Unid | Custo (R$) |
|:---|:---|:---|:---|:---|:---|
| 5.1 | Ventoinha Automotiva | 12V (pressão positiva → plenum limpo) | 1 | Un | 180 |
| 5.2 | Dutos de Secagem | Aço galvanizado Ø100mm, 3m (plenum → câmara) | 3 | m | 210 |
| 5.3 | Tambor Secagem 200L | Reuso (câmara de secagem de fibras) | 1 | Un | 80 |
| | **Subtotal Módulo 5** | | | | **470** |

### Módulo 6 — Instrumentação, Segurança e Automação

| Cód | Item | Descrição | Qtd | Unid | Custo (R$) |
|:---|:---|:---|:---|:---|:---|
| 6.1 | Termopares Tipo-K | Sondas (riser + vapor + plenum) + MAX6675 | 3 | Kit | 420 |
| 6.2 | Arduino Nano | Controlador PWM + leitura de sensores | 1 | Un | 80 |
| 6.3 | MOSFET IRF520 | Módulo de potência (controle ventoinha) | 1 | Un | 25 |
| 6.4 | Display LCD/OLED | Indicador de temperatura | 1 | Un | 60 |
| 6.5 | Válvula Solenoide 12V | Controle de fluxo d'água (serpentina vapor) | 1 | Un | 120 |
| 6.6 | Manômetro | Pressão do plenum (0–4 bar, glicerinado) | 1 | Un | 150 |
| 6.7 | Válvula de Alívio | Segurança do circuito de vapor (0,5 barg) | 1 | Un | 180 |
| 6.8 | LED + Fiação | Iluminação 12V do posto de trabalho | 1 | Kit | 120 |
| 6.9 | Extintor ABC 2kg | Segurança contra incêndio | 1 | Un | 120 |
| | **Subtotal Módulo 6** | | | | **1.275** |

### Módulo 7 — Montagem e Logística

| Cód | Item | Descrição | Qtd | Unid | Custo (R$) |
|:---|:---|:---|:---|:---|:---|
| 7.1 | Frete Amazônia | Transporte de componentes (São Paulo → Rio Branco) | 1 | Vb | 1.800 |
| 7.2 | Consumíveis | Solda, vedantes, fita alta temp., abraçadeiras | 1 | Kit | 350 |
| 7.3 | Mão de obra | Montagem (2 dias, 2 técnicos, inclui treinamento) | 1 | Vb | 2.000 |
| 7.4 | Tanque Elevado 50L | Reservatório de água p/ alimentação gravitacional | 1 | Un | 120 |
| 7.5 | Base/Estrutura | Perfis de aço para suporte elevado do forno | 1 | Kit | 200 |
| | **Subtotal Módulo 7** | | | | **4.470** |

---

### Resumo Financeiro — T01 Completo

| Módulo | CAPEX (R$) |
|:---|:---|
| 1. Núcleo Térmico (Riser + Serpentina + Câmara) | 2.035 |
| 2. Carenagem e Isolamento | 1.030 |
| 3. Geração Termoelétrica (TEG) | 2.165 |
| 4. Condensação e Pirolenhoso | 1.410 |
| 5. Ventilação e Secagem | 470 |
| 6. Instrumentação, Segurança e Automação | 1.275 |
| 7. Montagem e Logística | 4.470 |
| **TOTAL** | **12.855** |

> [!IMPORTANT]
> **Custo por unidade replicável (CIF Rio Branco): R$ 12.855**. Uma rede de 10 unidades T01 distribuídas em comunidades custa **R$ 128.550** — incluindo frete, montagem e treinamento. Valor equivalente a **~55%** de uma única unidade T02 industrial (R$ 35.000–55.000), mas com **10× mais pontos de impacto comunitário**.

---

## 10. Aplicações Comunitárias (Multiplicação)

Cada unidade T01 instalada em um ponto comunitário confere autonomia em:

| Serviço | Mecanismo T01 | Impacto |
|:---|:---|:---|
| **Tratamento de bambu** | Vapor (serpentina) + EP (condensado) | Elimina autoclave e produtos químicos |
| **Purificação de água** | Circuito secundário pela serpentina (pasteurização >75°C) | 20 L/h de água segura para 20–30 pessoas |
| **Iluminação e IoT** | TEGs (80–120W) + bateria buffer | Posto de trabalho autônomo |
| **Secagem de produtos** | Ar quente (plenum + soprador) | Fibras, castanha, açaí, farinha |
| **Defensivo agrícola** | Extrato pirolenhoso (3–5 L/h) | Substituição de agrotóxicos |
| **Biochar** | Resíduos carbonizados na retorta | Correção de solo + créditos de carbono |

---

## Documentos Relacionados

- <img src="../../../../assets/icons/human_17_black.svg" width="18px"> **[T02 — Reator de Biorrefinaria Industrial](../T02_REATOR_BIORREFINARIA/ENG-MEM-T02_BIORREFINARIA-REATOR.md)**: Versão industrial com RAI para carvão ativado.
- <img src="../../../../assets/icons/human_20_black.svg" width="18px"> **[Memorial Mestre: Coração Térmico](../../ENG-MEM-MASTER_CORACAO-TERMICO.md)**: Arquitetura unificada de cascateamento térmico.
- <img src="../../../../assets/icons/human_09_black.svg" width="18px"> **[NT-002: Comparativo Fornos e Reatores](ENG-NT-002_COMPARATIVO-FORNOS-REATORES.md)**: Estudo comparativo com padrões industriais.

## Como Citar

**APA:**
Takwara, F. R. (2026). *Memorial Técnico: Forno Ecológico T01 — Unidade Comunitária Replicável* (Versão 2.0). Projeto Mulheres Que Tecem a Floresta / Consórcio UnB/UFRR/UFAC. https://doi.org/10.5281/zenodo.18827106

---
<p align='center'><img src='../../../../assets/logo_BQTF/logo_mqtf_soberana.svg' width='45px'><br><b>Mulheres Que Tecem a Floresta — MQTF</b><br><i>"Soberania não se pede, se exerce."</i></p>