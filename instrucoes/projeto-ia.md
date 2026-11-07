# Deixar a instrução salva na sua IA

Colar a `instrucao-pronta.md` toda vez funciona. Se você vai documentar várias rotinas, vale deixar a instrução salva. Escolha **um** caminho abaixo.

Conferido nas centrais de ajuda oficiais em 02/11/2026. As ferramentas mudam com frequência: se um menu estiver diferente, procure pelo nome do recurso na ajuda oficial (links no fim).

## Caminho 1 — Projeto no ChatGPT

1. No ChatGPT, na barra lateral, crie um **novo projeto** com o nome "Rotinas da empresa".
2. Abra as configurações do projeto e cole o texto entre `--- INÍCIO ---` e `--- FIM ---` de `instrucao-pronta.md` nas **instruções do projeto**. Troque a última linha ("Comece agora pelo Bloco 1.") por: "Quando eu abrir uma conversa neste projeto, comece pelo Bloco 1."
3. Opcional: envie como arquivo do projeto o `modelos/pop-modelo.md` para a IA seguir o mesmo formato.
4. Cada rotina nova = uma conversa nova dentro do projeto.

O que conferimos: Projetos estão disponíveis no plano gratuito, com até 5 arquivos por projeto e limite de 3 envios de arquivo por dia; Go e Plus têm até 25 arquivos por projeto; Edu, Pro, Business e Enterprise, até 40. As instruções do projeto valem só dentro dele. Nos planos Free, Plus e Pro, o conteúdo dos projetos pode ser usado para treinar modelos se a opção "Improve the model for everyone" estiver ligada (fica nas configurações de controle de dados). A página da ajuda bloqueou a leitura direta; conferimos pelo conteúdo indexado da Central de Ajuda da OpenAI.

**Não use GPT personalizado para isso.** Pela Central de Ajuda da OpenAI, contas pessoais (Free, Go, Plus e Pro) não criam mais GPTs novos, e os GPTs personalizados têm aposentadoria prevista para 11/12/2026, com migração para "plugins".

## Caminho 2 — Projeto no Claude

1. No Claude, abra **Projects** e crie um projeto "Rotinas da empresa".
2. Nas instruções do projeto, cole o mesmo texto (com a troca da última linha descrita acima).
3. Opcional: adicione `modelos/pop-modelo.md` ao conhecimento do projeto.
4. Cada rotina = uma conversa nova dentro do projeto.

O que conferimos: Projetos estão disponíveis para todos, inclusive no plano gratuito, que permite no máximo 5 projetos. A expansão automática de capacidade do conhecimento (RAG) é para planos pagos. Privacidade: em Configurações > Privacidade você decide se suas conversas podem ser usadas para melhorar o Claude (planos Free, Pro e Max); conversas anônimas não são usadas para treino.

## Caminho 3 — Skill (Claude ou Gemini)

A pasta `instrucoes/claude-skill/rotina-documentada/` é uma skill pronta. A mesma pasta serve nas duas ferramentas.

### No Claude

1. Ligue a execução de código: **Settings > Capabilities > "Code execution and file creation"** (no layout novo aparece como **"Create and edit files"**).
2. Compacte em ZIP a **pasta** `rotina-documentada` (o ZIP precisa ter a pasta na raiz, não o arquivo solto). No Windows: clique com o botão direito na pasta > Enviar para > Pasta compactada.
3. Vá em **Customize > Skills**, clique em **+**, depois **+ Create skill** > **Upload a skill** e envie o ZIP.
4. Em qualquer conversa, peça: "documentar uma rotina" ou "fazer um POP". O Claude usa a skill quando o assunto bate com a descrição.

Disponível nos planos Free, Pro, Max, Ultra, Team e Enterprise. O nome da pasta precisa ser igual ao nome da skill (`rotina-documentada`).

### No Gemini

1. Em **gemini.google.com**, clique em **Customize** na barra lateral (se não aparecer, clique em **More** antes) e depois em **Skills**.
2. Clique em **Create** > **Upload** e selecione o `SKILL.md`, a pasta `rotina-documentada` ou um .zip com o `SKILL.md` na pasta principal.
3. Revise e clique em **Create**. Para usar, digite `/` e o nome da skill no chat, ou apenas peça para documentar uma rotina.

Requisitos conferidos: ter 18 anos ou mais, estar logado e com a Atividade (Keep Activity) ligada. Segundo a ajuda do Google, skills funcionam sem assinatura do Google AI. Limite de 100 MB para os arquivos enviados.

**Não use Gem para isso.** Em contas pessoais, os Gems ficam somente leitura em 17/11/2026 e são removidos em 17/12/2026, substituídos por skills.

## Cuidados com dados

- Use exemplos sem dado de cliente: troque nome, CPF, telefone e endereço por descrições ("nome do cliente").
- Não cole senhas. A instrução pede só **qual** acesso é necessário.
- Se a rotina envolve dados pessoais (clientes, funcionários), lembre que colocar esses dados em ferramentas de IA é tratamento de dados sob a LGPD. Confira a política da empresa e, se preciso, um profissional da área. Isto não é parecer jurídico.

## Links oficiais

- Projetos no ChatGPT: https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- Aposentadoria dos GPTs personalizados: https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq
- Projetos no Claude: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- Skills no Claude: https://support.claude.com/en/articles/12512180-use-skills-in-claude e https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- Privacidade no Claude: https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings
- Skills no Gemini: https://support.google.com/gemini/answer/17094296
- Transição de Gems para skills: https://support.google.com/gemini/answer/18560919
- LGPD (Lei 13.709/2018): https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
