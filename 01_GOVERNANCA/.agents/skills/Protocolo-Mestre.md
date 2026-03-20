---
title: Protocolo-Mestre (Meta-Skill)
description: Roteador principal de domínio. Analisa o contexto e carrega multiplas Skills (Ex: Ciência + Advocacy) simultaneamente.
---

# Meta-Skill: Protocolo-Mestre de Roteamento

Este documento funciona como a **Mesa de Som (Mixer)** das habilidades da Inteligência Artificial. Ele impede que o Agente atue "cego" usando apenas uma lente acadêmica ou apenas uma lente militante, quando o projeto exige as duas.

## Instrução de Triangulação de Domínio
Sempre que o Agente for acionado para criar, revisar ou documentar no ecossistema **Mulheres Que Tecem a Floresta**, ele deve cruzar automaticamente as matrizes abaixo:

### 1. Cruzamento: Ciência + Advocacy (Dossiês e Artigos)
**Quando usar:** Quando operar em `01_GOVERNANCA/04_PARECERES_E_RELATORIOS/`, `07_BLOG_MEDIUM`, ou acionar os comandos `/triage`, `/publicar_advocacy`.
**Ação do Agente:** 
- Carregar a **Advocacy Skill** (tom institucional de defesa e soberania).
- Carregar a **Research Skill** e **Technology Skill** (embasamento em tecnologia social regenerativa).

### 2. Cruzamento: Engenharia + Governança (Memoriais Técnicos)
**Quando usar:** Quando operar em `02_TECNICO/`, `01_GOVERNANCA/` ou acionar `/doi-sync`.
**Ação do Agente:** 
- Carregar a **Technology Skill** e **Management Skill** (descritivos estruturais de baixo custo).
- Carregar a **Governance Skill** (padronização BNDES, autoria institucional e licenças CC BY 4.0).

### 3. Cruzamento Singular: Preservação Histórica
**Quando usar:** Pasta `06_MEDIA`.
**Ação do Agente:** Carregar exclusivamente a **Annals Skill**.

### 4. Cruzamento: Integração e Mídia (Backstage)
**Quando usar:** Operações de exportação para NotebookLM ou criação de roteiros.
**Ação do Agente:** 
- Carregar a **Backstage Skill** (orquestração de mídia).
- Carregar a **Communication Skill** (tom institucional).

### 5. Cruzamento Principal: Bioeconomia Feminina e Consórcio (WTF)
**Quando usar:** Prioridade máxima para o projeto "Mulheres Que Tecem a Floresta" e Consórcio UnB/UFAC/UFRR.
**Ação do Agente:**
- Carregar a **WTF Skill** (Design Social e Governança Cooperativa).
- Carregar a **Technology Skill** (Bambu/Mamona - Tecnologia Social Regenerativa).
- Ativar prefixos de arquivo `ENG_` (técnicos) e `WTF_` (governança).


## O Ponto Cego (Gatilho de Segurança)
Se o usuário pedir algo ambíguo ("Escreva um texto sobre bambu"), o Agente deve **PARAR** e exigir do usuário: *"Autor, este documento deve ser roteado pelo eixo da Ciência (documento técnico) ou do Advocacy (denúncia/blog)?"*
