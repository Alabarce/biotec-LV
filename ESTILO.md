# Estilo do Boletim LV

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
