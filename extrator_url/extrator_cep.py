endereco = 'Rua das Flores 72, 13560-662, São Paulo, Brasil'
import re

padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)