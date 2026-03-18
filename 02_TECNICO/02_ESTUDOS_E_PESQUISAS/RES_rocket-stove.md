---
status: Pesquisa Ativa
colecao: 02_PESQUISA_DESENVOLVIMENTO
autor: Institucional Tec (via Antigravity AI)
versao: 5.1
licenca: CC BY-NC 4.0
---

# Nota Técnica: Otimização de Rocket Stoves para Biorrefinarias Artesanais

## 1. Introdução e Contexto
Esta nota técnica consolida os parâmetros fundamentais para o desenvolvimento de unidades de combustão de alta eficiência (Rocket Stoves) destinadas ao processamento de biomassa em biorrefinarias artesanais. O conteúdo baseia-se em análise de dinâmica de fluidos computacional (CFD) para superação das limitações térmicas de fogões tradicionais.

## 2. Especificações do Protótipo Base (Baseline)
O estudo de referência utilizou um fogão com as seguintes características construtivas:
- **Material**: Aço com espessura de 2.3 mm.
- **Peso**: 3 kg.
- **Dimensões**: 30 x 28 x 60 cm.
- **Configuração**: Geometria em "L" (L-elbow) com chaminé inclinada para alimentação de lenha.

## 3. Parâmetros de Otimização e Resultados
A principal inovação técnica reside na aplicação de isolamento térmico e no refinamento da geometria de saída (pot skirt).

### 3.1 Isolamento Térmico
- **Material Selecionado**: Fibra Cerâmica (superior à lã de vidro e poliuretano em condutividade e custo-benefício).
- **Espessura**: 30 mm, aplicada ao redor da câmara de combustão externa.
- **Impacto**: A adição do isolamento permitiu que o calor fosse concentrado no fluxo ascendente, reduzindo perdas radiais.

### 3.2 Desempenho Térmico (Simulação CFD)
As medições de temperatura mostraram um salto significativo de eficiência:

| Local de Medição | Antes (Sem Isolamento) | Depois (Com Isolamento/Ajustes) |
| :--- | :---: | :---: |
| Área de Combustão | 493.06°C | 525.68°C |
| Chaminé Inferior | 411.48°C | 468.61°C |
| Chaminé Central | 408.35°C | 469.13°C |
| Chaminé Superior | 417.82°C | 476.25°C |
| **Saída (Sob a panela)** | **374.91°C** | **452.94°C** |

**Eficiência Geral**: O ganho de desempenho térmico na interface de trabalho (saída/panela) foi de **11.15%**.

## 4. Diretrizes para Construção (Protocolo 5.1)
Para a replicação tecnológica no âmbito do projeto "Mãos que Tecem a Floresta", devem-se observar:
1. **Prioridade de Isolamento**: O isolamento de 30mm em fibra cerâmica é obrigatório para garantir operações de biorrefino (extração de óleos/hidrolatos) que exigem constância térmica.
2. **Entrada de Ar**: Velocidade de entrada regulada em aprox. 0.3 m/s para garantir combustão completa ("clean burn").
3. **Pot Skirt**: A distância entre a panela e a saída da chaminé deve ser mínima, forçando o fluxo de gases quentes a circular pelas paredes do recipiente de processamento antes de escapar.

## 5. Referências Bibliográficas (ABNT)
STEFANDITYA, Y. et al. **Design of Rocket Stove with Computational Fluid Dynamics (CFD) Simulation**. In: PROCEEDINGS OF THE 4TH BOROBUDUR INTERNATIONAL SYMPOSIUM ON SCIENCE AND TECHNOLOGY 2022 (BIS-STE 2022). Surakarta, Indonesia: Advances in Engineering Research 225, 2023. p. 12-19. Disponível em: https://doi.org/10.2991/978-94-6463-284-2_3.

---
> [!NOTE]
> Este documento foi gerado via protocolo `/triage` a partir do documento bruto `125994011.pdf` e integra a base de conhecimento soberano da Biorrefinaria 5.1.
