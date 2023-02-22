# site do link API para verificação de e-mail: https://cloud.google.com/identity-platform/docs/use-rest-api?hl=pt-br
import requests
from kivy.app import App

class MyFirebase():
    API_KEY = 'AIzaSyAvA2n3rLCUJb_R9tgcVAk43PBIHR7y0HA'

    def criar_conta(self, email, senha):
        link = f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={self.API_KEY}'

        info = {'email': email,
                'password': senha,
                'returnSecureToken': True}
        requisicao = requests.post(link, data=info)
        requisicao_dic = requisicao.json()

        if requisicao.ok:
            print('Usuário Criado')
            #requisicao_dic['idToken'] -> autenticação
            #requisicao_dic['refreshToken'] -> token que mantém o usuário logado
            #requisicao_dic['localId'] -> id_usuario
            refresh_token = requisicao_dic['refreshToken']
            local_id = requisicao_dic['localId']
            id_token = requisicao_dic['idToken']

            meu_aplicativo = App.get_running_app()
            meu_aplicativo.local_id = local_id
            meu_aplicativo.id_token = id_token

            with open('refreshtoken.txt', 'w') as arquivo:
                arquivo.write(refresh_token)
        else:
            mensagem_erro = requisicao_dic['error']['message']
            meu_aplicativo = App.get_running_app()
            pagina_login = meu_aplicativo.root.ids['homepage']
            pagina_login.ids['mensagem_login'].text = mensagem_erro
            pagina_login.ids['mensagem_login'].color = (1, 0, 0, 1)
        print(requisicao_dic)

    def fazer_login(self, email, senha):

        pass
