---
description: Avalia, higieniza e classifica materiais brutos em Markdown estruturado
---

# Workflow: `/triage`

Este fluxo de trabalho automatiza a entrada de dados brutos (PDFs, links de notícias, rascunhos) no acervo, aplicando as regras de redação, tom autoral e higiene cibernética antes de mesclar o conhecimento à Plataforma.

## Uso
**Para o usuário:** No chat, envie `/triage [link ou nome do arquivo na /tmp]`. Informe rapidamente o propósito (ex: "matéria sobre o PL 123", "artigo científico sobre PU").

## Passo a Passo para o Agente:
1. **Detecção e Decompressão:** Ao detectar pacotes comprimidos (`.zip`, `.tar.gz`) na pasta `/99_RESTRITO/02_TRIAGEM_BRUTA/`, extraia o conteúdo automaticamente via terminal.
2. **Processamento de Mídia:** Identifique arquivos de áudio (`.opus`, `.mp3`, `.wav`). Utilize o cérebro da IA para **transcrição obrigatória** do conteúdo.
3. **Integração de Mentoria:** Se o conteúdo for de mentoria (Tania/Sonia/etc.), incorpore as instruções transcritas no `GOV_memorando-mentoria.md` e movimente para a pasta de arquivos auditáveis em `01_SOMBRA_AUDITORIA/04_GESTAO_OPERACIONAL/01_MENTORIA/`.
4. **Higienização de Resíduos e Faxina:** 
    - Elimine arquivos de sistema (`.DS_Store`, etc).
    - Após a promoção do conteúdo refinado para a Sombra, **delete permanentemente os arquivos brutos** na pasta `02_TRIAGEM_BRUTA`.
5. **Acionamento:** Converta partilhas fundamentais ou pedidos em tarefas concretas no `task.md`.
## 4. Diferenciação e Contexto (Mãos que Tecem a Floresta / Biorrefinaria 5.1)
- **Membros Externos (Mapeamento de Componente)**:
    - **Prof. Tania**: Mentoria Global (Estratégia e Soberania). Encaminhar para `00_GOVERNANCA`.
    - **Prof. Sônia**: Componente Açaí-Castanhas (R&D de Bioinsumos). Encaminhar para `02_PESQUISA_DESENVOLVIMENTO`.
    - **Prof. Geórgia**: Artesanato (Design e Cultura). Encaminhar para `03_COMUNICACAO` (ou folder específico de design).
    - **Prof. Vanessa**: Financeiro, Consolidação e Auditoria. Encaminhar para `04_GESTAO_OPERACIONAL`.
- **Interpretação de Contexto**: Cada item deve ser delineado conforme sua aplicação no projeto **Mãos que Tecem a Floresta / Biorrefinaria 5.1**.
- **Alerta de Mentoria de Gestão**: O Agente deve disparar um sinal sonoro/alerta textual imediato se identificar que qualquer solicitação de **Mentoria de Gestão** está sendo desconsiderada ou postergada indevidamente.

## 5. Rotina de Triagem Robusta (PDF/Quartz macOS)
Para documentos técnicos complexos (ex: Imperveg, BNDES), utilize o modo robusto:
1. **Extração Nativa**: O script `triage_pdf_robusto.py` utiliza as bibliotecas `Quartz` e `PDFDocument` para garantir fidelidade total ao texto original.
2. **Prompts de Biblioteconomia**: O agente deve agir como "Biblioteconomista Sênior" para categorizar, resumir e vincular a tecnologia ao projeto WTF.
3. **Destino**: `01_SOMBRA_AUDITORIA/01_TECNOLOGIA_TAKWARA` ou pasta específica do projeto `WTF_`.

## 6. Alerta de Revisão: 
- Apresente o resumo analítico de 2 a 3 pontos.
- Peça aprovação final para mover do `tmp/` para a respectiva pasta auditada na Sombra.

