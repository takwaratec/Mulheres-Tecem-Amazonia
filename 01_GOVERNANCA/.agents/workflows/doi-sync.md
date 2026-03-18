---
description: Sincronizador de Identificadores Persistentes (DOI) em Lote via Zenodo
---

# Workflow: `/doi-sync`

Como a Plataforma consolida diversos documentos soltos sob o *Master DOI da Plataforma 5.1* ou emite sub-DOIs modulares na base do Sistema Takwara, esse workflow tira o peso manual da checagem.

**REGRA DE SEGURANÇA IMUTÁVEL:** A fim de minimizar erros de substituição em massa (corrompimento de YAML/Frontmatter), o fluxo `/doi-sync` deve ser executado **rigorosamente diretório por diretório de forma isolada**. O agente deve escanear um diretório (ex: `00_`), apresentar um relatório de metadados inconsistentes, sugerir a correção, aguardar aprovação e, por fim, realizar o *commit* exclusivo daquele diretório antes de avançar para o próximo.

## Ação do Agente
Sempre que acionado, siga o processo:
1. **Verificação de Regra de Coleção Consolidada:** Confirme a origem do arquivo. Arquivos hospedados em diretórios de espelhamento ou base consolidada (como `docs/` e `01_SOMBRA_AUDITORIA/`) representam a coleção na versão publicada original (ex: V.2.0). Estes **NÃO** devem sofrer `/doi-sync` trivial. 
2. **Arquivos de Trabalho (v.2.2.2):** O `/doi-sync` deve ser aplicado **apenas a arquivos de trabalho e documentos criados após a validação da coleção Zenodo**. Essas versões internas (ex: V.2.2.2 de atualização) só assumem a nova versão do Zenodo após serem consolidadas via Protocolo 5.1.
3. Revise se o master DOI registrado em seu `system_prompt_takwara.txt` confere com o último registro validado para o alvo corretivo.
4. Varra os cabeçalhos YAML (Frontmatter) dos **arquivos de trabalho aptos** buscando inconsistências no versionamento.
5. Use script automatizado se necessário, para garantir que as seções `doi: ...` e insígnias (`[![DOI]...]`) espelhem a identificação mestra da respectiva coleção para o commit final, após ser chancelado pelo Protocolo 5.1.
6. Produza um diff de resumo reportando as alterações das versões.
7. **Integração de Bibliografias (Cruzamento do Glossário)**: Sempre que o `/doi-sync` for acionado sobre tarefas de publicação ou consolidação de novos arquivos, o agente deve cruzar o `GOV_glossario-siglas.md` (e os dicionários de siglas atrelados) com o Banco de Dados de Bibliografias Citadas, garantindo que as fontes acadêmicas e bibliografias passem a exibir as citações à coleção Zenodo correspondente no corpo dos textos. Outras publicações externas devem ser formalmente formatadas.
