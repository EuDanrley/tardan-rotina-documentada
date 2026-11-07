# Teste via API do Gemini — 02/11/2026

> **Teste via API, não na interface do app.** Feito pela equipe Tardan com dados 100% fictícios (Papelaria Ponto Fictício). Não substitui o teste no ChatGPT, no Claude ou no app do Gemini, que ainda não foi feito.

## Como foi feito

- Ferramenta: servidor MCP `gemini-audio`, função `gemini_chat` (uma chamada por teste, sem histórico).
- Modelo: o padrão da ferramenta. A descrição da ferramenta indica `gemini-3.8-flash`; a resposta não informa o modelo usado, então o nome exato é **não confirmado**. Temperatura 0,7.
- Instrução: o texto de `instrucoes/instrucao-pronta.md` **na versão anterior** a este teste (sem as duas regras adicionadas depois; ver "O que mudou por causa do teste").
- Teste A — abertura: só a instrução (sem o bloco de formato), para ver se a IA começa pelo Bloco 1 com no máximo 3 perguntas.
- Teste B — geração: instrução completa + as respostas da dona para os 6 blocos (resumo de `entrada-ficticia.md`) + "confirmo que está correto: gere os documentos agora, sem novas perguntas". Serve para conferir se a IA marca lacunas e se inventa algo.

## Teste A — resposta da IA (literal)

> Nossa entrevista terá 6 blocos com até 3 perguntas curtas por vez, e você pode responder "não sei" sempre que não tiver certeza de algo.
>
> Vamos começar pelo **Bloco 1 — Objetivo e gatilho**:
>
> 1. Qual é o nome dessa rotina e para que ela serve?
> 2. O que faz essa rotina começar (qual é o gatilho) e com que frequência ela acontece?
> 3. Quem executa essa rotina hoje e quem vai passar a fazer?

Resultado: **conforme** — uma frase de explicação, Bloco 1, 3 perguntas.

## Teste B — avaliação da saída

A saída completa está no fim deste arquivo. Conferência feita pela equipe, comparando com `saida-esperada.md`:

| Critério | Resultado |
|---|---|
| Gerou POP, checklist de execução, checklist de conferência e teste de mesa no formato pedido | Conforme |
| Lacunas marcadas como A CONFIRMAR (acesso ao e-mail, sinal de pagamento, horário dos Correios, bairros do motoboy, aplicativo, texto de endereço, local da impressora, data) | Conforme — 9 lacunas listadas |
| Não inventou preço, prazo, horário, valor ou nome de pessoa | Conforme |
| Exceções encaminhadas para a dona, sem o executor responder o cliente | Conforme |
| Manteve "às vezes" como incerto (troca ou devolução) | Conforme — virou lacuna 8 |
| Não acrescentou detalhes não ditos | **Não conforme** — acrescentou "vedar com fita adesiva", "comprovante de postagem", "separar os itens que houver" na falta de produto, "acesso físico ao depósito" e uma lacuna sobre "qual agência" |
| Manteve a ordem relatada | **Parcial** — moveu "imprimir a via do pedido" para antes do lançamento na planilha |

Conclusão: a estrutura e as lacunas funcionaram; a IA ainda enfeitou alguns passos com detalhes plausíveis que a dona não disse. Isso confirma que a revisão humana com o `CHECKLIST.md` é obrigatória.

## O que mudou por causa do teste

Foram acrescentadas duas regras na instrução e na skill:

- Não acrescentar materiais, ações ou detalhes não ditos; passo que parece faltar vai como sugestão nas lacunas.
- Manter a ordem dos passos relatada; outra ordem só como sugestão.

A instrução com essas regras **não foi testada de novo**. Próximo teste recomendado: repetir o Teste B no ChatGPT, no Claude e no app do Gemini e conferir a linha "não acrescentou detalhes".

## Saída literal do Teste B

```markdown
# POP — Separação e envio de pedidos por e-mail

| Campo | Conteúdo |
|---|---|
| Versão | 0.1 (rascunho) |
| Data | A CONFIRMAR |
| Dono do procedimento | Carla (dona) |
| Quem executa | Rafael (balcão) |
| Quem confere | Carla (dona) |
| Situação | Rascunho — ainda não testado por outra pessoa |

## 1. Objetivo
Separar, embalar e despachar os materiais solicitados pelos clientes via e-mail, garantindo o envio correto dos itens e a notificação do cliente com as informações de rastreamento ou entrega.

## 2. Quando usar (gatilho e frequência)
- **Gatilho:** Chegada de novos pedidos na caixa de entrada do e-mail da loja (`pedidos@papelaria-ficticia.example`).
- **Frequência:** Diária, em todos os dias úteis. A verificação é realizada duas vezes ao dia: no período da manhã e após o almoço (horários exatos: A CONFIRMAR).

## 3. Entradas, materiais e acessos
- Conta de e-mail `pedidos@papelaria-ficticia.example` — Cliente de e-mail / Webmail — Quem libera: Carla (A CONFIRMAR: se será criada conta própria ou compartilhado o acesso).
- Planilha "Pedidos 2026" — Google Planilhas — Quem libera: Carla.
- Confirmação de pagamento do pedido — Planilha "Pedidos 2026" (A CONFIRMAR: definição de Carla sobre criar coluna "pago" na planilha, já que Rafael não tem acesso ao banco).
- Caixas e envelopes para embalagem — Depósito dos fundos — Quem libera: Acesso físico ao depósito (Carla).
- Impressora de etiquetas — Área de operação (A CONFIRMAR local exato) — Quem libera: Carla.
- Aplicativo de motoboy — Smartphone/computador (A CONFIRMAR qual aplicativo) — Quem libera: Carla (A CONFIRMAR usuário/acesso para Rafael).

## 4. Passo a passo

| Nº | Ação | Como / onde | Conferência do passo |
|---|---|---|---|
| 1 | Acessar o e-mail de pedidos | Entrar no e-mail `pedidos@papelaria-ficticia.example` nos turnos da manhã e após o almoço | Caixa de entrada aberta e mensagens de novos pedidos identificadas |
| 2 | Verificar a confirmação de pagamento | Consultar se o pedido consta como pago (A CONFIRMAR: onde e como Carla indicará o pagamento) | Status de "pago" validado antes de qualquer separação |
| 3 | Imprimir a via do e-mail do pedido | Utilizar a impressora da loja para imprimir o conteúdo completo do e-mail do cliente | Via impressa do e-mail em mãos com lista visível de produtos e endereço |
| 4 | Registrar o pedido na planilha | Abrir a planilha "Pedidos 2026" no Google Planilhas e preencher: data, número do pedido, itens pedidos e tipo de envio (Correios ou motoboy) | Todas as colunas citadas preenchidas na linha correspondente |
| 5 | Identificar o modal de envio | Avaliar se o destino é atendido por motoboy ou se vai por Correios (A CONFIRMAR: critérios objetivos e lista de bairros) | Coluna de tipo de envio preenchida corretamente na planilha |
| 6 | Coletar os produtos no estoque | Ir até o depósito dos fundos e pegar fisicamente os produtos solicitados | Todos os itens físicos colocados na bancada de embalagem |
| 7 | Conferir os itens separados | Comparar produto por produto físico contra a via impressa do e-mail do pedido | Quantidades, modelos e itens físicos idênticos ao pedido impresso |
| 8 | Embalar os produtos | Selecionar caixa ou envelope adequado no depósito dos fundos e colocar os produtos dentro | Produtos devidamente protegidos dentro da embalagem |
| 9 | Inserir a via impressa na embalagem | Colocar a folha impressa do e-mail do pedido dentro da caixa/envelope antes de fechar | Folha do pedido presente dentro da embalagem |
| 10 | Fechar a embalagem | Vedar o pacote com fita adesiva apropriada | Embalagem totalmente lacrada e pronta para transporte |
| 11 | Imprimir a etiqueta de envio | Gerar e imprimir a etiqueta de envio na impressora de etiquetas | Etiqueta legível com os dados do destinatário |
| 12 | Colar a etiqueta no pacote | Fixar a etiqueta impressa na parte externa da embalagem lacrada | Etiqueta colada em local plano e com dados totalmente visíveis |
| 13 | Despachar via Correios (se aplicável) | Levar os pacotes até a agência dos Correios no período da tarde (A CONFIRMAR: agência de destino e horário limite de postagem) | Comprovante de postagem com código de rastreio em mãos |
| 14 | Despachar via motoboy (se aplicável) | Chamar o serviço pelo aplicativo de entregas (A CONFIRMAR: nome do app e conta de acesso) e entregar o pacote ao motoboy | Coleta realizada pelo entregador |
| 15 | Atualizar a planilha "Pedidos 2026" | Inserir o código de rastreio (caso Correios) e alterar o status do pedido para "enviado" | Linha do pedido atualizada com status "enviado" e código (se houver) |
| 16 | Notificar o cliente por e-mail | Responder ao e-mail original do pedido: incluir o código de rastreio (se Correios) ou informar que o pedido saiu para entrega (se motoboy) | E-mail enviado ao cliente registrado na caixa de saída |

## 5. Exceções e encaminhamento

| Situação | O que fazer | Encaminhar para |
|---|---|---|
| Falta de produto no estoque | Não prometer substituição, não devolver valores e não responder ao cliente; separar os itens que houver e avisar Carla imediatamente | Carla (decide se troca por item parecido ou se devolve o dinheiro daquele item) |
| Endereço de entrega incompleto | Não despachar o pedido; não responder por conta própria até definição do modelo de mensagem | Carla (precisa localizar o texto-padrão de cobrança de endereço e definir se Rafael pode enviar) |
| Pedido sem confirmação de pagamento | Não iniciar a separação nem o envio | Carla (responsável por consultar o extrato no banco) |
| Cliente solicita entrega no mesmo dia | Não prometer prazos de entrega sob hipótese alguma | Carla (avalia e decide a viabilidade) |
| Bairro de entrega com dúvida sobre motoboy | Não acionar o motoboy sem confirmação | Carla (avalia se atende a rota de motoboy) |

## 6. Critério de pronto
A rotina é considerada concluída para um pedido quando:
1. O pacote foi devidamente embalado contendo a via impressa do pedido em seu interior.
2. O pacote foi entregue na agência dos Correios ou coletado pelo motoboy.
3. A linha correspondente na planilha "Pedidos 2026" está com status "enviado" (e código de rastreio preenchido, caso Correios).
4. O cliente recebeu a resposta por e-mail contendo o código de rastreio (Correios) ou o aviso de saída para entrega (motoboy).

## 7. Riscos e cuidados
- **Envio sem pagamento:** É expressamente proibido separar ou enviar pacotes sem a confirmação formal do pagamento.
- **Envio de material incorreto:** É obrigatória a conferência minuciosa, item a item, utilizando a folha impressa antes de lacrar o pacote.
- **Ausência da via do pedido no pacote:** A via impressa do e-mail do pedido deve obrigatoriamente acompanhar o conteúdo interno da embalagem para evitar reclamações de conferência pelo cliente.
- **Promessa indevida de prazos e concessão de descontos:** O executor não possui autorização para negociar prazos ou oferecer abatimentos de valores aos clientes.
- **Perda de prazo dos Correios:** Risco de atraso no envio caso a ida à agência ocorra após o horário limite de postagem.

## 8. Lacunas A CONFIRMAR
1. **Acesso do executor ao e-mail:** Como será formalizado o acesso de Rafael ao `pedidos@papelaria-ficticia.example` (criação de conta individual ou compartilhamento de acesso)? — *Carla*
2. **Sinalização do pagamento:** Como Carla comunicará a Rafael que o pedido está pago (será criada uma coluna "pago" na planilha "Pedidos 2026")? — *Carla*
3. **Horários de rotina e envio:** Quais são os horários exatos para checagem da caixa de entrada (manhã e pós-almoço) e qual é o horário limite dos Correios para postagem no mesmo dia? — *Carla*
4. **Agência dos Correios:** Em qual agência específica dos Correios as encomendas devem ser postadas? — *Carla*
5. **Critério para motoboy:** Qual é a lista oficial de bairros cobertos pelo serviço de motoboy? — *Carla*
6. **Aplicativo de motoboy:** Qual aplicativo é utilizado para solicitar entregas e como Rafael terá permissão para abrir chamados? — *Carla*
7. **Procedimento para endereço incompleto:** Onde está salvo o texto padrão de solicitação de endereço e Rafael terá autorização para enviá-lo diretamente? — *Carla*
8. **Regra de decisão para troca/devolução:** Quais critérios determinam se um produto faltante será substituído por similar ou terá o valor estornado (hoje feito "às vezes")? — *Carla*
9. **Local da impressora:** Onde fica fisicamente a impressora de etiquetas dentro da loja? — *Carla*

## 9. Histórico de versões

| Versão | Data | O que mudou | Quem aprovou |
|---|---|---|---|
| 0.1 | A CONFIRMAR | Elaboração inicial do procedimento a partir do relato da proprietária | Carla |

---

# Checklist de execução — Separação e envio de pedidos por e-mail

Data: ____/____/________
Executado por: ____________________________________

- [ ] Acessar o e-mail `pedidos@papelaria-ficticia.example` no horário programado.
- [ ] Verificar se o pedido consta como pago (conforme coluna/aviso de Carla).
- [ ] Imprimir a via do e-mail do pedido.
- [ ] Registrar os dados na planilha "Pedidos 2026" (data, pedido, itens, Correios/motoboy).
- [ ] Validar se o método de envio é Correios ou motoboy (conforme regras de entrega).
- [ ] Separar todos os itens físicos listados no depósito dos fundos.
- [ ] Conferir os itens coletados comparando um a um com a folha impressa.
- [ ] Acondicionar os produtos dentro da embalagem (caixa ou envelope).
- [ ] Colocar a via impressa do pedido dentro da embalagem com os produtos.
- [ ] Lacrar a embalagem com fita adesiva.
- [ ] Imprimir a etiqueta de envio na impressora de etiquetas.
- [ ] Colar a etiqueta no lado de fora da embalagem lacrada.
- [ ] Despachar o pacote (levar aos Correios à tarde ou acionar motoboy por aplicativo).
- [ ] Preencher a coluna de código de rastreio na planilha "Pedidos 2026" (para Correios).
- [ ] Mudar o status da linha na planilha "Pedidos 2026" para "enviado".
- [ ] Responder ao e-mail do cliente informando o código de rastreio ou o envio via motoboy.

---

# Checklist de conferência — Separação e envio de pedidos por e-mail

Data: ____/____/________
Conferido por: ____________________________________

- [ ] Todas as linhas de pedidos movimentadas no dia na planilha "Pedidos 2026" possuem confirmação de pagamento prévia.
- [ ] O status de todos os pedidos despachados no dia está marcado como "enviado" na planilha.
- [ ] Os pedidos enviados via Correios contêm o código de rastreio registrado na planilha.
- [ ] Os e-mails de resposta a cada cliente constam na pasta de Enviados do e-mail de pedidos, acompanhados do respectivo rastreio ou aviso de entrega.
- [ ] Não há pedidos marcados como enviados cujos pacotes físicos ainda estejam retidos na loja.

Resultado: [ ] Aprovado  [ ] Devolvido — motivo: __________________________________________________

---

# Próximo passo: teste de mesa

Peça para Rafael executar a rotina do início ao fim usando apenas este POP impresso, sem receber orientações verbais.
Enquanto ele realiza as etapas, observe em silêncio e anote em uma folha todos os momentos em que ele hesitar, fizer perguntas ou travar.
Esses pontos observados revelarão as instruções que precisam ser esclarecidas ou corrigidas para a publicação da versão 1.0.

---

O que ainda impede a execução autônoma pelo Rafael é a falta de acesso ao e-mail da loja e ao aplicativo de motoboy, a ausência de uma sinalização formal de pagamento na planilha e a falta de listas objetivas para bairros atendidos por motoboy e horários de corte dos Correios.
```
