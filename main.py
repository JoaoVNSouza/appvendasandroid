from kivy.app import App
from kivy.lang import Builder
import requests
from telas import *
from botoes import *
from bannervenda import *

GUI = Builder.load_file("main.kv")  # Load the GUI from main.kv


class MainApp(App):  # Página principal.
    id_usuario = 1

    def build(self):  # Função para construir a GUI.
        self.icon = 'icones/hash.png'
        return GUI

    def on_start(self):  # São executadas no início do programa.
        # Pegar informações do usuário no BD.
        url = f'https://aplicativovendashash-fdfdd-default-rtdb.firebaseio.com/{self.id_usuario}.json'
        requisicao = requests.get(url)

        if requisicao.status_code == 200:
            dados_usuario = requisicao.json()

            # Preencher foto de perfil.
            avatar = dados_usuario['avatar']
            foto_perfil = self.root.ids['foto_perfil']
            foto_perfil.source = f'icones/fotos_perfil/{avatar}'

            # Preencher lista de vendas.
            try:
                vendas = dados_usuario['vendas'][1:]
                for venda in vendas:
                    banner = BannerVenda(quantidade=venda['quantidade'], preco=venda['preco'], data=venda['data'],
                                         produto=venda['produto'], cliente=venda['cliente'], unidade=venda['unidade'],
                                         foto_cliente=venda['foto_cliente'], foto_produto=venda['foto_produto'])
                    pagina_homepage = self.root.ids['homepage']
                    lista_vendas = pagina_homepage.ids['lista_vendas']
                    lista_vendas.add_widget(banner)

            except KeyError:
                print('Teste')

    def mudar_tela(self, id_tela):
        self.root.ids['screen_manager'].current = id_tela


MainApp().run()  # Executar o aplicativo
