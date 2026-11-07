# Rotina documentada — tire a rotina da sua cabeça

A IA entrevista você com poucas perguntas por vez e entrega um **POP (procedimento operacional padrão)**, um **checklist de execução** e um **checklist de conferência** que outra pessoa da sua equipe consegue seguir.

## Use em 5 minutos

1. **Baixe:** botão verde **Code → Download ZIP** e descompacte a pasta.
2. Abra `instrucoes/instrucao-pronta.md`, copie o texto entre `--- INÍCIO ---` e `--- FIM ---` e cole no ChatGPT, no Claude ou no Gemini.
3. Responda às perguntas. São 6 blocos curtos; pode responder "não sei" que a IA marca para confirmar depois.
4. Confirme o resumo que a IA mostrar. Ela gera o POP e os dois checklists.
5. Leia as **Lacunas A CONFIRMAR**, passe pelo `CHECKLIST.md` e cole o resultado em `modelos/pop-modelo.docx` (ou em `modelos/pop-modelo.md`).

Quer ver como fica antes de começar? Abra `exemplos/saida-esperada.docx` (exemplo fictício de uma papelaria).

## O que você precisa

- Uma conta no ChatGPT, no Claude ou no Gemini. O plano gratuito serve para a instrução pronta.
- Um tempo sem interrupção para responder à entrevista sobre uma rotina (quanto maior a rotina, mais blocos de perguntas).
- Para abrir os modelos: Word, LibreOffice ou Google Docs.
- Opcional: deixar a instrução salva num Projeto (ChatGPT/Claude) ou como skill (Claude/Gemini) — veja `instrucoes/projeto-ia.md`. Limites e planos foram conferidos em 02/11/2026.
- Opcional: Python 3.11 para converter o texto da IA em .docx com o script (`scripts/LEIA-ME.md`).

## Arquivos do repositório

| Arquivo | Para que serve |
|---|---|
| `instrucoes/instrucao-pronta.md` | Texto para colar na IA. Faz a entrevista e gera os documentos. |
| `instrucoes/projeto-ia.md` | Como deixar a instrução salva no ChatGPT, no Claude ou no Gemini. |
| `instrucoes/claude-skill/rotina-documentada/SKILL.md` | A mesma instrução em formato de skill (serve no Claude e no Gemini). |
| `modelos/pop-modelo.docx` e `.md` | Modelo de POP em branco. |
| `modelos/checklists-modelo.docx` e `.md` | Modelos de checklist de execução e de conferência. |
| `modelos/registro-teste-de-mesa.docx` e `.md` | Folha para registrar o teste com outra pessoa. |
| `exemplos/entrada-ficticia.md` | Entrevista de exemplo (empresa fictícia). |
| `exemplos/saida-esperada.md` e `.docx` | POP e checklists de referência para essa entrevista. |
| `exemplos/teste-api-gemini-2026-11-02.md` | Registro do teste da instrução feito pela equipe via API. |
| `scripts/gerar_docx.py` | Opcional: converte o texto da IA (Markdown) em .docx. |
| `CHECKLIST.md` | Conferência antes de entregar o POP para a equipe. |

## Quer entender ou adaptar?

As aulas do módulo 05 no Pro mostram a solução funcionando (aula 1), como adaptar a entrevista para rotinas difíceis e fazer o teste de mesa (aula 2) e como tudo funciona por dentro, versões, treinamento e automação (aula 3). Você não precisa assistir para usar.

## Limites

- A IA organiza o que **você** disser. Se a rotina tiver regra que só existe na sua cabeça e você não falar, ela não vai aparecer — vai virar lacuna, no máximo.
- A IA pode enfeitar passos com detalhes plausíveis que você não disse. No nosso teste isso aconteceu; por isso a instrução proíbe e o `CHECKLIST.md` manda conferir.
- O POP só está pronto depois do teste de mesa com outra pessoa. Antes disso é rascunho.
- Não coloque senhas nem dados de clientes na conversa. Dados pessoais em ferramentas de IA estão sujeitos à LGPD; confira a política da sua empresa. Isto não é orientação jurídica.
- Este repositório não cria tarefas, não envia mensagens e não se conecta a sistemas da sua empresa.

## Licença

Veja `LICENCA.md`. Material da Comunidade Tardan para uso de membros ativos em seus próprios negócios.
