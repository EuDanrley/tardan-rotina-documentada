"""Converte um POP/checklist em Markdown (formato deste repositório) para .docx editável.

Uso:
    python scripts/gerar_docx.py caminho/do/arquivo.md            -> cria arquivo.docx ao lado
    python scripts/gerar_docx.py arquivo.md saida.docx             -> escolhe o nome da saída
    python scripts/gerar_docx.py --todos                           -> regenera os .docx de modelos/ e exemplos/

Entende o Markdown simples que a instrução pronta pede: títulos (#, ##, ###),
parágrafos, citações (>), listas (-, 1.), caixas de seleção (- [ ]), tabelas com |
e negrito (**texto**). Não acessa a internet e não altera o arquivo .md de origem.
Requer python-docx (ver scripts/requirements.txt).
"""

import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_BREAK
from docx.shared import Cm, Pt

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVOS_PADRAO = [
    "modelos/pop-modelo.md",
    "modelos/checklists-modelo.md",
    "modelos/registro-teste-de-mesa.md",
    "exemplos/saida-esperada.md",
]

NEGRITO = re.compile(r"(\*\*[^*]+\*\*)")


def escrever_com_negrito(paragrafo, texto, negrito_total=False):
    texto = texto.replace("`", "")
    for parte in NEGRITO.split(texto):
        if not parte:
            continue
        if parte.startswith("**") and parte.endswith("**"):
            run = paragrafo.add_run(parte[2:-2])
            run.bold = True
        else:
            run = paragrafo.add_run(parte)
            run.bold = negrito_total or None


def celulas(linha):
    linha = linha.strip()
    if linha.startswith("|"):
        linha = linha[1:]
    if linha.endswith("|"):
        linha = linha[:-1]
    return [c.strip() for c in linha.split("|")]


def eh_separador(linha):
    return bool(re.fullmatch(r"\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?", linha.strip()))


def adicionar_tabela(doc, linhas):
    linhas = [l for l in linhas if not eh_separador(l)]
    dados = [celulas(l) for l in linhas]
    colunas = max(len(d) for d in dados)
    tabela = doc.add_table(rows=len(dados), cols=colunas)
    tabela.style = "Table Grid"
    for i, linha in enumerate(dados):
        for j in range(colunas):
            texto = linha[j] if j < len(linha) else ""
            celula = tabela.cell(i, j)
            celula.text = ""
            escrever_com_negrito(celula.paragraphs[0], texto, negrito_total=(i == 0))
    doc.add_paragraph()


def converter(origem: Path, destino: Path):
    linhas = origem.read_text(encoding="utf-8").splitlines()
    doc = Document()
    estilo = doc.styles["Normal"]
    estilo.font.name = "Calibri"
    estilo.font.size = Pt(11)
    for secao in doc.sections:
        secao.left_margin = secao.right_margin = Cm(2)
        secao.top_margin = secao.bottom_margin = Cm(2)

    titulos_nivel1 = 0
    i = 0
    while i < len(linhas):
        linha = linhas[i].rstrip()
        bruta = linha.strip()

        if not bruta:
            i += 1
            continue

        if bruta.startswith("|"):
            bloco = []
            while i < len(linhas) and linhas[i].strip().startswith("|"):
                bloco.append(linhas[i])
                i += 1
            adicionar_tabela(doc, bloco)
            continue

        titulo = re.match(r"^(#{1,3})\s+(.*)$", bruta)
        if titulo:
            nivel = len(titulo.group(1))
            if nivel == 1:
                titulos_nivel1 += 1
                if titulos_nivel1 > 1:
                    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
            doc.add_heading(titulo.group(2).replace("**", "").replace("`", ""), level=nivel)
        elif bruta.startswith(">"):
            p = doc.add_paragraph()
            escrever_com_negrito(p, bruta.lstrip("> ").strip())
            for run in p.runs:
                run.italic = True
        elif re.match(r"^- \[[ xX]\]\s+", bruta):
            marcado = bruta[3] in "xX"
            texto = re.sub(r"^- \[[ xX]\]\s+", "", bruta)
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.5)
            p.add_run("☒ " if marcado else "☐ ")
            escrever_com_negrito(p, texto)
        elif bruta.startswith("- "):
            p = doc.add_paragraph(style="List Bullet")
            escrever_com_negrito(p, bruta[2:])
        elif re.match(r"^\d+\.\s+", bruta):
            numero, texto = re.match(r"^(\d+)\.\s+(.*)$", bruta).groups()
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.5)
            p.add_run(f"{numero}. ")
            escrever_com_negrito(p, texto)
        else:
            p = doc.add_paragraph()
            escrever_com_negrito(p, bruta)
        i += 1

    destino.parent.mkdir(parents=True, exist_ok=True)
    doc.save(destino)
    return destino


def main(argumentos):
    if not argumentos or argumentos[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argumentos[0] == "--todos":
        for relativo in ARQUIVOS_PADRAO:
            origem = RAIZ / relativo
            destino = converter(origem, origem.with_suffix(".docx"))
            print(f"gerado: {destino.relative_to(RAIZ)}")
        return 0
    origem = Path(argumentos[0])
    if not origem.exists():
        print(f"arquivo nao encontrado: {origem}")
        return 1
    destino = Path(argumentos[1]) if len(argumentos) > 1 else origem.with_suffix(".docx")
    converter(origem, destino)
    print(f"gerado: {destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
