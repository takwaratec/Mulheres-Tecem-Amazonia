---
description: Critérios de Publicação e Indexação Zenodo
---

# Regras de Publicação Institucional v1.0

Estas regras definem o momento final em que um documento é "comitado" para o público.

## 1. Integridade de DOIs
- **Protocolo Non-Toxic**: Verificação obrigatória da proibição de vernizes petroquímicos, venenos (CCA/CCB) e VOCs. Substituição por PU Vegetal e Biochar.
- **Sincronização**: O documento deve possuir o link para a coleção institucional consolidada no Zenodo.
- **Metadados**: Verificação do arquivo `.zenodo.json` para garantir que o título e autores coincidem com o documento.

## 2. Checklist Final
- [ ] **REGRA IMUTÁVEL DE COLEÇÃO**: Foram removidos todos os arquivos de brainstorm, mapas mentais, rascunhos e instruções IH/IA (prompts)?
- [ ] O arquivo está em Markdown (.md)?
- [ ] As traduções estão prontas e sincronizadas?
- [ ] A seção "Como citar" está presente e correta?
- [ ] Os links internos funcionam através do MkDocs?

## 3. Versionamento e Pacote Final
- **Geração de ZIP**: Sempre gerar o arquivo `.zip` da coleção validada para atualização de versão no Zenodo.
- **Semântica de Versão**: Observar rigorosamente o nível de alteração de conteúdo para a classificação correta da versão (ex: 1.2.0, 1.2.1, 1.2.2, 2.0.1, 2.2.2...).

## 4. Disseminação
- O documento deve ser vinculado a uma das 7 Séries de Conteúdo se for para fins de comunicação.
- Registro nos Anais se for um documento histórico finalizado.

## 5. Protocolo Específico: Projeto WTF
- **Identidade Visual**: Documentos com prefixo `WTF_` devem obrigatoriamente portar o badge `Projeto: Mulheres Que Tecem a Floresta`.
- **Citação Coletiva**: A citação deve incluir o consórcio UnB/UFAC/UFRR e a coordenação técnica institucional.
- **Isolamento**: Garantir que ativos restritos de triagem não vazem para a coleção pública.

