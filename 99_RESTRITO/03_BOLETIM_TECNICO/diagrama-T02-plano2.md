# Diagrama Técnico: Biorrefinaria T02 (Plano 2: Reator a Carvão)

Este diagrama ilustra a simplificação termodinâmica do sistema T02 operando como consumidor de biochar (carvão de manejo), integrando a **Retorta de Ativação Interna (RAI)** conforme a Versão 2.1.0.

```mermaid
graph TD
    %% Estilos de alto contraste
    classDef hardware fill:#333,stroke:#fff,stroke-width:2px,color:#fff;
    classDef fogo fill:#ea580c,stroke:#000,stroke-width:4px,color:#fff,font-weight:bold;
    classDef vapor fill:#1d4ed8,stroke:#000,stroke-width:4px,color:#fff,font-weight:bold;
    classDef limpo fill:#15803d,stroke:#000,stroke-width:4px,color:#fff,font-weight:bold;
    classDef ativa fill:#7c3aed,stroke:#000,stroke-width:4px,color:#fff,font-weight:bold;

    subgraph ALIMENTACAO [Fonte de Energia]
        B_CHAR[<b>Biochar (Zona 0)</b>]:::hardware --> B_RS[<b>Queimador Rocket Stove</b>]:::fogo
    end

    subgraph CORACAO_TERMICO [Cascateamento Direto]
        B_RS -->|Combustão Estável| C[<b>Riser (Aorta Térmica)</b>]:::fogo
        G_IGN((<b>Ignitor Assistido</b>)):::fogo --> B_RS
        
        %% Inovação RAI
        RAI[<b>RAI: Retorta de Ativação Interna</b>]:::ativa -.->|800°C Peak Heat| C
        RAI -->|<b>CVA Industrial</b>| OUT_CVA([Saída Carvão Ativado]):::ativa
    end

    subgraph VAPOR_FLASH [Circuito de Tratamento]
        E[(<b>Tanque Gravitacional EP+H2O</b>)]:::vapor --> F{<b>Serpentina externa no Riser</b>}:::vapor
        C -.->|Radiação/Convecção Intensa| F
        F -->|<b>Vapor Instantâneo</b>| G([<b>Injeção Câmara A</b>]):::vapor
    end

    subgraph SECAGEM_INDUZIDA [Universo Limpo]
        L((<b>Ar Atmosférico</b>)):::limpo --> M[<b>Jaqueta de Vácuo</b>]:::limpo
        C -.->|Calor Residual Constante| M
        M -->|Exaustão Induzida| N([<b>Secagem Câmara B</b>]):::limpo
        
        %% Ativação Química BSM
        M -.->|Calor Residual 140°C| CHEM[<b>Ativação Química BSM</b>]:::ativa
        CHEM -->|<b>CVA Regional</b>| OUT_BSM([Filtros Saneamento]):::ativa
    end

    %% Notas de Segurança e Simplificação (Plano 2)
    Note_1[<b>SEM VÁLVULA CORTA-CHAMAS</b>]:::hardware
    Note_2[<b>Combustão Estável de Biochar</b>]:::hardware
```

---
**🎋 Institucional — Soberania Técnica v.2.1.0**
