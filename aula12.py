import requests

try:
    requisicao = requests.get('http://youtube.com.br')
    print(requisicao.status_code)
except Exception as e:
    print("Requisição deu um erro", e)
