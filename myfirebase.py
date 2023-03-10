# site do link API para verificação de e-mail: https://cloud.google.com/identity-platform/docs/use-rest-api?hl=pt-br
import json

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
        print(requisicao_dic)

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

            #link do banco de dados
            link = f'https://appcadastrofuncionario-default-rtdb.firebaseio.com/{local_id}.json'
            info_admin = '{"admin": "", "email": "", "foto": "admin.png", "password": ""}'
            requisicao_admin = requests.patch(link, data=info_admin)

            meu_aplicativo.on_start()
            meu_aplicativo.mudar_tela('menupage')

        else:
            mensagem_erro = requisicao_dic['error']['message']
            meu_aplicativo = App.get_running_app()
            pagina_login = meu_aplicativo.root.ids['homepage']
            pagina_login.ids['mensagem_login'].text = mensagem_erro
            pagina_login.ids['mensagem_login'].color = (1, 0, 0, 1)
        print(requisicao_dic)

    def fazer_login(self, email, senha):
        link = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={self.API_KEY}'
        info = {'email': email,
                'password': senha,
                'returnSecureToken': True}
        requisicao = requests.post(link, data=info)
        requisicao_dic = requisicao.json()

        if requisicao.ok:
            refresh_token = requisicao_dic['refreshToken']
            local_id = requisicao_dic['localId']
            id_token = requisicao_dic['idToken']

            meu_aplicativo = App.get_running_app()
            meu_aplicativo.local_id = local_id
            meu_aplicativo.id_token = id_token

            with open('refreshtoken.txt', 'w') as arquivo:
                arquivo.write(refresh_token)

            meu_aplicativo.on_start()
            meu_aplicativo.mudar_tela('menupage')

        else:
            mensagem_erro = requisicao_dic['error']['message']
            meu_aplicativo = App.get_running_app()
            pagina_login = meu_aplicativo.root.ids['homepage']
            pagina_login.ids['mensagem_login'].text = mensagem_erro
            pagina_login.ids['mensagem_login'].color = (1, 0, 0, 1)


    def trocar_token(self, refresh_token):
        link = f'https://securetoken.googleapis.com/v1/token?key={self.API_KEY}'

        info = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token
        }
        requisicao = requests.post(link, data=info)
        requisicao_dic = requisicao.json()
        print(requisicao_dic)
        local_id = requisicao_dic['user_id']
        id_token = requisicao_dic['id_token']
        return local_id, id_token

    def adicionar_funcinario(self, nome, cpf, endereco, uf, cidade, admissao, cargo, salario, demissao):
        link = 'https://appcadastrofuncionario-default-rtdb.firebaseio.com/'
        info = {'nome': nome,
                'CPF': cpf,
                'endereço': endereco,
                'uf': uf,
                'cidade': cidade,
                'admissão': admissao,
                'cargo': cargo,
                'salário': salario,
                'demissão': demissao
                }

        requisicao = requests.post(f'{link}/funcionário/.json', data=json.dumps(info))
        print(requisicao)
        print(requisicao.text)

    def buscarfuncionario(self, cpf):
        link = 'https://appcadastrofuncionario-default-rtdb.firebaseio.com/'
        requisicao = requests.get(f'{link}/funcionário/.json')
        requisicao_dic = requisicao.json()
        #print(requisicao_dic['CPF'])
        id_cpf = None
        for id_funcionario in requisicao_dic:
            funcionario = requisicao_dic[id_funcionario]['CPF']
            if funcionario == cpf:
                print(id_funcionario)
                id_cpf = id_funcionario

        requisicao = requests.get(f'{link}/funcionário/{id_cpf}/.json')
        print(requisicao)
        requisicao_dic = requisicao.json()
        print(requisicao_dic)

        meu_aplicativo = App.get_running_app()
        buscacpf = meu_aplicativo.root.ids["buscarfuncionariopage"]
        buscacpf.ids['buscar_nome_funcionario'].text = requisicao_dic['nome']
        buscacpf.ids['buscar_endereco_funcionario'].text = requisicao_dic['endereço']
        buscacpf.ids['buscar_cidade_funcionario'].text = requisicao_dic['cidade']
        buscacpf.ids['buscar_estado_funcionario'].text = requisicao_dic['uf']
        buscacpf.ids['buscar_admissao_funcionario'].text = requisicao_dic['admissão']
        buscacpf.ids['buscar_cargo_funcionario'].text = requisicao_dic['cargo']
        buscacpf.ids['buscar_salario_funcionario'].text = requisicao_dic['salário']
        buscacpf.ids['buscar_demissao_funcionario'].text = requisicao_dic['demissão']

    def deletarfuncionario(self, cpf):
        link = 'https://appcadastrofuncionario-default-rtdb.firebaseio.com/'
        requisicao = requests.get(f'{link}/funcionário/.json')
        requisicao_dic = requisicao.json()
        # print(requisicao_dic['CPF'])
        id_cpf = None
        for id_funcionario in requisicao_dic:
            funcionario = requisicao_dic[id_funcionario]['CPF']
            if funcionario == cpf:
                print(id_funcionario)
                id_cpf = id_funcionario

        requisicao = requests.get(f'{link}/funcionário/{id_cpf}/.json')
        print(requisicao)
        requisicao_dic = requisicao.json()
        print(requisicao_dic)

        meu_aplicativo = App.get_running_app()
        buscacpf = meu_aplicativo.root.ids["excluirfuncionariopage"]
        buscacpf.ids['excluir_nome_funcionario'].text = requisicao_dic['nome']


    def deletarfinal(self, cpf):
        link = 'https://appcadastrofuncionario-default-rtdb.firebaseio.com/'
        requisicao = requests.get(f'{link}/funcionário/.json')
        requisicao_dic = requisicao.json()
        # print(requisicao_dic['CPF'])
        id_cpf = None
        for id_funcionario in requisicao_dic:
            funcionario = requisicao_dic[id_funcionario]['CPF']
            if funcionario == cpf:
                print(id_funcionario)
                id_cpf = id_funcionario


        requisicao = requests.delete(f'{link}/funcionário/{id_cpf}/.json')

    def editarfuncionario(self, cpf):
        link = 'https://appcadastrofuncionario-default-rtdb.firebaseio.com/'
        requisicao = requests.get(f'{link}/funcionário/.json')
        requisicao_dic = requisicao.json()
       # print(requisicao_dic['CPF'])
        id_cpf = None
        for id_funcionario in requisicao_dic:
            funcionario = requisicao_dic[id_funcionario]['CPF']
            if funcionario == cpf:
                print(id_funcionario)
                id_cpf = id_funcionario

        requisicao = requests.get(f'{link}/funcionário/{id_cpf}/.json')
        print(requisicao)
        requisicao_dic = requisicao.json()
        print(requisicao_dic)

        meu_aplicativo = App.get_running_app()
        buscacpf = meu_aplicativo.root.ids["editarfuncionariopage"]
        buscacpf.ids['editar_nome_funcionario'].text = requisicao_dic['nome']
        buscacpf.ids['editar_endereco_funcionario'].text = requisicao_dic['endereço']
        buscacpf.ids['editar_cidade_funcionario'].text = requisicao_dic['cidade']
        buscacpf.ids['editar_estado_funcionario'].text = requisicao_dic['uf']
        buscacpf.ids['editar_admissao_funcionario'].text = requisicao_dic['admissão']
        buscacpf.ids['editar_cargo_funcionario'].text = requisicao_dic['cargo']
        buscacpf.ids['editar_salario_funcionario'].text = requisicao_dic['salário']
        buscacpf.ids['editar_demissao_funcionario'].text = requisicao_dic['demissão']

    def atualizar_funcinario(self, nome, cpf, endereco, cidade, uf, admissao, cargo, salario, demissao):
        link = 'https://appcadastrofuncionario-default-rtdb.firebaseio.com/'
        info = {'nome': nome,
                'CPF': cpf,
                'endereço': endereco,
                'uf': uf,
                'cidade': cidade,
                'admissão': admissao,
                'cargo': cargo,
                'salário': salario,
                'demissão': demissao
                }

        requisicao = requests.get(f'{link}/funcionário/.json')
        requisicao_dic = requisicao.json()
        # print(requisicao_dic['CPF'])
        id_cpf = None

        for id_funcionario in requisicao_dic:
            funcionario = requisicao_dic[id_funcionario]['CPF']
            if funcionario == cpf:
                print(id_funcionario)
                id_cpf = id_funcionario

        requisicao = requests.patch(f'{link}/funcionário/{id_cpf}/.json', data=json.dumps(info))
        print(requisicao)
        print(requisicao.text)
