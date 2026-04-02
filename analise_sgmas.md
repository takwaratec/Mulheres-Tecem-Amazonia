# Relatório de Diagnóstico: SGMAS Plotter v17.0
**Arquivo Analisado**: `docs/01_GOVERNANCA/sgmas_plotter.html`

A análise profunda do código geoespacial e dos construtores de *array* em JavaScript do **SGMAS Plotter** revelou diversas inconsistências com o Dossiê Final BNDES (R$ 30M Global / R$ 16M CAPEX). A ferramenta parou na versão anterior da estruturação orçamentária.

Abaixo, os laudos cirúrgicos e o plano exato das retificações que precisaremos executar no código para restaurar a soberania e simetria técnica da plataforma.

---

## <img src="assets/patterns/square_01_red.svg" width="22px"> 1. Inconsistências Globais (Sidebar e Header)

1.  **Déficit Demográfico**: O medidor fixo na lateral (linha 557) indica `1.050 FAMÍLIAS`. Nossa atualização fechou oficialmente a escala de impacto em **1.150 Famílias** diretas, e nós validamos isso expressamente no `ANEXO_VI`.
2.  **Ruído do CAPEX Global**: O medidor consolidado informa `R$ 25.0M CAPEX`. Devemos corrigir para **R$ 30.0M GLOBAL | R$ 16.0M CAPEX** para espelhar as aprovações recentes do DRE linear.

## <img src="assets/patterns/square_03_black.svg" width="22px"> 2. Erros de Destinação de CAPEX nos Nós (Javascript Array)

Os blocos de dados (`masterData`) estão inflados com projeções antigas e fantasmas nas cidades erradas, ignorando completamente nossa tabela cirúrgica de Centrais N2 (do ANEXO VI).

*   **Tarauacá (AC)**: Está alocado com *R$ 4.000.000,00*. (Incorreto. Tarauacá não é um Hub N2 com orçamento direto alocado, é atingido pelas Unidades Móveis N0).
*   **Cruzeiro do Sul (AC)**: *R$ 4.500.000,00*. (Deve ser reconfigurado para o impacto de **Polo Naval N2**, que no subtotal custa **R$ 209.145,00** em instalações, fora as compras das Balsas).
*   **Lábrea (AM)**: Alocada com *R$ 2.000.000,00* em instalações fantasmas. Lábrea não está na hierarquia de Polos N2 da nossa implantação final.
*   **Porto Velho e Boa Vista**: Ambas exibem R$ 3.000.000,00. As centrais de apoio artesanal e bioeconomia indígena dessas cidades foram otimizadas, e o investimento físico direto lá não passa de **R$ 78.800,00** por polo.
*   **Manaus (AM)** e **Mâncio Lima (AC)**: Estão registrados com `R$ 0,00`, mas recebem infraestrutura de domos no projeto, na ordem de **R$ 90.000,00** e **R$ 104.145,00**, respectivamente.
*   **Rio Branco (Hub N1)**: Está travado em R$ 8.5M. O ideal aqui é englobar todo o Lastro Central (Obras N1 + Maquinário Mestre T01-T09 + Frota Rodoviária), que bate **R$ 14.450.000,00**. 

**Resolução a Executar:** Remapear o nó `cost:` de cada cidade para refletir com exatidão implacável a matriz descentralizada dos Polos N2 descrita no `ANEXO VI`. O que for da verba global entra como adensamento da matriz Rio Branco.

## <img src="assets/patterns/square_04_black.svg" width="22px"> 3. Inconsistências Tecnológicas (Modelos T)

O painel de invenções do SGMAS (`n.inventions`) está desatualizado quanto às nomenclaturas e aos patamares de saneamento aprovados ontem:

1.  **Reator Biorrefinaria T02**: No Hub Master (Rio Branco), ele ainda carrega o nome genérico *T02*. Deve ser atualizado para a classificação blindada: **Reator Industrial 10m³ NR-13 (Coração Térmico)**.
2.  **Saneamento Suprimido (T12)**: As cabines essenciais **BSM (Banheiro Seco Modular - T12)**, citadas na mitigação das 1.150 famílias, não aparecem plotadas ou citadas visualmente em nenhum arranjo ribeirinho (ex: Cruzeiro do Sul ou Mâncio Lima). 
3.  **Tecnologia N0 Oculta**: Em Cruzeiro do Sul e Juruá, não existe menção sistemática à *Biorrefinaria Artesanal* (O antigo T02-A virou o novo **T01 Artesanal** com tambores), nem às Resinadoras **Airless Tornado**.

## Próximos Passos (Ação Governança)

Se você aprovar o escopo acima, posso reescrever os construtores JSON e os *loops* HTML do `sgmas_plotter.html`. Minha missão técnica será realinhar as variáveis de `$cost`, `$inventions` e `$threats` para que, ao clicarmos nos mapas, vejamos a perfeição fiscal e o alcance biológico exato do dossiê final.
