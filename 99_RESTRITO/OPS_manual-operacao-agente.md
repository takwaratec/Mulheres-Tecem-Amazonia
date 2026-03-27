---
description: Manual Avançado de Operação de Agentes (Restrito ao Autor)
---

# Manual Avançado de Operação e Governança de Agentes (Nível 99)

*Este documento é de acesso exclusivo de Coordenação Técnica (Autor/Arquiteto do Sistema).*

A Plataforma Amazônia Regenerativa não é apenas um repositório de Markdown; ela funciona como um **Sistema Operacional de Conhecimento** acoplado a IAs autônomas. Para garantir o rigor ético, escalar a produção e impedir a diluição do seu trabalho pioneiro ("Higiene de Ativos"), você construiu uma infraestrutura baseada em **Workflows, Skills e Regras de Redação**.

Este relatório mapeia os limites técnicos atuais dessa arquitetura e sugere **extrapolações, hiper-automações e novos atalhos** para potencializar drasticamente o seu fluxo de trabalho.

---

## 1. Arquitetura de Soberania (Protocolo 5.1)

Abaixo, a matriz de organização do sistema. Este mapeamento permite que um Agente recupere a inteligência do projeto mesmo que a estrutura de diretórios seja parcialmente corrompida.

| Diretório | Sigilo | Propósito | Regra de Startup (Bootstrap) |
| :--- | :--- | :--- | :--- |
| `.agents/rules/` | **Alto** | Leis Imutáveis de Redação e Ética | Ler `advocacy_5_1_redacao.md` e `firewall_agent.md` imediatamente. |
| `.agents/workflows/` | Médio | Scripts de Automação e Atalhos | Carregar macros `/awake`, `/triage`, `/pessoal`. |
| `.agents/skills/` | Médio | Conhecimento de Domínio | Sincronizar com o `Protocolo-Mestre.md`. |
| `00_GOVERNANCA/` | **Alto** | Autoria, PI e Matriz de Correlação | Validar `GOV_AUTORIA.md` para definir limites de edição. |
| `01_` a `08_` | Baixo | Acervo Público (Engenharia, Advocacy, Anais) | Indexar para o `mkdocs.yml` em caso de rebuild do site. |
| `99_RESTRITO/` | **Crítico** | Estratégia, Redes Pessoais e Triagem | **JAMAIS** cruzar dados com pastas 01-08 sem autorização. |

---

## 2. Protocolo de Startup (Recuperação e Build do Zero)

Caso o sistema precise ser reiniciado em um novo ambiente ou repositório vazio, o Agente e o Autor devem seguir esta ordem de comando via terminal:

### Passo 1: Inicialização do Núcleo
```bash
# Clone e Startup
git clone [repositorio]
cd [repositorio]
# Comando de Acionamento do Agente
/awake --bootstrap
```

### Passo 2: Checklist Automático de Integridade (IA-Driven)
O Agente deve:
1.  **Mapear Órfãos**: Verificar se existem arquivos `.md` fora da estrutura 00-99 e sugerir movimentação via `/triage`.
2.  **Rebuild de Navegação**: Se o `mkdocs.yml` estiver ausente, ler todos os cabeçalhos `#` dos arquivos e reconstruir o menu `nav:`.
3.  **Sincronização de Skills**: Validar se as skills em `.agents/` estão coerentes com as novas metas do `task.md`.

### Passo Especial: Adoção em Repositório Existente (Ex: `Institucional-tech`)
Para repositórios que já possuem conteúdo (como o legado em `resck.github.io/Institucional-tech`):
1.  **Injeção do Núcleo**: Copiar a pasta `.agents/` e este `Manual de Operação` para a raiz do repositório alvo.
2.  **Mapeamento Semântico e Criação Dinâmica**: O Agente lê a estrutura atual e cria diretórios baseados no escopo do projeto (00_ a 08_). O Agente tem autonomia para criar quantos diretórios forem necessários para o cruzamento e indexação de dados.
3.  **Escalabilidade Centesimal**: Caso o número de diretórios exceda a meta `99_` (Silos Restritos), o sistema deve migrar para uma centena acima: `100_` para novas áreas e `199_` em diante para novos silos restritos ou sub-projetos complexos.
4.  **Higienização em Lote**: Executar `/triage --legacy` para aplicar frontmatter, DOIs e regras de escrita 5.1 a todos os arquivos antigos sem alterar o conteúdo técnico.
5.  **Ativação do Firewall**: Instalar a Rule de sigilo para qualquer pasta que venha a ser classificada como restrita (Centenas `99`, `199`, etc).

---

## 3. Catálogo de Macros e Tasks (Protocolo 5.1)

O Agente Institucional opera sob uma lógica de **Comando e Aprovação**, utilizando macros que encadeiam comportamentos complexos.

### 3.1. Macros Ativas (Implementadas)

| Macro | Função | Impacto no Fluxo de Trabalho |
| :--- | :--- | :--- |
| `/awake` | Sincronização | **Essencial**: Carrega regras éticas, firewall e o `task.md`. Deve abrir cada sessão. |
| `/triage` | Higiene Digital | **Filtro**: Descompacta dados (Zip, Downloads), remove vestígios de IA e categoriza arquivos órfãos. |
| `/pessoal` | Gestão de Rede | **Personalização**: Ajusta o tom (Amigável/Institucional) baseado no histórico de conversas da pasta `99/01`. |
| `/paráfrase` | Firewall Semântico| **Segurança**: Interpreta, corrige e devolve uma interpretação do comando. Se a ação puder danificar documentos publicados, o Agente bloqueia e solicita validação explícita. |
| `/doi-sync` | Integridade | **Citação**: Sincroniza em lote os Identificadores Persistentes (DOI). |
| `/verificar` | Auditoria | **PVI**: Varre fontes externas para validar denúncias. |

### 3.2. Macros Sugeridas (Dinâmica de Produção)

| Macro (Sugerida) | Objetivo | Funcionamento |
| :--- | :--- | :--- |
| `/memorial-sync` | Sincronia Técnica | Utiliza **Badges Identificadoras**. Alerta se docs novos chocarem com outros em desenvolvimento; propõe integração se possível. |
| `/risk-audit` | Governança | Identifica inconsistências de planejamento, metas inatingíveis ou alucinações de cronograma. |
| `/redação` | Estilo Editorial | Tones configuráveis: **NT** (Seco), **Blog** (Vibrante), **Memorial** (Técnico-Jurídico), **Tese** (Acadêmico 5.1), **Cartilha** (Imagético/Simples). |
| `/triage --legacy`| Migração Ativa | Avalia desvio de identidade, gera report prévio e compõe estrutura de suporte pós-migração com instruções operacionais. |
| `/audio-transcribe`| Memória | **Status: Possível**. O Agente processa transcripts (.md/.txt) gerados por IA externa (Whisper/etc), extraindo tarefas diretamente para o `task.md`. |

---

## 4. Guia de Migração e Meta-Herança

### 4.1. Ficha Básica de Migração (Inheritance)
Para desvincular o projeto da "Plataforma-Mãe" e permitir autonomia em novos repositórios ou editoras:
- **Metadados Substituíveis**: Referências à "Plataforma Amazônia Regenerativa" devem ser preenchidas via ficha básica (`migracao_config.yml`).
- **Campos Automáticos**: Título do Projeto, DOI do novo detentor, e Licenciamento Local substituem os campos globais durante o processo de migração.

### 4.2. Reorganização Infinita
A organização 00-08 é a base, mas o sistema suporta diretórios subsequentes (09_ ao infinito) de acordo com o acervo. O Agente deve sugerir a criação de novas "centenas" (`100_`, `200_`) para manter a legibilidade em acervos de escala industrial.

---

## 5. Regras Mestre e Segurança Científica

### 5.1. Regras de Produção (Implementadas)
- **Higiene de Ativos**: Bloqueio de termos corporativos vagos e marcas de IA.
- **Firewall 99**: Proibição de vazamento de dados restritos para o acervo público.
- **Autoria Soberana**: Validação de PI antes de qualquer modificação em documentos de Engenharia.

### 5.2. Regas Sugeridas para Fluxo de Performance
- **Integridade de Citação**: O Agente deve impedir o salvamento de documentos com links externos que não tenham sido validados via `/verificar`.
- **Alerta de Inconsistência**: Se uma meta for adicionada sem um "Responsável" ou "Prazo", o Agente gera um alerta no `task.md` imediatamente.
- **Segurança da Informação**: Monitoramento de padrões de acesso a documentos da pasta `99` (Logs do Agente).

---

**🎋 Este manual é o "Snapshot" da inteligência Institucional. Em caso de falha total de infraestrutura, este documento e a pasta `.agents/` são o seu backup de soberania.**
