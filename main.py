import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth

user = input('User: ')
password = getpass()


opcao = 0



while True:
    opcao = int(input("Digite uma opção: \n 1 para listar seguidores \n 2 para seguir um usuário \n 3 para deixar de seguir um usuário \n 4 - Sair"))


    if opcao == 1:
        response = requests.get("https://api.github.com/user/followers", auth=HTTPBasicAuth(user, password))
     

        seguidores = response.json()
        if response.status_code == 200:
            print("Ok, tudo certo")
            seguidores = response.json()
        for seguidor in seguidores:
            print(seguidor['login'])
      
        else:
            print("Deu ruim :/")

    
    elif opcao == 2:
        target = input("User for follow: ")
        response = requests.put(f"https://api.github.com/user/following/{target}", auth=HTTPBasicAuth(user, password))
        print(response)
        print(response.status_code)
        
     

      
        if response.status_code == 204:
            print(f"Boa, agora {target} foi seguido")
        elif response.status_code == 304:
            print("Não modificado")
        elif response.status_code == 401:
            print("Precisa de autenticação")
        elif response.status_code == 403:
            print("Não autorizado")
        elif response.status_code == 404:
            print("Não encontrado")

        print(response.text)

    elif opcao == 3:
        target = input("User for unfollow: ")
        response = requests.delete(f"https://api.github.com/user/following/{target}", auth=HTTPBasicAuth(user, password))

        if response.status_code == 204:
            print(f"Humm, agora {target} não é mais seguido")
        else:
            print("Deu errado")

    elif opcao == 4:
        print("Saindo...")
        break





