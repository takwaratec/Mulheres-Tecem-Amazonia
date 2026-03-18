---
title: "Análise Termodinâmica e Simulação Aspen: Biorrefinaria T02 v.2.1.0"
author: "Núcleo Institucional / Skill: Engenharia Industrial"
date: "2026-03-07"
version: "2.2.2-aspen"
status: "RESTRITO - AUDITORIA TÉCNICA"
type: "Boletim de Simulação"
---

# Boletim Técnico: Parâmetros de Simulação Aspen Plus / DWSIM

Este documento formaliza os inputs de processo para a validação do **T02 Plano 2 (Reator a Carvão)**, permitindo que a equipe de engenharia simule o balanço de massa e energia com precisão científica.

## 1. Definição do Escopo da Simulação
O objetivo é provar a autossuficiência térmica do sistema para vaporização flash (Câmara A) e secagem induzida (Câmara B), utilizando o combustível produzido na Zona 0 (Biochar).

## 2. Componentes e Propriedades (Global Settings)
- **Método Termodinâmico:** RK-SOAVE ou PENG-ROB (adequados para hidrocarbonetos e gases não-condensáveis).
- **Componentes Não-Convencionais (NC):** 
    - `BIOCHAR`: Definido por análise elementar (C: 85%, H: 3%, O: 10%, Cinzas: 2%) e análise imediata.
    - `BIOMASSA`: Para o Plano 1 (Gases de pirólise).

## 3. Flowsheet de Processo: Blocos de Simulação

### A. Subsistema de Combustão (Rocket Stove)
- **Bloco:** `RStoic` ou `RGibbs`.
- **Alimentação 1:** Biochar (Zona 0) a 25°C.
- **Alimentação 2:** Ar Atmosférico (Excesso de 20%, T=28°C, UR=80%).
- **Saída:** Gases de combustão (Flue Gas) a T > 900°C.
- **Objetivo:** Calcular o calor de reação ($Q_{comb}$).

### B. Subsistema de Vapor Flash (Serpentina)
- **Bloco:** `HeatX` (Trocador de calor).
- **Lado Quente:** Gases do Riser.
- **Lado Frio:** Mistura Fluida (80% H2O + 20% EP).
- **Parâmetros:**
    - Pressão de entrada: 1.3 atm (Coluna hidrostática de 3m).
    - Temperatura de saída: 125°C - 150°C (Vapor Superaquecido).
    - Taxa de Fluxo Alvo: 30 kg/h.

### C. Subsistema de Secagem Induzida (Jaqueta de Vácuo)
- **Bloco:** `Heater` acoplado a um fluxo de ar.
- **Entrada:** Ar externo (28°C).
- **Troca Térmica:** Calor residual da jaqueta anular ($Q_{loss}$ do Rocket/Retorta).
- **Saída Alvo:** Fluxo de ar a 70°C constante.

## 4. Critérios de Convergência e Validação
- **Balanço Global:** $Q_{comb} \ge Q_{vap} + Q_{secagem} + Q_{perdas}$.
- **Soberania Energética:** O sistema deve demonstrar que 5kg de biochar/hora são suficientes para manter o cascateamento total por 8 horas.

---
## 5. Próximos Passos (Plano 3 - Metanol)
Para a próxima etapa de auditoria, incluir o bloco `R-Equil` para gaseificação catalítica e o compressor multibágio para o loop de síntese de metanol (BtL).

**🎋 Institucional — Engenharia Soberana v.2.1.0**
