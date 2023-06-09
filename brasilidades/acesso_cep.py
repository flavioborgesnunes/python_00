import requests

class BuscaEndereco:

    def __init__(self,cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError('CEP inválido.')
        
    def __str__(self):
        return self.gera_dados()


    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def format_cep(self):
        return '{}-{}'.format(self.cep[:5], self.cep[5:])
    
    def gera_dados(self):
        r = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/').json()

        if r == {'erro': True}:
            raise ValueError ('Cep Inválido')
        else:
            return f"{r['logradouro']}\n{r['bairro']}\n{r['localidade']} {r['uf']}"

    
    
