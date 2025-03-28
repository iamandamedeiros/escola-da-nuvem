import requests

def gerar_perfil():
    response = requests.get('https://randomuser.me/api/')
    
    if response.status_code == 200:
        data = response.json()
        usuario = data['results'][0]
        
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}")
    else:
        print("Erro ao acessar a API 'Random User Generator'.")

if __name__ == '__main__':
  gerar_perfil()