'''The purpose of this project is to create a live chat with Flet, a Python web framework. One Flask
version will be made too.'''

import flet as ft       #First, we import flet and call it as ft

def main(page):         #The page is defined in main function
    text = ft.Text('HashZap')       #Here, we configure the text variable
    chat = ft.Column()      #All the messages sent to chat will appear in a column
    username = ft.TextField(label='Seu nome aqui...')  #With this textField we store the username   

    def sendMessage(event):         #the sendMessage function will catch values for messageField and username
                                    #to send messages to all the users logged
        page.pubsub.send_all({'text': messageField.value, 'user': username.value, 'type': 'message'})
        messageField.value = ''     #clear the messageField
        page.update()

    '''Here, we create a message field and a button to send the message. The actions for both elements
    will be treated by the sendMessage function'''
    messageField = ft.TextField(label='Digite sua mensagem', on_submit=sendMessage) 
    sendMessageButton = ft.ElevatedButton('Enviar', on_click=sendMessage)

    def popupClose(event):         #the popupClose function will close the popup generated in login
                                   #and capture the value for username to render it on the chat. Furthermore,
                                   #the function will add a field for message and a button to send the messages
        page.pubsub.send_all({'user': username.value, 'type': 'enter'})
        page.add(chat)
        popup.open = False
        page.remove(loginButton)    #the button for login and the text will be removed
        page.remove(text)
        page.add(ft.Row(
            [messageField, sendMessageButton ]
        ))
        page.update()

    popup = ft.AlertDialog(     #The object popup creates a pop which will be render for the user with a welcome
                                #message and a login button
        open= False, modal= True, title= ft.Text('Bem vindo ao HashZap'), content= username, 
        actions=[ft.ElevatedButton('Entrar', on_click=popupClose)]
    )

    def chat_login(event):      #The chat_login function call for the popup created above and open it
        page.dialog = popup
        popup.open = True
        page.update()

    loginButton = ft.ElevatedButton('Iniciar chat', on_click=chat_login)    #login button configurations
    page.add(text)      #All the elements need to be added to the page (text and loginButton, for example)
    page.add(loginButton) 

ft.app(target=main, view=ft.WEB_BROWSER, port=5000) #App configurations