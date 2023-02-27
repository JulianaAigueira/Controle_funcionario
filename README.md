 Controle_funcionario
 Aplicativo onde a empresa controla o fluxo de funcionários.
 
 Utilizei o banco de dado Firebase para armazenar os usuários criados na tela de login e armazenar os funcionários cadastrados.
 
 O Firebase disponibiliza um link para fazer as trocas de informações através de APIs.
 
 Link do site Firebase: https://console.firebase.google.com/u/0/?hl=pt-br, para você criar seu projeto.
 
 Fiz uma tela inicial de login. Usei o Google Cloud (site: https://cloud.google.com/identity-platform/docs/use-rest-api?hl=pt-br) para criar usuário e logar o mesmo. Ele possui APIs específicos para cada situação e já valida se o usuário existe, se e-mail está correto, se a senha é válido e se os campos de e-mail e senha estão preenchidos corretamente.

Tela inicial:

Serve para criar e logar usuários.

![tella_login](https://user-images.githubusercontent.com/121833579/221573915-26efdc70-d163-4998-b4ed-640f404ac352.jpg) ![tela_criando_login](https://user-images.githubusercontent.com/121833579/221574652-e5350e83-ae4f-403b-b12c-ea75e1d718e3.jpg)

Tela menu:

Menu com todas as funcionalidades do aplicativo. Adicionar usuário, buscar funcionário, editar funcionário e excluir funcionário).
Tanto as imagens como os Label são botões para levar a página que desejada e posso voltar para a tela de login ou sair do aplicativo.


![tela_menu_logado](https://user-images.githubusercontent.com/121833579/221575278-28736e85-a3bd-4e10-b0d1-2657e2b8867f.jpg)

Tela adicionar funcionário:

O usuário vai preencher todas as informações solicitadas e salvar no banco de dados.
Existe um botão para voltar para tela menu principal.

![tela_add_funcionario](https://user-images.githubusercontent.com/121833579/221576949-af2024da-3fc7-4367-b410-a534a6c4d44f.jpg)

Tela buscar funcionário:

Para buscar o funcionário utilizei o cpf que é único para cada pessoa.
Ao ser localizado todas as informações do funcionário é exibido na tela.
Existe um botão para voltar para tela menu principal.

![tela_buscar_funcionario](https://user-images.githubusercontent.com/121833579/221578890-d1f7d7be-714e-4fdb-88e7-ef26eb981ad2.jpg)

Tela editar funcionário:

Para editar o funcionário que deseja, é feito uma busca utilizando o cpf e ao localizar é exibido o funcionário onde você pode alterar os dados desejado e atualizar no banco de dado. Existe um botão para voltar para tela menu principal.

![tela editar funcionario](https://user-images.githubusercontent.com/121833579/221580442-d0e0e6ce-d208-4bed-97fe-d7aa01ac556b.jpg)

Tela excluir funcionário:

Através de uma busca você pode excluir o funcionário que deseja e automaticamente ele será eliminado do seu banco de dado.
Existe um botão para voltar para tela menu principal.

![tela_excluir_funcionario](https://user-images.githubusercontent.com/121833579/221581081-62165c62-8af6-4b89-9b71-21de3ac51592.jpg)







