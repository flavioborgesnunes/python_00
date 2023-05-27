import requests
from acesso_cep import BuscaEndereco

#r = requests.get('https://viacep.com.br/ws/13560820/json/').json()


cep = 60010040

objeto_cep = BuscaEndereco(cep)

print(objeto_cep) 

