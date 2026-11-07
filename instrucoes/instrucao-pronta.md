# Instrução pronta — Rotina documentada

Copie tudo o que está entre as linhas `--- INÍCIO ---` e `--- FIM ---` e cole como primeira mensagem no ChatGPT, no Claude ou no Gemini. Depois é só responder às perguntas. Não precisa instalar nada.

Dica: se você já tem a rotina escrita (um áudio transcrito, um texto, uma lista), cole junto depois da instrução. A IA aproveita o que você mandou e pergunta só o que faltar.

--- INÍCIO ---

Você vai me entrevistar para documentar uma rotina da minha empresa, de modo que outra pessoa consiga executá-la sem depender de mim. No final, você vai gerar um POP (procedimento operacional padrão), um checklist de execução e um checklist de conferência.

COMO CONDUZIR A ENTREVISTA

1. Pergunte em blocos, nesta ordem. Faça no máximo 3 perguntas por vez, curtas e objetivas, e espere minha resposta antes de seguir.
   - Bloco 1 — Objetivo e gatilho: qual é a rotina, para que serve, o que faz ela começar, com que frequência acontece, quem faz hoje e quem vai passar a fazer.
   - Bloco 2 — Entradas, materiais e acessos: o que a pessoa precisa ter em mãos, onde isso fica, quais sistemas, planilhas ou ferramentas usa, quais acessos precisa e quem libera. Pergunte qual acesso é necessário; nunca peça senha.
   - Bloco 3 — Passos como acontecem hoje: peça para eu descrever a última vez que fiz, do começo ao fim. Se houver salto entre um passo e outro, pergunte o que acontece no meio.
   - Bloco 4 — Decisões e exceções: em que ponto a pessoa precisa decidir alguma coisa, com que critério, o que fazer quando algo sai do normal e para quem encaminhar.
   - Bloco 5 — Critério de pronto e conferência: como saber que a rotina terminou certo, quem confere, o que confere e quando.
   - Bloco 6 — Riscos: o que não pode acontecer de jeito nenhum, o que já deu errado antes e que cuidado a pessoa precisa ter.
2. Antes do primeiro bloco, diga em uma frase como a entrevista vai funcionar (6 blocos, poucas perguntas por vez, posso responder "não sei").
3. Se eu já tiver mandado uma descrição da rotina, aproveite o que estiver nela e pergunte só o que faltar em cada bloco.
4. Se eu responder de forma vaga ("depende", "a gente vê na hora", "normalmente"), faça uma pergunta de acompanhamento: depende de quê, quem vê, o que acontece quando não é o normal.
5. Se eu não souber ou preferir não responder, registre como A CONFIRMAR e siga para a próxima pergunta.
6. Ao fim dos 6 blocos, mostre um resumo do que entendeu, em tópicos curtos, e pergunte: "Está correto? Falta alguma coisa ou tem algo errado?". Só gere os documentos depois que eu confirmar. Se eu pedir para gerar antes, gere mantendo as lacunas marcadas.

REGRAS DE VERDADE

- Use somente o que eu disser. Não invente sistemas, ferramentas, permissões, nomes de pessoas, prazos, horários, valores, quantidades, políticas ou etapas.
- Tudo que faltar ou estiver incerto vira A CONFIRMAR, com a pergunta que precisa ser respondida.
- Não acrescente materiais, ações ou detalhes que eu não disse (por exemplo: "fechar com fita", "guardar comprovante"). Se achar que falta um passo, coloque como sugestão em "Lacunas A CONFIRMAR", não no passo a passo.
- Mantenha a ordem dos passos como eu contei. Se achar que outra ordem é melhor, sugira nas lacunas.
- Não transforme hábito em regra. Se eu disser "às vezes" ou "quase sempre", escreva assim e marque o critério como A CONFIRMAR.
- Se duas respostas minhas se contradisserem, não escolha uma: aponte o conflito e pergunte.
- Não peça nem registre senhas, dados de clientes, CPF, telefone ou qualquer dado pessoal. Se aparecer algum, substitua por uma descrição genérica (por exemplo: "e-mail do cliente") e me avise.
- Escreva para alguém que nunca fez essa rotina e não pode me perguntar nada. Cada passo começa com um verbo e descreve uma ação só.
- Português do Brasil, frases curtas, sem jargão.

FORMATO DA ENTREGA (em Markdown, nesta ordem)

# POP — [nome da rotina]

| Campo | Conteúdo |
|---|---|
| Versão | 0.1 (rascunho) |
| Data | [data de hoje, se eu informar; senão A CONFIRMAR] |
| Dono do procedimento | [quem responde pela rotina] |
| Quem executa | [função ou pessoa] |
| Quem confere | [função ou pessoa] |
| Situação | Rascunho — ainda não testado por outra pessoa |

## 1. Objetivo
## 2. Quando usar (gatilho e frequência)
## 3. Entradas, materiais e acessos
(lista: item — onde fica — quem libera)
## 4. Passo a passo
| Nº | Ação | Como / onde | Conferência do passo |
## 5. Exceções e encaminhamento
| Situação | O que fazer | Encaminhar para |
## 6. Critério de pronto
## 7. Riscos e cuidados
## 8. Lacunas A CONFIRMAR
(lista numerada: o que falta — quem pode responder)
## 9. Histórico de versões
| Versão | Data | O que mudou | Quem aprovou |

# Checklist de execução — [nome da rotina]
Data: ____ Executado por: ____
- [ ] (um item por passo do POP, em linguagem de ação)

# Checklist de conferência — [nome da rotina]
Data: ____ Conferido por: ____
- [ ] (o que quem revisa deve olhar para dizer que ficou certo)
Resultado: [ ] Aprovado  [ ] Devolvido — motivo: ____

# Próximo passo: teste de mesa
Explique em 3 linhas: peça a outra pessoa (não o dono) para executar seguindo só o POP, enquanto alguém observa sem ajudar e anota onde ela travou. Os pontos de travamento viram ajustes na versão seguinte.

Ao final, liste em uma frase o que ainda impede alguém de executar sem ajuda (as lacunas mais importantes).

Comece agora pelo Bloco 1.

--- FIM ---

## Depois que a IA gerar

1. Leia a seção **8. Lacunas A CONFIRMAR** e responda o que der. Peça para a IA atualizar o POP.
2. Copie o resultado para o modelo `modelos/pop-modelo.docx` (ou use o script em `scripts/` para converter o texto em .docx).
3. Faça o teste de mesa com `modelos/registro-teste-de-mesa.md`.
4. Confira com `CHECKLIST.md` antes de entregar o POP para a equipe.
