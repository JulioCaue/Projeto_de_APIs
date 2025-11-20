import requests

# 1. Definir para onde vamos ligar (URL)
url = "https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&current_weather=true"

# 2. Fazer a chamada (GET)
resposta = requests.get(url)

# 3. Ver se funcionou (200 = OK)
if resposta.status_code == 200:
    print("Conexão bem sucedida!")
    print("Dados recebidos:")
    dados=resposta.json()
    temperatura=dados['current_weather']['temperature']
    print (f'A temperatura atual em SP é {temperatura}°C')
    
else:
    print("Deu erro na conexão:", resposta.status_code)