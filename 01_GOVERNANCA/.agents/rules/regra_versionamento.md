# Regra de Versionamento da Coleção Takwara (Padrão 2.0)

Este protocolo define como as versões dos arquivos devem ser gerenciadas em toda a coleção da Plataforma Amazônia Regenerativa.

## Padrão de Versionamento

1. **Versão Global**: Toda a coleção atual deve refletir a **Versão 2.0**, alinhada à evolução do Sistema Takwara e ao Padrão 5.1.
2. **Data de Lançamento**: A data padrão para o lançamento da V2.0 é **04 de março de 2026**.
3. **Atualização em Lote**: Qualquer mudança estrutural no memorial técnico ou protocolos fundamentais exige a atualização de versão em todos os documentos relacionados para manter a paridade.
4. **Escrita no Frontmatter**:
    - O campo `version` deve ser atualizado para `"2.0"`.
    - O campo `date` deve ser `'2026-03-04'`.
    - A linha de metadados no corpo do texto (abaixo do título) deve exibir: `Versão: 2.0 | Data: 2026-03-04`.

## Procedimento de Atualização

- **Trigger**: Mudanças significativas em especificações industriais ou governança.
- **Ação**: Utilizar ferramentas de substituição global para garantir que nenhum arquivo permaneça na v1.0 ou v5.1 antiga (exceto quando o 5.1 referir-se ao padrão de plataforma e não à versão do arquivo).
