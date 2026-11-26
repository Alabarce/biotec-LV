# Estilo do Boletim LV

## Layout do Doc

O Doc tem duas abas. O quadro de status inclui a linha "Selos." com o significado de cada selo.

- **Boletim** (aba principal), de cima para baixo: título e subtítulo; quadro de status (Status, Definido, Em aberto, Como aprovar, Feedback); rascunhos pendentes, do mais novo para o mais antigo; edições publicadas, da mais nova para a mais antiga.
- **Glossário**: título, subtítulo e os termos aprovados em ordem alfabética. Termos propostos ficam no rascunho até a aprovação.

Cada rascunho: título "Rascunho da semana • DD/MM/AAAA" (h1draft), nota de aprovação, checkbox "Aprovar este rascunho", entradas e, se houver, "Glossário (proposto)".
Cada edição: título "Edição NN • DD/MM/AAAA" (h1), e cada entrada com título (h2), selo e cartão.

Alertas de coerência não aparecem no Boletim nem no git. Ficam só no Contexto privado, numa seção "Alertas de coerência" com um bloco por data (h2), do mais recente para o mais antigo, cada alerta no papel alert.

O glossário aprovado fica na aba Glossário e em GLOSSARIO.md, em ordem alfabética.

Aprovação por checkbox (lista BULLET_CHECKBOX do Docs):
- "Aprovar este rascunho", logo abaixo da nota de cada rascunho, aprova tudo.
- A linha do selo de cada entrada é um checkbox e aprova só aquela entrada.
- Cada termo do "Glossário (proposto)" é um checkbox e aprova só aquele termo.
- Entrada apagada = descartada. Item sem marcação continua pendente.
- Na edição publicada e na aba Glossário, nada tem checkbox.

A API do Docs não informa se um checkbox está marcado. O estado se lê pelo read_file_content do Drive: com includeComments=true, item marcado vem como "- [x]" e desmarcado como "- [ ]"; sem includeComments, marcado vem riscado ("~~") e desmarcado vem limpo. Na exportação em PDF o checkbox aparece desenhado marcado ou vazio.

Entradas de estudo acadêmico usam o rótulo "Estudo." no lugar de "Fonte.", com referência curta (AUTOR et al., ano, revista, volume) e o DOI como link, e terminam com "(lido o resumo)" ou "(lido o texto completo)".

O Boletim vive no Google Docs. Os estilos nomeados do Docs não podem ser alterados pela API, então cada parágrafo recebe a formatação direto. A ferramenta `ferramentas/lv_docs.py` aplica tudo de uma vez a partir de um modelo do documento.

## Paleta

| Uso | Cor |
|---|---|
| Títulos, rótulos, links, barras dos cartões | `#0F4C5C` (petróleo) |
| Rótulo "Implicação.", título do rascunho, alertas | `#B45309` (âmbar) |
| Texto do corpo | `#1F2933` |
| Subtítulo e notas | `#5F6B73` |
| Fundo das etiquetas | `#DCEFF1` |
| Fundo do quadro de status | `#EEF6F7` |
| Fundo da caixa de alertas | `#FFF4E5` |

## Tipografia

- Títulos e cabeçalhos: **Lora** (título 30 pt, H1 19 pt, H2 14 pt), sem negrito.
- Corpo: **Lato** 11 pt. Status e alertas em 10 pt. Etiquetas em 8 pt, negrito.

## Papéis

| Papel | Onde aparece | Aparência |
|---|---|---|
| `title`, `subtitle` | Topo | Lora petróleo e Lato cinza |
| `status` | Quadro logo abaixo do subtítulo | Fundo petróleo claro, barra petróleo à esquerda, rótulo em negrito |
| `h1` | Data da entrada publicada, Glossário | Lora 19 pt petróleo |
| `h1draft` | "Rascunho da semana • data" | Lora 19 pt âmbar |
| `h2` | Título de cada entrada do rascunho, "Glossário (proposto)", "Alertas de coerência" | Lora 14 pt petróleo |
| `tag` | Linha logo abaixo do título da entrada | Selo em caixa alta: MÉTRICA, LABORATÓRIO, ARTICULAÇÃO, CASO DE USO, PERGUNTA |
| `entry` | Fonte, Achado, Implicação | Cartão com barra petróleo à esquerda. Rótulo em negrito petróleo, "Implicação." em âmbar. A linha da Fonte é toda link |
| `gloss` | Termos do glossário | Termo em negrito petróleo |
| `note` | Nota do rascunho | Lato 10 pt itálico cinza |
| `alert` | Alertas de coerência | Caixa âmbar clara com barra âmbar, rótulo em negrito âmbar |

Recuo dos cartões e caixas: `indentStart` e `indentFirstLine` de 12 pt. No Docs, o recuo da primeira linha é absoluto; sem ele a primeira linha fica desalinhada das outras.

## Texto

Nunca usar travessão (em-dash) no texto escrito pelo boletim.
