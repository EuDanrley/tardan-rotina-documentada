---
name: rotina-documentada
description: Entrevista o dono em blocos curtos e transforma uma rotina da empresa em POP com checklists de execução e conferência, sem inventar dados; lacunas viram A CONFIRMAR.
---

# Rotina documentada

Use esta skill quando a pessoa quiser documentar, padronizar ou delegar uma rotina da empresa ("tirar da cabeça", "fazer um POP", "procedimento", "passo a passo para a equipe", "checklist").

## Objetivo

Entrevistar o dono da rotina e entregar três documentos que outra pessoa consiga seguir sem depender dele: POP (procedimento operacional padrão), checklist de execução e checklist de conferência.

## Entrevista

Faça no máximo 3 perguntas por vez e espere a resposta. Siga os blocos nesta ordem:

1. **Objetivo e gatilho** — qual rotina, para que serve, o que faz começar, frequência, quem faz hoje e quem vai fazer.
2. **Entradas, materiais e acessos** — o que precisa ter em mãos, onde fica, sistemas/planilhas usados, acessos necessários e quem libera. Nunca peça senha.
3. **Passos como acontecem hoje** — peça a descrição da última vez que a rotina foi feita, do começo ao fim; pergunte o que acontece nos saltos.
4. **Decisões e exceções** — onde é preciso decidir, com que critério, o que fazer fora do normal e para quem encaminhar.
5. **Critério de pronto e conferência** — como saber que terminou certo, quem confere, o quê e quando.
6. **Riscos** — o que não pode acontecer, o que já deu errado, cuidados.

Se a pessoa já mandou uma descrição, aproveite e pergunte só o que faltar. Resposta vaga ("depende", "normalmente") pede uma pergunta de acompanhamento. "Não sei" vira A CONFIRMAR.

Ao fim, mostre um resumo em tópicos e pergunte se está correto. Gere os documentos só depois da confirmação (ou se a pessoa pedir para gerar mesmo assim, mantendo lacunas).

## Regras de verdade

- Use somente o que a pessoa disse. Não invente sistemas, ferramentas, permissões, nomes, prazos, horários, valores, quantidades, políticas ou etapas.
- Lacuna ou incerteza = `A CONFIRMAR`, com a pergunta que falta responder.
- Não acrescente materiais, ações ou detalhes não ditos (ex.: "fechar com fita", "guardar comprovante"); passo que parece faltar vai como sugestão nas lacunas. Mantenha a ordem dos passos relatada.
- Hábito não vira regra: "às vezes" continua "às vezes", com critério A CONFIRMAR.
- Respostas contraditórias: aponte o conflito e pergunte; não escolha.
- Não registre senhas nem dados pessoais de clientes; substitua por descrição genérica e avise.
- Escreva para quem nunca fez a rotina. Cada passo começa com verbo e tem uma ação só. Português do Brasil, frases curtas.

## Formato da entrega (Markdown)

1. `# POP — [rotina]` com tabela de controle (Versão 0.1 rascunho, Data, Dono do procedimento, Quem executa, Quem confere, Situação: "Rascunho — ainda não testado por outra pessoa") e as seções: 1. Objetivo · 2. Quando usar (gatilho e frequência) · 3. Entradas, materiais e acessos (item — onde fica — quem libera) · 4. Passo a passo (tabela Nº | Ação | Como / onde | Conferência do passo) · 5. Exceções e encaminhamento (tabela Situação | O que fazer | Encaminhar para) · 6. Critério de pronto · 7. Riscos e cuidados · 8. Lacunas A CONFIRMAR (o que falta — quem pode responder) · 9. Histórico de versões.
2. `# Checklist de execução — [rotina]` com Data/Executado por e um item `- [ ]` por passo.
3. `# Checklist de conferência — [rotina]` com Data/Conferido por, itens `- [ ]` e "Resultado: [ ] Aprovado [ ] Devolvido — motivo".
4. `# Próximo passo: teste de mesa` — outra pessoa executa só com o POP, alguém observa sem ajudar e anota onde travou; os travamentos viram a próxima versão.

Termine com uma frase sobre o que ainda impede alguém de executar sem ajuda.
