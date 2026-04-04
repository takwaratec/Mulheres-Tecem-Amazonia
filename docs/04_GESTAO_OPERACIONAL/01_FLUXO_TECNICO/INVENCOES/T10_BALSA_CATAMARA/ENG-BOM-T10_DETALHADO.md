---
projeto: Mulheres Que Tecem a Floresta
instituicao: Consórcio UnB / UFRR / UFAC
tipo: Documentação Técnica
referencia: ENG-BOM-T10_DETALHADO.md
status: Consolidado
---

<p align="right"><i>"O Brasil, última nação a abrogar a escravidão, tem um compromisso terrível com o seu povo."<br>— Darcy Ribeiro</i></p>

### <img src="../../../../assets/patterns/square_05_red.svg" width="22px">&nbsp; Ficha Técnica e Metadados
*   **Projeto**: Mulheres Que Tecem a Floresta (MQTF)
*   **Instituição**: Consórcio UnB / UFRR / UFAC
*   **Referência**: ENG-BOM-T10_DETALHADO.md
*   **Status**: Consolidado

![Status: Consolidado](https://img.shields.io/badge/Status-Consolidado-brightgreen)

# <img src="../../../../assets/patterns/square_title_red.svg" width="30px"> BoM: Catamarã Utilitário Solar MQTF (Fase 1)

Este documento detalha o Bill of Materials para a construção do Catamarã Utilitário de **12,0 metros**, equipado com **propulsão dupla** (2 × 60 HP elétricos) para operação intercalada ou combinada, otimizado para logística de Unidades BSM e escoamento refrigerado via energia solar.

---

## <img src="../../../../assets/patterns/square_01_red.svg" width="22px"> Premissa de Dimensionamento Solar

### Geometria do Teto e Captação

| Parâmetro | Valor | Observação |
|:---|:---|:---|
| **Área útil do teto** | 10,0 m × 4,0 m = **40 m²** | Descontados recuos de proa (1m) e popa (1m), laterais (0,4m cada). |
| **Painel unitário (450W mono)** | 2,10 m × 1,04 m = **2,18 m²** | Dimensão comercial padrão. |
| **Layout de teto** | 4 colunas × 4 fileiras (retrato) | Largura: 4 × 1,04 = 4,16 m ✓ / Comprimento: 4 × 2,10 = 8,40 m ✓ |
| **Total de painéis** | **16 unidades** | 16 × 450W = **7,2 kWp** instalados. |

### Irradiância Solar na Região-Alvo (Atlas INPE/LABREN)

**Fonte de dados**: Atlas Brasileiro de Energia Solar, 2ª edição (INPE/LABREN, período 1999–2019). Consulta SunData/CRESESB para coordenadas de Cruzeiro do Sul (7° 37′ S, 72° 40′ O).

A irradiação global horizontal (GHI) na região do Alto Juruá apresenta a seguinte **variação sazonal**:

| Período | Meses | GHI Média (kWh/m²·dia) | Característica Climática |
|:---|:---|:---|:---|
| **Verão amazônico** (seca) | Mai–Out | **5,2 a 5,8** | Céu limpo, baixa nebulosidade, menor pluviosidade. |
| **Inverno amazônico** (chuvas) | Nov–Abr | **3,8 a 4,5** | Alta nebulosidade convectiva (cumulonimbus), picos de radiação difusa. |
| **Média anual** | Jan–Dez | **5,0** | Valor de referência (LABREN/INPE, longo prazo). |
| **Pior mês (referência)** | Fevereiro | **~3,8** | Cenário crítico para dimensionamento conservador. |

> [!WARNING]
> **Decisão de projeto**: O dimensionamento deve utilizar o **pior mês** (3,8 kWh/m²·dia) como referência de segurança, não a média anual. Nos meses de verão, o excedente de geração recarga completamente as baterias e permite jornadas mais longas.

### Balanço Energético — Cenários Real e Conservador

| Variável | Cenário Médio Anual | Cenário Crítico (Pior Mês) |
|:---|:---|:---|
| **GHI** | 5,0 kWh/m²·dia | 3,8 kWh/m²·dia |
| **Performance Ratio (PR)** | 0,75 | 0,75 |
| **Geração solar efetiva** | 7,2 × 5,0 × 0,75 = **27,0 kWh/dia** | 7,2 × 3,8 × 0,75 = **20,5 kWh/dia** |
| **Banco de baterias (2 × LiFePO4 48V/400Ah)** | 38,4 kWh nominal | 38,4 kWh nominal |
| **Energia utilizável (80% DoD)** | 30,7 kWh | 30,7 kWh |
| **Orçamento energético total/dia** | 27,0 + 30,7 = **57,7 kWh/dia** | 20,5 + 30,7 = **51,2 kWh/dia** |

> [!IMPORTANT]
> O **Performance Ratio (PR) de 0,75** desconta perdas reais: temperatura dos módulos (~35°C na Amazônia reduz eficiência em ~10%), sujidade (poeira, material orgânico), perdas em cabos, eficiência do MPPT e do inversor. É o fator padrão utilizado pela indústria para sistemas off-grid tropicais.

### Autonomia por Modo de Operação (com PR corrigido)

| Modo | Potência de Cruzeiro | Autonomia (Média Anual) | Autonomia (Pior Mês) | Cenário de Uso |
|:---|:---|:---|:---|:---|
| **Intercalado** (1 motor) | ~13 kW | **≈ 4,0 h** | **≈ 3,5 h** | Navegação de rotina, escoamento leve. |
| **Carga Total** (2 motores) | ~27 kW | **≈ 1,9 h** | **≈ 1,6 h** | Transporte BSM, manobra em correnteza forte. |
| **Misto** (30 min carga + 3h intercalado) | — | **≈ 3,5 h** | **≈ 3,0 h** | Partida carregado + cruzeiro de entrega. |
| **Câmara fria (24h)** | 0,25 kW | **6,0 kWh/dia** | **6,0 kWh/dia** | Cadeia de frio ininterrupta. |

> [!NOTE]
> A velocidade de cruzeiro estimada é de **6 a 8 nós** (11–15 km/h) em regime de deslocamento. A operação de dois motores permite **propulsão diferencial** (manobra de precisão em rios sinuosos) além de redundância de segurança. No pior mês, a jornada é reduzida mas continua operacional para rotas curtas típicas do Alto Juruá (15–40 km entre comunidades).

### Fornecedores na Cadeia Manaus–Rio Branco–Cruzeiro do Sul

| Fornecedor | Localização | Perfil | Observação |
|:---|:---|:---|:---|
| **BRX Solar** | Manaus (AM) | Distribuidora atacado | Logística própria com entrega em Manaus. Parceria com integradores, suporte técnico. |
| **Amazon Solar** | Manaus (AM) | Integrador + kits off-grid | Kits fotovoltaicos completos e serviços de instalação de sistemas renováveis. |
| **InfinitySun Energia Solar** | Manaus (AM) | Projetos off-grid de variados portes | Experiência em aplicações residenciais, industriais e rurais. |
| **Megatron Energia Solar** | Manaus (AM) | Projetos rurais e urbanos | Histórico de projetos em áreas remotas no estado do Amazonas. |
| **SISA Solar** | Rio Branco (AC) | Integrador regional Acre | Atuação direta na capital do Acre — ponto logístico mais próximo do Alto Juruá. |

> [!TIP]
> **Rota de suprimento recomendada**: Manaus (distribuidora BRX Solar) → **frete fluvial** até Cruzeiro do Sul (R$ 610/trecho, 7–12 dias) → montagem no Canteiro Escola. A opção rodoviária via BR-364 (Rio Branco → Cruzeiro do Sul) é viável nos meses de seca, mas sujeita a interrupções sazonais. A SISA Solar (Rio Branco) pode servir como ponto intermediário de apoio técnico.

---

## <img src="../../../../assets/patterns/square_02_black.svg" width="22px"> 1. Módulos de Flutuação e Convés (Bio-Estrutural)

| Cód | Item | Descrição Técnica | Qtd | Unid | Custo Est. (R$) | Valuation (1.4x) |
|:---|:---|:---|:---|:---|:---|:---|
| 1.1 | Bambu Guadua | Colmos *weberbaueri* termorretificados | 800 | Un | 12.000 | 16.800 |
| 1.2 | Mamonex RD70 | PU Vegetal Expansivo (Dens. 70 kg/m³) | 450 | kg | 11.250 | 15.750 |
| 1.3 | Selante MQTF | Impermeabilizante bio-epóxi | 80 | kg | 4.800 | 6.720 |
| 1.4 | Travessas + Esteira | Colmos inteiros + esteira contínua de ripas de bambu | 1 | Kit | 6.500 | 9.100 |
| 1.5 | Areia/PU Antiderrap. | Camada de areia + PU para áreas de circulação | 40 | m² | 2.000 | 2.800 |
| 1.6 | Treliças de Cobertura | Bambu *Guadua*, tipo Warren, vão 4,8m (4 un) | 4 | Un | 2.800 | 3.920 |
| 1.7 | Muratas de Contra Sol | PU + bambu + fibras/areia, laterais (2 × 12m) | 1 | Kit | 3.500 | 4.900 |
| 1.8 | Guarda-Corpo | Bambu laminado resinado, h=1,0m, perím. ~30m | 1 | Kit | 3.500 | 4.900 |
| 1.9 | Porcas Olhal | Aço galv. M12, ancoragem/içamento, malha 3×3m | 15 | Un | 450 | 630 |
| **Subtotal** | | | | | **46.800** | **65.520** |

---

## <img src="../../../../assets/patterns/square_03_black.svg" width="22px"> 2. Propulsão Solar Dupla e Armazenamento (Fase 1)

| Cód | Item | Descrição Técnica | Qtd | Unid | Custo Est. (R$) | Valuation (1.4x) |
|:---|:---|:---|:---|:---|:---|:---|
| 2.1 | Painéis Fotov. | Monocristalinos 450W (Teto Plano 4×4) | 16 | Un | 20.800 | 29.120 |
| 2.2 | Banco Baterias | LiFePO4 48V / 400Ah (2 bancos) | 2 | Kit | 56.000 | 78.400 |
| 2.3 | Inversor Solar | Híbrido 10kW (Náutico/Offgrid) | 1 | Un | 13.000 | 18.200 |
| 2.4 | Motores Elétricos | Fora de borda 60hp equiv. (15kW cada) | 2 | Un | 36.000 | 50.400 |
| 2.5 | Controlador Carga | MPPT 150/100 (2 strings sincronizadas) | 2 | Un | 6.400 | 8.960 |
| 2.6 | Sistema de Pilotagem | Joystick prop. diferencial + display + CAN bus | 1 | Kit | 4.500 | 6.300 |
| **Subtotal** | | | | | **136.700** | **191.380** |

---

## <img src="../../../../assets/patterns/square_04_black.svg" width="22px"> 3. Câmara Fria e Logística Social

### 3.0 Dimensionamento da Câmara Fria (Sob Convés)

A câmara fria é instalada **entre os cascos, sob o convés** — zona protegida da irradiação solar direta. O isolamento utiliza o mesmo PU vegetal do casco (Mamonex RD70), integrando a câmara à arquitetura naval.

| Parâmetro | Dimensão |
|:---|:---|
| **Envelope externo** | 3,0 m × 1,8 m × 1,2 m |
| **Isolamento (Mamonex RD70, 100mm)** | λ = 0,025 W/m·K |
| **Volume interno líquido** | 2,6 m × 1,4 m × 0,8 m = **2,9 m³** (2.900 litros) |

**Configuração Bipartida:**

| Compartimento | Temperatura | Volume | Capacidade (60% preench.) | Produtos-Alvo |
|:---|:---|:---|:---|:---|
| **A — Refrigerado** | 0 a 5°C | 1,8 m³ | ~1.080 kg | Polpas de açaí, pescado, laticínios, medicamentos |
| **B — Resfriado** | 10 a 15°C | 1,1 m³ | ~660 kg | Frutas inteiras, legumes, doces, artesanato perecível |
| **Total** | — | **2,9 m³** | **~1.740 kg** | — |

**Balanço Térmico:**

| Variável | Valor |
|:---|:---|
| ΔT máximo (35°C ambiente → 5°C interno) | 30°C |
| Área de superfície | 22,32 m² |
| Fluxo térmico (paredes) | (0,025 ÷ 0,10) × 22,32 × 30 = **167 W** |
| Perdas por abertura + carga de produto | +83 W (fator de segurança 50%) |
| **Carga térmica total** | **250 W** contínuos |
| **Consumo diário** | 250W × 24h = **6,0 kWh/dia** (9% do orçamento solar) |

### 3.1 Itens de BoM — Câmara Fria e Logística

| Cód | Item | Descrição Técnica | Qtd | Unid | Custo Est. (R$) | Valuation (1.4x) |
|:---|:---|:---|:---|:---|:---|:---|
| 3.1 | Câmaras Frias Distrib. | Moldadas no casco (PU+bambu+fibras), banco-convés | 8 | Un | 8.500 | 11.900 |
| 3.2 | Condensadores Submersos | Unidades condensadoras 48V embutidas no casco inferior | 2 | Un | 5.500 | 7.700 |
| 3.3 | BSM Fixa de Bordo | Unidade BSM permanente (popa-BB), compostagem seca | 1 | Un | 3.500 | 4.900 |
| 3.4 | Redário Estrut. | Pontos de ancoragem + redes de descanso bio | 12 | Kit | 4.800 | 6.720 |
| 3.5 | Kit BSM Handl. | Trilhos e travas para módulos BSM (4 posições) | 4 | Un | 6.500 | 9.100 |
| 3.6 | Mobiliário Aux. | Cozinha de bordo / Apoio social | 1 | Kit | 5.000 | 7.000 |
| 3.7 | Termômetros IoT | Monitoramento contínuo de temperatura (A+B) | 2 | Un | 1.200 | 1.680 |
| **Subtotal** | | | | | **35.000** | **49.000** |

> [!NOTE]
> **Protocolo operacional:** Os produtos devem ser **pré-resfriados** no ponto de embarque em terra antes do carregamento, reduzindo a carga térmica inicial e otimizando o consumo energético durante a navegação. Na ancoragem (4–6h diurnas), os painéis alimentam exclusivamente a câmara fria sem consumo de propulsão.

---

## <img src="../../../../assets/patterns/square_06_black.svg" width="22px"> 4. Instrumentação e Navegação

| Cód | Item | Descrição Técnica | Qtd | Unid | Custo Est. (R$) | Valuation (1.4x) |
|:---|:---|:---|:---|:---|:---|:---|
| 4.1 | Monitoramento | IoT / Nível de baterias / GPS / nível tanque água | 1 | Kit | 4.500 | 6.300 |
| 4.2 | Iluminação LED | Eficiência A (Ambiental + Sinalização naval) | 1 | Kit | 2.800 | 3.920 |
| 4.3 | Boias Salva-vidas | Circular c/ retinida flutuante (NORMAM-02) | 2 | Un | 600 | 840 |
| 4.4 | Coletes Salva-vidas | Homologados Marinha (8 pessoas) | 8 | Un | 1.600 | 2.240 |
| 4.5 | Flutuadores Emerg. | Rolos espuma PU, compartimentos sob teto | 4 | Un | 800 | 1.120 |
| 4.6 | Extintor + Kit Med. | CO2/pó químico + primeiros socorros | 1 | Kit | 500 | 700 |
| **Subtotal** | | | | | **10.800** | **15.120** |

---

## <img src="../../../../assets/patterns/square_07_black.svg" width="22px"> 5. Captação de Água e Potabilização

| Cód | Item | Descrição Técnica | Qtd | Unid | Custo Est. (R$) | Valuation (1.4x) |
|:---|:---|:---|:---|:---|:---|:---|
| 5.1 | Calhas + Condutores | Bambu laminado resinado (2×12m) + descidas | 1 | Kit | 1.800 | 2.520 |
| 5.2 | First-Flush Diverter | Válvula gravitacional (descarte 80L) | 1 | Un | 800 | 1.120 |
| 5.3 | Tanque PU 500L | Moldado no casco (Mamonex RD70) + indicador IoT | 1 | Un | 1.500 | 2.100 |
| 5.4 | Filtro Sedimentos | Filtro-bolsa lavável (>50 μm) | 2 | Un | 400 | 560 |
| 5.5 | Carvão Ativado | Cartucho 10″ de coco babaçu (troca trimestral) | 4 | Un | 600 | 840 |
| 5.6 | Esterilizador UV-C | Lâmpada 12W solar (0,3 kWh/dia) | 1 | Un | 1.200 | 1.680 |
| 5.7 | Tubulação + Registro | PVC recicl. / bambu + torneira de convés | 1 | Kit | 500 | 700 |
| **Subtotal** | | | | | **6.800** | **9.520** |

> [!NOTE]
> **Autonomia hídrica**: O sistema garante **70 L/dia** para 4 tripulantes + BSM fixa em todos os meses do ano. No período chuvoso, o excedente (~200 L/dia) permite reabastecimento de comunidades visitadas.

---

## <img src="../../../../assets/patterns/square_05_red.svg" width="22px"> Resumo Financeiro — Catamarã T10 Solar (Fase 1 / Propulsão Dupla)

| Módulo | CAPEX (R$) | Valuation 1.4x (R$) |
|:---|:---|:---|
| 1. Bio-Estrutural (Casco + Treliças + Muratas + Guarda-corpo) | 46.800 | 65.520 |
| 2. Propulsão Solar Dupla + Pilotagem | 136.700 | 191.380 |
| 3. Câmaras Frias Distrib., BSM Fixa e Logística | 35.000 | 49.000 |
| 4. Instrumentação e Segurança (NORMAM-02) | 10.800 | 15.120 |
| 5. Captação de Água e Potabilização | 6.800 | 9.520 |
| **TOTAL** | **236.100** | **330.540** |

> [!IMPORTANT]
> **Soberania Energética e Hídrica**: Custo operacional de combustível fóssil: **R$ 0,00**. Custo de água potável: **R$ 0,00**. O T10 é autossuficiente em energia e água, com autonomia de 5–7 dias sem reabastecimento.

---
<p align='center'><img src='../../../../assets/logo_BQTF/logo_mqtf_soberana.svg' width='45px'><br><b>Mulheres Que Tecem a Floresta — MQTF</b><br><i>"Soberania não se pede, se exerce."</i></p>