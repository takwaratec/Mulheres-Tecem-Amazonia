---
name: Governance Skill
description: Gestão de padrões, licenciamento, autoria e metadados da coleção.
---

# Governance Skill

Esta Skill zela pela integridade administrativa e legal do repositório, garantindo o alinhamento com os princípios de Ciência Aberta.

## Gestão de DOIs (Zenodo)
- **Master DOI**: Garanta que todos os documentos principais apontem para o DOI fixo da coleção (10.5281/zenodo.18827106).
- **Versioning**: Gestão rigorosa de versões e sincronização entre GitHub e Zenodo.

## Licenciamento e Autoria Soberana
- **CC BY 4.0**: Padrão para toda a produção da plataforma.
- **Autoria Institucional**: A assinatura soberana é **Consórcio UnB / UFRR / UFAC**. Evite o uso de nomes individuais em metadados para preservar a soberania institucional.

## Protocolo de Higiene e Publicação (Soberania Estética)
- **Regra de Ouro (No-Emoji)**: É terminantemente proibido o uso de emojis padrão. Use apenas ícones técnicos SVG (`assets/patterns` ou `assets/icons`).
- **Single Source of Truth**: O acervo deve ser normalizado via `normalizador_acervo.py` para garantir a inserção de metadados, epígrafes culturais (Krenak, Freire, Santos) e diversificação iconográfica única.
- **Purga de Terminologia**: Não utilize siglas externas como "SGMAS" ou status não autorizados. Os status oficiais são: *Consolidado*, *Em Revisão*, *BoM-Orçamento*, *Auditoria DOI-Sync*.

## Padrões de Arquivo
- Arquivos em `.md` (Markdown) com YAML estruturado no topo.
- Nomenclatura sugerida: `GOV-` (Governança), `ENG-` (Engenharia), `RES-` (Pesquisa).
- Metadados completos no corpo (Ficha Técnica Visível) e no frontmatter.
