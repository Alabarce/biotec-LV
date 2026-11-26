# LV • Boletim de pesquisa

Mobilidade ativa e tecnologias assistivas. Catálogo das edições semanais do boletim, de 2026 a 2027.

Cada entrada liga **fonte ou estudo → achado → implicação**: o que uma notícia, norma ou estudo diz, e que pergunta ou requisito testável isso gera para o projeto (sistema embarcado, processamento de dados e aplicativo de monitoramento). Estudos acadêmicos trazem a referência no padrão ABNT e o DOI, prontos para o TCC.

## Edições

### 2026

| Nº | Data | Entradas | Selos | Arquivo |
|---|---|---|---|---|
| 02 | 26/11/2026 | 3, sendo 2 estudos | métrica, articulação | [edição 02](edicoes/2026/02-2026-11-26-semana.md) |
| 01 | 24/11/2026 | 3 | articulação, laboratório, métrica | [edição 01](edicoes/2026/01-2026-11-24-semana.md) |
| 00 | 19/11/2026 | 1 (piloto) | métrica | [piloto](edicoes/2026/00-2026-11-19-piloto.md) |

## Rascunhos aguardando aprovação

Nenhum no momento.

## Manual de uso

### Como o catálogo cresce

1. **Sábado de manhã:** sai o rascunho da semana, com levantamento e checagem de coerência. Ele entra no topo do Boletim (Google Docs) e em `rascunhos/`, num commit `rascunho:` (autor: Claude).
2. **Aprovação:** no Doc, o checkbox "Aprovar este rascunho" aprova tudo; o checkbox no selo de uma entrada aprova só ela; o checkbox de um termo proposto aprova só o termo. Apagar uma entrada a descarta. Item sem marcação continua pendente.
3. **Publicação:** o que foi aprovado vira uma edição numerada em `edicoes/AAAA/`, num commit `aprovação:` com autoria do Bruno, e os termos aprovados entram no `GLOSSARIO.md` e na aba Glossário do Doc.

O histórico de commits é o registro do trabalho contínuo: um rascunho por semana e uma aprovação por edição.

### Selos

Cada entrada leva um selo: a pendência do projeto que ela ajuda a resolver. No frontmatter das edições os selos aparecem sem acento, no campo `pendencias`, para facilitar filtro e contagem.

| Selo | No frontmatter | O que a entrada faz avançar |
|---|---|---|
| MÉTRICA | `metrica` | O que medir e com que precisão: erro aceitável, critério de sucesso, método de ensaio. |
| LABORATÓRIO | `laboratorio` | Onde fazer o ensaio de bancada: grupos, laboratórios e infraestrutura em São Carlos. |
| ARTICULAÇÃO | `articulacao` | Conexão com parceiros: Onovolab/Toyota, Sebrae, ELI e outros atores do ecossistema. |
| CASO DE USO | `caso-de-uso` | Qual problema concreto de mobilidade o projeto vai resolver, e para quem. |
| PERGUNTA | `pergunta` | A pergunta de pesquisa do TCC. |

### Campos do frontmatter

| Campo | Significado |
|---|---|
| `edicao` | Número sequencial da edição. |
| `data` | Data do rascunho que originou a edição. |
| `tipo` | `piloto`, `semanal` ou `pre-drop` (teste). |
| `aprovada_por` / `aprovada_em` | Quem aprovou e quando. |
| `entradas` / `estudos` | Total de entradas e quantas são estudos acadêmicos. |
| `pendencias` | Selos das entradas da edição. |

### Rótulos das entradas

- **Fonte.** Notícia, norma ou site institucional, com link.
- **Estudo.** Artigo acadêmico, com referência curta e DOI; indica se foi lido o texto completo ou só o resumo.
- **Achado.** O que a fonte diz, com palavras próprias.
- **Implicação.** A pergunta ou o requisito testável que isso gera para o projeto.

Alertas de coerência não ficam aqui: eles vivem só no contexto privado do projeto.

## Estrutura

- `edicoes/AAAA/NN-AAAA-MM-DD-*.md`: edições aprovadas, uma por arquivo.
- `rascunhos/AAAA-MM-DD-*.md`: rascunhos semanais ainda não aprovados.
- `GLOSSARIO.md`: termos aprovados, em ordem alfabética (espelho da aba Glossário).
- `ESTILO.md`: paleta, tipografia, layout, regra de aprovação e papéis visuais do Boletim no Google Docs.
- `ferramentas/lv_docs.py`: gera os comandos de formatação do Google Docs a partir de um modelo do documento.
