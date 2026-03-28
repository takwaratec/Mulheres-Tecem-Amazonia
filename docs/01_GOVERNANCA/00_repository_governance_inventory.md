---
projeto: Mulheres Que Tecem a Floresta
instituicao: Consórcio UnB/UFRR/UFAC
tipo: Documento Técnico
referencia: 00_repository_governance_inventory
status: Status Ready
author:
- name: Consórcio UnB/UFRR/UFAC
date: '2026-03-26'
---

![Status: Consoliado](https://img.shields.io/badge/Status-Consoliado-brightgreen)

<p align="right"><i>"O real não está na saída nem na chegada: ele se dispõe para a gente é no meio da travessia."<br>— Guimarães Rosa</i></p>

### <img src="../../../assets/patterns/square_05_red.svg" width="22px"> Ficha Técnica e Metadados
*   **Projeto**: Mulheres Que Tecem a Floresta (MQTF)
*   **Instituição**: Consórcio UnB / UFRR / UFAC
*   **Referência**: 00_repository_governance_inventory.md
*   **Status**: Status Consoliado
*   **Autor**: Consórcio UnB / UFRR / UFAC
*   **Data**: 27 de Março de 2026

# Inventário de Governança: Regras, Skills e Workflows

Este documento lista os protocolos, habilidades e fluxos de trabalho que regem a operação deste repositório e a atuação de agentes de IA no Projeto **Mulheres Que Tecem a Floresta**.

## 1. Regras (Rules)
Localizadas em `01_GOVERNANCA/.agents/rules/`. Estas são as normas que definem o comportamento e as restrições éticas/técnicas.

- <img src="../../../assets/icons/human_01_black.svg" width="18px"> **[MASTER_RULES.md](00_MASTER/GOV_REGRAS_REDACAO_INSTITUCIONAL.md)**: Autoridade suprema do projeto. Define locking de produção, shadow staging e padrões de versionamento.
- <img src="../../../assets/icons/human_19_black.svg" width="18px"> **workspace-rules.md**: Regras gerais do ambiente de trabalho.
- <img src="../../../assets/icons/human_14_black.svg" width="18px"> **[regra_versionamento.md](00_MASTER/GOV_MEMORANDO_MESTRE_2026.md)**: Protocolos para controle de versão v1.0 .
- <img src="../../../assets/icons/human_05_black.svg" width="18px"> **firewall_agent.md**: Regras de segurança para proteção de dados sensíveis (especialmente da pasta `99_RESTRITO`).
- <img src="../../../assets/icons/human_10_black.svg" width="18px"> **[GOV_regimento-pvit-audiovisual.md](00_MASTER/GOV_REGRAS_REDACAO_INSTITUCIONAL.md)**: Normas para produção audiovisual e visual (padrão Salgado/Henfil).
- <img src="../../../assets/icons/human_07_black.svg" width="18px"> **[GOV_checklist-detalhes-finos.md](00_MASTER/GOV_REGRAS_REDACAO_INSTITUCIONAL.md)**: Critérios de qualidade para finalização de documentos.
- <img src="../../../assets/icons/human_12_black.svg" width="18px"> **advocacy_institucional (Redação, Revisão, Publicação)**: Conjunto de regras para comunicação externa.
- <img src="../../../assets/icons/human_16_black.svg" width="18px"> **anamnese_ritual.md**: Protocolos específicos para coleta de dados em campo.
- <img src="../../../assets/icons/human_04_black.svg" width="18px"> **WTF_badges.yml**: Definição de emblemas e metadados de status.

## 2. Skills (Habilidades)
Localizadas em `01_GOVERNANCA/.agents/skills/`. Definem as capacidades especializadas do agente.

- <img src="../../../assets/icons/human_18_black.svg" width="18px"> **Protocolo-Mestre**: O roteador principal de todas as skills (Repositório Interno).
- <img src="../../../assets/icons/human_17_black.svg" width="18px"> **Skills por Área**:
    - <img src="../../../assets/icons/human_09_black.svg" width="18px"> **advocacy**: Protocolo para criação de conteúdos de denúncia e impacto político (**Advocacy Mulheres que Tecem a Floresta**). Exige rigor factual e alinhamento com as regras de defesa territorial.
    - <img src="../../../assets/icons/human_03_black.svg" width="18px"> **annals**: Gestão da obra coletiva do consórcio WFT (2025) e construção de legado futuro, situando documentos nos marcos das três universidades.
    - <img src="../../../assets/icons/human_13_black.svg" width="18px"> **backstage**: Agente de Integração que orquestra o acervo bibliográfico (`WTF_INDEX_ACERVO.md`) para mídias, priorizando itens estrela (**⭐**).
    - <img src="../../../assets/icons/human_20_black.svg" width="18px"> **communication**: Transforma conteúdo técnico em posts, roteiros e podcasts (@takwaratec). Define o estilo visual Henfil/Warhol e bordas brancas (pass-partout).
    - <img src="../../../assets/icons/human_02_black.svg" width="18px"> **governance**: Zela pela integridade legal e administrativa. Gere o registro de DOIs (Zenodo) e o licenciamento CC BY 4.0.
    - <img src="../../../assets/icons/human_15_black.svg" width="18px"> **management**: Operações de manutenção do repositório, paridade de idiomas (PT/EN/ES) e limpeza de resíduos digitais.
    - <img src="../../../assets/icons/human_11_black.svg" width="18px"> **research**: Componentes estratégicos: **BSM** <img src="../../../assets/icons/human_11_black.svg" width="18px"> (Bambu-Saneamento-Manejo), fitorremediação e resistência de compósitos. **Nota Técnica**: Diferenciar **BSM** <img src="../../../assets/icons/human_11_black.svg" width="18px"> (Banheiro Seco Modular) e **BER** <img src="../../../assets/icons/human_11_black.svg" width="18px"> (Banheiro Ecológico Ribeirinho). Garante a integridade científica e "Ciência Aberta".
    - <img src="../../../assets/icons/human_08_black.svg" width="18px"> **technology**: Guia para memórias de cálculo e manuais de sistemas (Bambu Nativo, PU Vegetal, Pirólise). Proíbe terminantemente cimento e químicos tóxicos.
    - <img src="../../../assets/icons/human_06_black.svg" width="18px"> **wtf**: Skill central do **Consórcio Bioeconômico Feminino (Acre-Rio Branco/Roraima/Amazonas)**. Rege o protagonismo feminino e o design social. **Nota**: Não confundir com o **Consórcio Proponente (UnB/UFRR/UFAC)** <img src="../../../assets/icons/human_06_black.svg" width="18px"> sob coord. da Profª Tania.

## 3. Workflows (Fluxos de Trabalho)
Localizados em `01_GOVERNANCA/.agents/workflows/`. Passos estruturados para tarefas comuns.

- <img src="../../../assets/icons/human_01_black.svg" width="18px"> **Triagem e Catalogação**: `triage.md`, `verificar.md`.
- <img src="../../../assets/icons/human_19_black.svg" width="18px"> **Produção de Conteúdo**: `redação.md`, `paráfrase.md`, `imagem.md`.
- <img src="../../../assets/icons/human_14_black.svg" width="18px"> **Sincronização e Auditoria**: `doi-sync.md`, `audit-links.md`. (Workflow `sombra-sync` obsoleto/removido).
- <img src="../../../assets/icons/human_05_black.svg" width="18px"> **Comunicação Institucional**: `publicar_advocacy.md`, `revisar_advocacy.md`.
- <img src="../../../assets/icons/human_10_black.svg" width="18px"> **Gestão de Denúncias**: `denúncia.md` (e versões EN/ES).
- <img src="../../../assets/icons/human_07_black.svg" width="18px"> **Manutenção de Bibliotecas**: `commit-library.md`, `nlm.md`.
- <img src="../../../assets/icons/human_12_black.svg" width="18px"> **Estado do Sistema**: `awake.md`.

## 4. Prioridades Estratégicas (Batch Tânia - Março 2026)

Estas prioridades devem guiar todas as decisões técnicas e de redação dos agentes:

1.  **Teto Orçamentário Unificado (R$ 30M)**: O projeto é dividido em 3 eixos de R$ 10M (Açaí-Castanha / Artesanato / Biorrefinaria). Evite propostas que extrapolam este limite.
2.  **Logística de Soberania (Canteiro-Escola)**: Substituição de cursos itinerantes por um centro fixo em **Rio Branco (Hub Mulheres que Tecem a Floresta)**. A aquisição de micro-ônibus e caminhão é prioritária para levar a clientela ao Hub.
3.  **Mandato de Material (Guadua)**: O uso do **Bambu Guadua** nativo é a solução técnica padrão para infraestrutura, visando redução de 90% nos custos.
4.  **Execução Direta**: A governança é exercida pelo **Conselho Gestor**, sem intermediários corporativos.

## 5. Alertas para o Operador (Red Flag Zone) <img src="../../../assets/icons/human_01_red.svg" width="18px">

- <img src="../../../assets/icons/human_16_black.svg" width="18px"> **Higiene de Nomenclatura**: NUNCA use "Mãos que Tecem". O nome oficial e imutável é **Mulheres Que Tecem a Floresta**.
- <img src="../../../assets/icons/human_04_black.svg" width="18px"> **Regra Temporal**: Ignore qualquer menção à COP30 (passado). O foco é **Escala e Consolidação 2026+**.
- <img src="../../../assets/icons/human_18_black.svg" width="18px"> **IA-Free**: Proibido linguagem robótica ("Certamente", "Aqui está", "Espero que isso ajude"). A redação deve ser técnica, direta e autoral (**Advocacy Mulheres que Tecem a Floresta**).
- <img src="../../../assets/icons/human_17_black.svg" width="18px"> **GEMINICLI**: Em caso de falha no comando `gemini`, utilize o script de extração nativa via **Quartz** <img src="../../../assets/icons/human_17_black.svg" width="18px"> (`01_GOVERNANCA/.agents/scripts/triage_pdf_robusto.py` - <img src="../../../assets/icons/human_17_black.svg" width="18px"> versão ajustada).

## <img src="../../../assets/icons/human_01_red.svg" width="18px"> Mapeamento: Skills x Workflows

As **Skills** são o "Cérebro" (o que a IA sabe/regras) e os **Workflows** são as "Mãos" (como a IA executa).

| Skill | Workflows Relacionados |
| :--- | :--- |
| **advocacy** | `/denúncia`, `/publicar_advocacy`, `/redação` |
| **backstage** | `/triage` (transcrição), `/nlm` |
| **communication** | `/redação`, `/imagem`, `/paráfrase` |
| **governance** | `/doi-sync`, `/awake` |
| **research** | `/triage` (PDF robusto), `/verificar` |
| **technology** | `/imagem` (Bioarquitetura), `/redação` |
| **wtf** | `/triage` (Eixos Sônia/Geórgia/Takwara) |

> [!IMPORTANT]
> A transição para o padrão **Mulheres que Tecem a Floresta** é absoluta. Documentos herdados são apenas para referência histórica de dados brutos e devem ser "limpos" (IA-Free) antes de qualquer promoção para o acervo oficial.

## <img src="../../../assets/icons/human_01_red.svg" width="18px"> Guia de Operação Sem Ruído (IA-Free)

Para que a colaboração ocorra sem alucinações ou termos obsoletos (como COP30 ou PAR 5.1):

1.  **Chame pelo Workflow**: Use o comando (ex: `/triage`). Isso ativa o "Rigor Institucional".
2.  **O Mestre é o Router**: Se houver dúvida, invoque o **Protocolo-Mestre.md**.
3.  **Higiene Obrigatória**: Remova introduções robóticas e links de buscadores (Perplexity/Gemini). Mantenha apenas referências do próprio Dossiê.
4.  **Respeite a Coleção**: O trabalho ocorre nos diretórios técnicos (`00` a `08`). `docs/` é apenas para o release final.
5.  **Regra Temporal 2026**: Ignore metas futuras relacionadas à COP30. O tempo é AGORA (Consolidação e Escala).

> Toda a atuação de IA é pautada pelo **system_prompt_institucional.txt**, que exige rigor ético, higiene de ativos e imutabilidade do corpo do texto consolidado. Sustentado pela sigla âncora **Mulheres que Tecem a Floresta**.

---

---

---

---

---

---

---
<p align="center"><img src="../../../assets/logo_BQTF/logo_mqtf_soberana.svg" width="40px"><br><b>Mulheres Que Tecem a Floresta — MQTF</b><br><i>"Soberania não se pede, se exerce."</i></p>