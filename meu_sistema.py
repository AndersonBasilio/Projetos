# Botao de iniciar site
# Popup para entrar no chat
# Quando entrar no site (aparece para todo mundo)
    # a mensagem que entrou no chat
    # botao para enviar mensagem
# a cada mensagem que voce envia (aparece para todo mundo)
    # Nome: Texto da mensagem

import flet as ft

# Precisamos de tres passos para fazer site flet
# importar o flet
# Precisamos criar uma função que ira receber uma página com parâmetro
def main(pagina):
    texto = ft.Text('Chat Rhapsody!')

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu nome")

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            #adicionar a mensagem no chat
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}", color="red"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat.", size=16, italic=True, color=ft.colors.GREEN_500))    
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_de_mensagem.value, 'usuario': nome_usuario.value, "tipo": "mensagem"})
        #limpar o texto de mensagem 
        campo_de_mensagem.value = ""
        pagina.update()

    campo_de_mensagem = ft.TextField(label="Escreva uma mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar Mensagem", on_click=enviar_mensagem)


    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        #adiciona o chat
        pagina.add(chat)
        # fechar popup
        popup.open = False
        # remover botao de iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        # criar campo de mensagem do usuário
        pagina.add(ft.Row(
            [campo_de_mensagem, botao_enviar_mensagem]
        ))
        # aparecer botao de enviar mensagem.  
        pagina.update()  


    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao Rhapsody Chat."),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
    )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()


    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)
    
ft.app(target=main, view=ft.WEB_BROWSER, port=8000)


