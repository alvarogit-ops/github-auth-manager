import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth


user = input("Enter your username: ")
password = getpass("Enter your password: ")

#pedir o usuário alvo
user_target = input("Enter the username of the target user: ")


# teste dos 30 primeiros usuários e suas posições

print("Usuário alvo: ", user_target)


#buscar
response = requests.get(f"https://api.github.com/users/{user_target}/followers?per_page=30", auth=HTTPBasicAuth(user, password))



seguidores = response.json()

if response.status_code == 200:
        print("OK")
        for seguidor in seguidores:
            print(seguidor['login']) 
            response_seguindo = requests.put(f"https://api.github.com/user/following/{seguidor['login']}?per_page=30", auth=HTTPBasicAuth(user, password))
            
            if response_seguindo.status_code == 204:
                print(f"OK {response_seguindo}")
            else:
                print(f"Deu ruim :/ {response_seguindo}")

else:
    print(f"deu ruim :/{response}")

#seguir todos usuários de target