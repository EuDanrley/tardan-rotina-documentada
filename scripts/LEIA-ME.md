# Script opcional: Markdown → Word (.docx)

Você **não precisa** deste script. Os modelos .docx já estão prontos em `modelos/`, e você pode copiar o texto da IA direto para eles.

O script serve para quem quer transformar o POP que a IA gerou (em Markdown) num .docx formatado, com tabelas e caixas de seleção, de uma vez.

## Requisitos

- Python 3.11 (testado em 3.11.9 no Windows 11).
- Pacote python-docx 1.2.0.

## Como usar

No terminal, dentro da pasta do repositório:

```
python -m venv .venv
.venv\Scripts\activate          (Windows)   |   source .venv/bin/activate   (Mac/Linux)
pip install -r scripts/requirements.txt
```

1. Salve a resposta da IA num arquivo, por exemplo `meu-pop.md` (copie a resposta e cole num editor de texto; salve com codificação UTF-8).
2. Rode:

```
python scripts/gerar_docx.py meu-pop.md
```

3. O arquivo `meu-pop.docx` aparece ao lado do `.md`. Abra no Word, LibreOffice ou Google Docs.

Para escolher o nome da saída: `python scripts/gerar_docx.py meu-pop.md POP-pedidos-v0.1.docx`.

Para regenerar os modelos e o exemplo deste repositório: `python scripts/gerar_docx.py --todos`.

## O que ele entende

Títulos (`#`, `##`, `###`), parágrafos, citações (`>`), listas (`-` e `1.`), caixas de seleção (`- [ ]`), tabelas com `|` e negrito (`**texto**`). Cada título de nível 1 depois do primeiro começa numa página nova (POP, checklist de execução e checklist de conferência ficam em páginas separadas). Não acessa a internet e não altera o arquivo de origem.

## Como foi testado

Em 02/11/2026, no Windows 11 com Python 3.11.9 e python-docx 1.2.0:

- `python scripts/gerar_docx.py --todos` gerou `modelos/pop-modelo.docx`, `modelos/checklists-modelo.docx`, `modelos/registro-teste-de-mesa.docx` e `exemplos/saida-esperada.docx`.
- `python scripts/gerar_docx.py exemplos/saida-esperada.md <outra pasta>/teste.docx` gerou o arquivo no caminho pedido.
- Arquivo inexistente: mostra "arquivo nao encontrado" e sai com código 1.
- Os .docx foram reabertos com python-docx para conferir títulos, tabelas e caixas de seleção. A aparência no Word não foi conferida visualmente nesta produção.
