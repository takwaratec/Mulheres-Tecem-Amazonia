---
projeto: Mulheres Que Tecem a Floresta
instituicao: Consórcio UnB / UFRR / UFAC
tipo: Documentação Técnica
referencia: NT-003_ALINHAMENTO-ORCAMENTARIO-T01.md
status: Em Revisão
---

<p align="right"><i>"O espaço geográfico é o encontro de objetos e ações."<br>— Milton Santos</i></p>

### <img src="../../assets/patterns/square_05_cyan.svg" width="22px">&nbsp; Ficha Técnica e Metadados
*   **Projeto**: Mulheres Que Tecem a Floresta (MQTF)
*   **Instituição**: Consórcio UnB / UFRR / UFAC
*   **Referência**: NT-003_ALINHAMENTO-ORCAMENTARIO-T01.md
*   **Status**: Em Revisão

![Status: Em Revisão](https://img.shields.io/badge/Status-Em_Revisão-yellow)

# <img src="../../assets/patterns/square_title_red.svg" width="30px"> Nota Técnica NT-003: Alinhamento Orçamentário — T01 Biorrefinaria e Implantação dos Hubs N2

---

## <img src="../../assets/patterns/square_01_red.svg" width="22px"> 1. Objeto

Esta Nota Técnica justifica e detalha o **CAPEX unitário revisado** da unidade T01 (Forno Ecológico / Biorrefinaria de Pequeno Porte) em **R$ 12.855,00** (CIF Rio Branco), bem como os custos adicionais de implantação nos novos Hubs N2 de **Manaus (AM)** e **Porto Velho (RO)**.

---

## <img src="../../assets/patterns/square_03_black.svg" width="22px"> 2. Composição do CAPEX Unitário — T01

O valor anterior (pré-revisão) de ~R$ 4.000,00 foi reavaliado após a inclusão de itens críticos de segurança, automação e isolamento, além do **Markup Amazônia** (logística remota e fornecedores regionais).

### 2.1. Bill of Materials (BoM) Revisada — T01 Unitário

| Grupo | Item | Qtd | Custo Unit (R$) | Subtotal (R$) |
| :--- | :--- | :---: | ---: | ---: |
| **Câmara de Combustão** | Riser em aço carbono (∅200mm, h=800mm, e=3mm) | 1 | 420,00 | 420,00 |
| | Câmara de combustão ampliada (briquetes) | 1 | 380,00 | 380,00 |
| | Grelha de cinzas em aço inox | 1 | 180,00 | 180,00 |
| **Serpentina** | Serpentina escalonada inox (∅15mm, 6 espiras) | 1 | 1.200,00 | 1.200,00 |
| | Conexões hidráulicas inox (luvas, niples, cotovelos) | 1 kit | 350,00 | 350,00 |
| **TEG (Termoelétrico)** | Módulos Peltier/TEG (SP1848-27145) | 4 | 85,00 | 340,00 |
| | Dissipadores de calor + pasta térmica | 4 | 45,00 | 180,00 |
| | Controlador de carga / regulador DC-DC | 1 | 120,00 | 120,00 |
| **Automação** | Arduino Nano + sensor DS18B20 (temperatura) | 1 | 95,00 | 95,00 |
| | PWM + ventilador (tiragem forçada) | 1 | 150,00 | 150,00 |
| | Válvula solenóide (água, ∅½") | 1 | 280,00 | 280,00 |
| | Manômetro analógico (0–6 bar) | 1 | 120,00 | 120,00 |
| **Isolamento e Carenagem** | Fibra cerâmica (manta 30mm, 1m²) | 2 | 320,00 | 640,00 |
| | Carenagem externa (tambor metálico recortado, e=2,3mm) | 1 | 450,00 | 450,00 |
| | Lã de rocha (placa 50mm) | 1 | 180,00 | 180,00 |
| | PU vegetal expansivo (1kg) | 2 | 95,00 | 190,00 |
| | Cinzas (subproduto — custo zero) | — | 0,00 | 0,00 |
| **Plenum / Condensação** | Tambor PEAD 200L (plenum de resfriamento) | 1 | 350,00 | 350,00 |
| | Bomba d'água submersa (12V, 800L/h) | 1 | 180,00 | 180,00 |
| | Serpentina enterrada (cobre ∅15mm, 10m) | 1 | 480,00 | 480,00 |
| | Tubulação PVC/CPVC (conexões) | 1 kit | 120,00 | 120,00 |
| **Segurança** | Válvula de alívio de pressão (½") | 1 | 220,00 | 220,00 |
| | Extintor ABC 4kg | 1 | 150,00 | 150,00 |
| | Luvas e proteção térmica (kit) | 1 | 120,00 | 120,00 |
| **Base e Estrutura** | Base suspensa em metalon (recebimento de chama) | 1 | 350,00 | 350,00 |
| | Chaminé inox (∅100mm, h=2m) | 1 | 280,00 | 280,00 |
| **Markup Amazônia** | Frete CIF Rio Branco + embalagem reforçada | 1 | 1.800,00 | 1.800,00 |
| | Margem de contingência (10%) | 1 | — | 930,00 |
| | | | **SUBTOTAL REATOR (núcleo)** | **~12.855,00** |

### 2.2. Câmaras de Tratamento (componente integral do T01)

As câmaras de tratamento são **parte integrante** da unidade T01 — não infraestrutura avulsa. O material das câmaras varia conforme a cadeia produtiva do núcleo:

| Variante | Câmaras | Material | Aplicação | Custo Câmaras (R$) |
| :--- | :---: | :--- | :--- | ---: |
| **T01-B** | 4× 200L | PEAD (Polietileno de Alta Densidade) | Tratamento de bambu (vapor + pirolenhoso) | 2.145,00 |
| **T01-A** | 4× 200L | Inox 304 (food-grade) | Beneficiamento de alimentos (açaí, castanha, polpas) | 7.145,00 |
| **T01-D** | 4× PEAD + 4× Inox | Dual (PEAD + Inox 304) | Cadeias duplas: bambu + alimentos | 9.145,00 |

#### Detalhamento das Câmaras

| Item | Descrição | T01-B (R$) | T01-A (R$) | T01-D (R$) |
| :--- | :--- | ---: | ---: | ---: |
| Câmaras horizontais 200L (PEAD) | Tratamento com vapor/pirolenhoso — bambu | 1.400,00 | — | 1.400,00 |
| Câmaras horizontais 200L (Inox 304) | Beneficiamento food-grade — alimentos | — | 5.600,00 | 5.600,00 |
| Tubulação e conexões (PEAD ou Inox) | Manifold de vapor + drenos | 400,00 | 800,00 | 1.200,00 |
| Markup proporcional (frete + contingência) | | 345,00 | 745,00 | 945,00 |
| **Subtotal Câmaras** | | **2.145,00** | **7.145,00** | **9.145,00** |

### 2.3. Custo Total por Variante T01

| Variante | Composição | CAPEX Unitário (R$) | Quando usar |
| :--- | :--- | ---: | :--- |
| **T01-B** | Reator + 4× Câmaras PEAD | **15.000,00** | Hub com cadeia exclusiva de bambu (tratamento, construção naval) |
| **T01-A** | Reator + 4× Câmaras Inox 304 | **20.000,00** | Hub com cadeia exclusiva de alimentos (açaí, castanha, polpas) |
| **T01-D** | Reator + 4× PEAD + 4× Inox | **22.000,00** | Hub com dualidade de cadeias (bambu + alimentos) |

> [!IMPORTANT]
> O "Markup Amazônia" (frete + contingência) aplica-se proporcionalmente ao kit de câmaras, assim como ao núcleo do reator.
> O custo de mão de obra de montagem **não está incluído** — será absorvido pelo canteiro-escola (formação remunerada).

---

## <img src="../../assets/patterns/square_04_black.svg" width="22px"> 3. Impacto no Inventário Mecânico (ENG-MEM-010)

| Item | Antes | Variante B | Variante A | Variante D |
| :--- | ---: | ---: | ---: | ---: |
| T01 Unitário (s/ câmaras) | ~R$ 4.000 | — | — | — |
| T01 Unitário (revisado, núcleo) | — | **R$ 12.855** | **R$ 12.855** | **R$ 12.855** |
| Kit Câmaras | — | R$ 2.145 | R$ 7.145 | R$ 9.145 |
| **T01 Completo (unitário)** | — | **R$ 15.000** | **R$ 20.000** | **R$ 22.000** |

> [!NOTE]
> A atribuição da variante é definida pela função do núcleo (ver ANEXO_VI §3.2):
> - **T01-B** (PEAD): Cruzeiro do Sul (Polo Naval), Porto Velho, Boa Vista — cadeia de bambu
> - **T01-D** (Dual): Mâncio Lima — bambu + beneficiamento de açaí/castanha
> - A sede N1 (Rio Branco) opera com inventário completo T01–T08 (ver `ENG-MEM-010`).

---

## <img src="../../assets/patterns/square_05_red.svg" width="22px"> 4. Adendo: Custos de Implantação dos Hubs N2

### 4.1. Hub Manaus (AM) — Domo Voador 10m

| Item | Estimativa (R$) | Observação |
| :--- | ---: | :--- |
| Domo Geodésico 10m (estrutura + cobertura) | 45.000,00 | Kit pré-fabricado, montagem in loco |
| Transporte e logística (Frete → AM) | 8.000,00 | Rodoviário + balsa |
| Base de concreto / plataforma nivelada | 12.000,00 | Depende do terreno cedido pelo parceiro |
| Instalação elétrica (iluminação + painéis solar) | 15.000,00 | Autonomia energética parcial |
| Mobiliário expositivo e sinalização | 10.000,00 | Vitrines, banners, totens |
| **Subtotal Manaus** | **90.000,00** | **Contrapartida parceiro: espaço + segurança** |

### 4.2. Hub Porto Velho (RO) — Apoio Técnico e Artesanal

| Item | Estimativa (R$) | Observação |
| :--- | ---: | :--- |
| T01 Biorrefinaria (1 unidade) | 12.855,00 | Instalação demonstrativa + capacitação |
| Adaptação do espaço (bancadas, piso, exaustão) | 18.000,00 | Adequação do galpão cedido |
| Ferramental de artesanato (bancadas, furadeiras, lixadeiras) | 8.000,00 | Kit básico para biojoias |
| Conectividade Starlink (1 ano) | 4.800,00 | R$ 400/mês — plataforma EcoSol |
| Mobiliário e EPIs | 6.000,00 | Cadeiras ergonômicas, luvas, óculos |
| **Subtotal Porto Velho** | **49.655,00** | **Contrapartida parceiro: espaço + água/luz** |

### 4.3. Resumo de Investimento Adicional (Hubs N2)

| Hub | CAPEX Adicional (R$) |
| :--- | ---: |
| Manaus (AM) — Domo Voador | 90.000,00 |
| Porto Velho (RO) — Apoio Técnico | 49.655,00 |
| **Total N2 (AM + RO)** | **139.655,00** |

> [!WARNING]
> Este investimento adicional deverá ser contemplado como **adendo orçamentário** ao Componente 2 (Bioconstrução e Biorrefinaria) do dossiê BNDES, ou absorvido pela rubrica de "Infraestrutura e Instalações" já prevista no Memorando de Orçamento Consolidado (GOV_memorando-orcamento-consolidado.md).

---

## <img src="../../assets/patterns/square_06_black.svg" width="22px"> 5. Recomendações

1. **Integrar** os valores desta NT ao Memorando de Orçamento Consolidado (`GOV_memorando-orcamento-consolidado`), rubrica de CAPEX.
2. **Vincular** a implantação dos Hubs N2 ao cronograma de adesão dos parceiros (Plano de Atuação `PLAN-ATUACAO-POLOS-N2.md`).
3. **Registrar** o aceite de contrapartida dos parceiros como ativo de contrapartida econômica (valoração de ativos — § 3.1 do Memorando de Orçamento).

---
<p align='center'><img src='../../assets/logo_BQTF/logo_mqtf_soberana.svg' width='45px'><br><b>Mulheres Que Tecem a Floresta — MQTF</b><br><i>"Soberania não se pede, se exerce."</i></p>