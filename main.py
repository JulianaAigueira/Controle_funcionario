from kivy.app import App
from kivy.lang import Builder
from telas import *
from botoes import *
import requests
from myfirebase import MyFirebase

GUI = Builder.load_file('main.kv')

class MainApp(App):
    #id_usuario = 'admin/1'
    def build(self):
        self.firebase = MyFirebase()
        return GUI

    def on_start(self):
        try:
            with open('refreshtoken.txt', 'r') as arquivo:
                refresh_token = arquivo.read()
            local_id, id_token = self.firebase.trocar_token(refresh_token)
            self.local_id = local_id
            self.id_token = id_token

            # pegar informação do adimin
            requisicao = requests.get(f'https://appcadastrofuncionario-default-rtdb.firebaseio.com/{self.local_id}.json')
            requisicao_dic = requisicao.json()

            #preencher foto de ferfil
            foto = requisicao_dic['foto']
            foto_admin = self.root.ids['foto_admin']
            foto_admin.source = f'icones/{foto}'
            print(requisicao_dic)

            self.mudar_tela('menupage')
        except:
            pass

    def mudar_tela(self, id_tela):
        gerenciador_telas = self.root.ids['screen_manager']
        gerenciador_telas.current = id_tela

MainApp().run()

