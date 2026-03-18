# Protocolo de Higiene de Ativos Brutos (Cross-App)

Este protocolo define o padrão para a limpeza e indexação de dumps de dados de aplicativos de comunicação (WhatsApp, Instagram, etc) no Acervo Amazonia Regenerativa.

## 1. Filtro de Lixo Residual
Ao processar uma pasta de exportação, o Agente deve deletar ou ignorar:
- **Arquivos de Sistema:** `.DS_Store`, `Thumbs.db`, `.nomedia`.
- **Mídia de Interface:** Ícones, botões, stickers (.webp), e imagens de visualização rápida (.thumb).
- **Metadados Irrelevantes:** Arquivos `.json` de configuração de aplicativo que não contenham logs de mensagem.

## 2. Processamento de Logs (Texto)
- **Extração Semântica:** Converter fragmentos de chat em arquivos Markdown estruturados por contato/data.
- **Anonimização (Se necessário):** Proteção de dados sensíveis de terceiros não relacionados ao projeto.
- **Linkagem:** Se um link foi compartilhado no chat, ele deve ser processado pelo `/triage` padrão para extração de conteúdo.

## 3. Gestão de Mídias Ativas
- **Imagens Técnicas:** Fotos de campo, esquemas e notas manuais devem ser movidas para a respectiva pasta de projeto.
- **Áudios Pendentes:** Criar uma entrada em `task.md` no formato: `[ ] Transcrever áudio: [nome_do_arquivo] - Origem: [App/Data]`.
- **Arquivos Fundamentais:** PDFs, documentos de engenharia e notas fiscais devem ser indexados imediatamente.

## 4. Geração de Tarefas de Resposta
Toda mensagem que exija um posicionamento ou ação do Autor deve se tornar uma pendência no `task.md`, classificada pelo nível de intimidade da rede pessoal.
