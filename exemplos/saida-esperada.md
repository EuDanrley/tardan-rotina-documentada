# POP — Separar e enviar pedidos recebidos por e-mail

> Exemplo 100% fictício (Papelaria Ponto Fictício). Saída de referência escrita pela equipe Tardan a partir de `entrada-ficticia.md`, para mostrar o padrão que a IA deve seguir. Não é cópia de uma resposta gerada pela IA.

| Campo | Conteúdo |
|---|---|
| Versão | 0.1 (rascunho) |
| Data | A CONFIRMAR |
| Dono do procedimento | Carla (dona) |
| Quem executa | Rafael (balcão) |
| Quem confere | Carla, no fim do dia |
| Situação | Rascunho — ainda não testado por outra pessoa |

## 1. Objetivo

Garantir que o cliente receba o material certo e saiba que o pedido foi enviado.

## 2. Quando usar (gatilho e frequência)

- Gatilho: pedido novo no e-mail pedidos@papelaria-ficticia.example.
- Frequência: todo dia útil, em duas verificações: de manhã e depois do almoço.

## 3. Entradas, materiais e acessos

| Item | Onde fica | Quem libera |
|---|---|---|
| E-mail de pedidos | pedidos@papelaria-ficticia.example | Carla — forma de acesso A CONFIRMAR (conta própria ou acesso compartilhado) |
| Planilha "Pedidos 2026" | Google Planilhas | Carla |
| Caixas e envelopes | Depósito dos fundos | — |
| Impressora de etiquetas | A CONFIRMAR (local) | — |
| Confirmação de pagamento | A CONFIRMAR — Rafael não terá acesso ao banco | Carla |

## 4. Passo a passo

| Nº | Ação | Como / onde | Conferência do passo |
|---|---|---|---|
| 1 | Abrir o e-mail de pedidos | Verificar pedidos novos de manhã e depois do almoço | Todos os pedidos novos foram abertos |
| 2 | Confirmar que o pedido está pago | Forma de consulta A CONFIRMAR (proposta da dona: coluna "pago" na planilha, ainda não adotada) | Sem confirmação de pagamento, não seguir |
| 3 | Lançar o pedido na planilha | "Pedidos 2026": data, número do pedido, itens e forma de envio (Correios ou motoboy) | Linha preenchida com os quatro campos |
| 4 | Separar os itens | Estoque | Todos os itens do pedido estão separados |
| 5 | Conferir item por item com o e-mail | Comparar quantidade e descrição | Nenhum item diferente ou faltando |
| 6 | Imprimir o e-mail do pedido e colocar dentro da caixa | Impressora (local A CONFIRMAR) | Via impressa dentro da caixa |
| 7 | Embalar | Caixas e envelopes do depósito | Embalagem fechada |
| 8 | Imprimir e colar a etiqueta | Impressora de etiquetas | Etiqueta legível e colada |
| 9 | Enviar | Correios: levar na agência à tarde, antes do horário limite (A CONFIRMAR). Motoboy: chamar pelo aplicativo (qual aplicativo e conta: A CONFIRMAR) | Pacote entregue à agência ou ao motoboy |
| 10 | Atualizar a planilha | Correios: registrar o código de rastreio. Mudar a situação para "enviado" | Situação "enviado"; código preenchido quando for Correios |
| 11 | Responder o e-mail do cliente | Correios: enviar o código de rastreio. Motoboy: avisar que saiu para entrega | E-mail enviado, sem prometer prazo |

## 5. Exceções e encaminhamento

| Situação | O que fazer | Encaminhar para |
|---|---|---|
| Item em falta no estoque | Não responder o cliente. Parar o pedido | Carla decide (troca por item parecido ou devolução do valor do item). Canal para avisar: A CONFIRMAR |
| Endereço incompleto | Não enviar. Existe um texto pronto pedindo o endereço completo (local A CONFIRMAR) | A CONFIRMAR se Rafael envia o texto sozinho ou passa para Carla |
| Cliente pede entrega no mesmo dia | Não prometer prazo nenhum | Carla |
| Pagamento não confirmado | Não separar nem enviar | Carla |
| Bairro sem certeza se é motoboy ou Correios | Não decidir sozinho | Carla — lista de bairros atendidos por motoboy A CONFIRMAR |

## 6. Critério de pronto

O pedido está como "enviado" na planilha, com código de rastreio quando foi pelos Correios, e o cliente recebeu o e-mail de envio.

## 7. Riscos e cuidados

- Nunca enviar pedido sem pagamento confirmado.
- Nunca enviar item diferente do pedido.
- Nunca dar desconto nem prometer prazo de entrega.
- Não esquecer a via impressa do e-mail dentro da caixa (já houve reclamação de cliente por isso).

## 8. Lacunas A CONFIRMAR

1. Como o Rafael vai saber que o pedido está pago — Carla.
2. Como o Rafael vai acessar o e-mail de pedidos (conta própria ou acesso compartilhado) — Carla.
3. Lista de bairros atendidos por motoboy — Carla.
4. Horário limite para postar na agência dos Correios — Carla (consultar a agência).
5. Qual aplicativo de motoboy e qual conta usar — Carla.
6. Onde está o texto pronto para endereço incompleto e se o Rafael pode enviá-lo sozinho — Carla.
7. Por qual canal o Rafael avisa a Carla sobre exceções — Carla.
8. Local da impressora usada para a via do pedido — Carla.
9. Data desta versão — Carla.
10. Em que momento imprimir a via do pedido (a entrevista não diz; o passo 6 é uma sugestão de posição) — Carla.

## 9. Histórico de versões

| Versão | Data | O que mudou | Quem aprovou |
|---|---|---|---|
| 0.1 | A CONFIRMAR | Primeira versão, gerada a partir da entrevista | A CONFIRMAR |

# Checklist de execução — Separar e enviar pedidos

Data: ____________ Executado por: ____________ Versão do POP: 0.1

- [ ] Abri o e-mail de pedidos e vi todos os pedidos novos
- [ ] Confirmei que cada pedido está pago (como indicado no POP)
- [ ] Lancei na planilha: data, número, itens e forma de envio
- [ ] Separei os itens
- [ ] Conferi item por item com o e-mail
- [ ] Coloquei a via impressa do e-mail dentro da caixa
- [ ] Embalei e colei a etiqueta
- [ ] Enviei pelos Correios ou motoboy
- [ ] Registrei o código de rastreio (Correios) e mudei para "enviado"
- [ ] Respondi o cliente sem prometer prazo
- [ ] Avisei a Carla de toda exceção (falta de item, endereço, pedido urgente, pagamento)

Observações: ________________________________________________

# Checklist de conferência — Separar e enviar pedidos

Data: ____________ Conferido por: ____________

- [ ] Todo pedido "enviado" na planilha tinha pagamento confirmado
- [ ] Pedidos dos Correios têm código de rastreio na planilha
- [ ] Todo pedido "enviado" tem e-mail de resposta ao cliente
- [ ] Nenhum e-mail enviado promete prazo ou desconto
- [ ] Exceções do dia foram avisadas e têm decisão
- [ ] Nenhum pedido novo do dia ficou sem lançamento na planilha

Resultado: [ ] Aprovado  [ ] Devolvido — motivo: ____________________

# Próximo passo: teste de mesa

Peça ao Rafael para processar um pedido de exemplo seguindo só este POP e o checklist, falando em voz alta o que faz. A Carla observa sem ajudar e anota no `modelos/registro-teste-de-mesa.md` onde ele travou. Cada travamento vira um ajuste na versão 0.2.

O que ainda impede o Rafael de executar sem ajuda: a forma de confirmar pagamento, o acesso ao e-mail de pedidos e a lista de bairros do motoboy.
