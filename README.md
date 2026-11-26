# LV • Boletim de pesquisa

Mobilidade ativa e tecnologias assistivas. Catálogo das edições semanais do boletim, de 2026 a 2027.

Cada entrada liga **fonte ou estudo → achado → implicação**: o que uma notícia, norma ou estudo diz, e que pergunta ou requisito testável isso gera para o projeto (sistema embarcado, processamento de dados e aplicativo de monitoramento). Estudos acadêmicos trazem a referência no padrão ABNT e o DOI, prontos para o TCC.

## Como o catálogo cresce

1. **Sábado de manhã:** sai o rascunho da semana, com levantamento e checagem de coerência. Ele entra no topo do Boletim (Google Docs) e em `rascunhos/`, num commit `rascunho:`.
2. **Aprovação:** um comentário "aprovado" no título do rascunho (ou numa entrada) libera a publicação. O rascunho aprovado vira uma edição em `edicoes/AAAA/`, num commit `aprovação:` do responsável, e os termos novos vão para a aba Glossário.

O histórico de commits é o registro do trabalho contínuo: um rascunho por semana e uma aprovação por edição.

## Edições

### 2026

| Nº | Data | Entradas | Pendências | Arquivo |
|---|---|---|---|---|
| 00 | 19/11/2026 | 1 (piloto) | métrica | [piloto](edicoes/2026/00-2026-11-19-piloto.md) |

## Rascunhos aguardando aprovação

| Data | Entradas | Pendências | Arquivo |
|---|---|---|---|
| 26/11/2026 | 3, sendo 2 estudos (pré-drop de teste) | métrica, articulação | [pré-drop 2](rascunhos/2026-11-26-pre-drop-2.md) |
| 24/11/2026 | 3 (pré-drop de teste) | articulação, laboratório, métrica | [pré-drop](rascunhos/2026-11-24-pre-drop.md) |

## Estrutura

- `edicoes/AAAA/NN-AAAA-MM-DD-*.md`: edições aprovadas, uma por arquivo.
- `rascunhos/AAAA-MM-DD-*.md`: rascunhos semanais ainda não aprovados.
- `ESTILO.md`: paleta, tipografia, layout e papéis visuais do Boletim no Google Docs.
- `ferramentas/lv_docs.py`: gera os comandos de formatação do Google Docs a partir de um modelo do documento.
