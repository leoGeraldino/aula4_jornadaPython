'''The purpose of this project is to create a live chat with Flet, a Python web framework. One Flask
version will be made too.'''

import flet as ft       #First, we import flet and call it as ft

def main(page):         #The page is defined in main function
    text = ft.Text('HashZap')       #Here, we configure the text variable
    
    chat = ft.Column()

    username = ft.TextField(label='Seu nome aqui...')  #With this textField we store the username   

    popup = ft.AlertDialog(
        open= False, modal= True, title= ft.Text('Bem vindo ao HashZap'), content= username, 
        actions=[ft.ElevatedButton('Entrar', on_click=popupRender)]
    )

   # def popupRender(event):
   #     page.subpub.send_all({'user': username.value, 'type': 'enter'})

    def chat_login(event):
        page.dialog = popup
        popup.open = True
        page.update()

    loginButton = ft.ElevatedButton('Iniciar chat', on_click=chat_login)    #login button configurations
    page.add(text)      #All the elements need to be added to the page (text and loginButton too)
    page.add(loginButton) 

ft.app(target=main, view=ft.WEB_BROWSER, port=5000) #App configurations