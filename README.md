# LV • Boletim de pesquisa

Mobilidade ativa e tecnologias assistivas. Catálogo das edições semanais do boletim, de 2026 a 2027.

Cada entrada liga **fonte → achado → implicação**: o que uma fonte diz, e que pergunta ou requisito testável isso gera para o projeto (sistema embarcado, processamento de dados e aplicativo de monitoramento).

## Como o catálogo cresce

1. **Sábado de manhã:** sai o rascunho da semana, com levantamento e checagem de coerência. Ele entra em `rascunhos/` num commit `rascunho:`.
2. **Aprovação:** depois da revisão, o rascunho aprovado vira uma edição em `edicoes/AAAA/` num commit `aprovação:` do responsável.

O histórico de commits é o registro do trabalho contínuo: um rascunho por semana e uma aprovação por edição.

## Edições

### 2026

| Nº | Data | Entradas | Pendências | Arquivo |
|---|---|---|---|---|
| 00 | 19/11/2026 | 1 (piloto) | métrica | [piloto](edicoes/2026/00-2026-11-19-piloto.md) |

## Rascunhos aguardando aprovação

| Data | Entradas | Pendências | Arquivo |
|---|---|---|---|
| 24/11/2026 | 3 (pré-drop de teste) | articulação, laboratório, métrica | [pré-drop](rascunhos/2026-11-24-pre-drop.md) |

## Estrutura

- `edicoes/AAAA/NN-AAAA-MM-DD-*.md`: edições aprovadas, uma por arquivo.
- `rascunhos/AAAA-MM-DD-*.md`: rascunhos semanais ainda não aprovados.
- `ESTILO.md`: paleta, tipografia e papéis visuais do Boletim no Google Docs.
- `ferramentas/lv_docs.py`: gera os comandos de formatação do Google Docs a partir de um modelo do documento.
