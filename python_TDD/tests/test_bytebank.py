from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):

        entrada = '13/03/2000' #Given-contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() #When-ação

        assert resultado == esperado #Then-desfecho

    def test_quando_nome_recebebe_lucas_carvalho_retorna_carvalho(self):

        entrada = ' Lucas Carvalho' #Given-contexto
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '28/02/1985', 1111)
        resultado = lucas.sobrenome() #When-ação

        assert resultado == esperado #Then-desfecho

    def test_quando_o_decrescimo_salario_for_100000_deve_retornar_90000(self):
        entrada_salario = 100000 #given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2011', entrada_salario)
        funcionario_teste.decrescimo_salario() #when
        resultado = funcionario_teste._salario

        assert resultado == esperado #then


    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000 #given
        esperado = 100

        bonus_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = bonus_teste.calcular_bonus() #when

        assert resultado == esperado #then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_10001_deve_retornar_exeption(self):
        with pytest.raises(Exception):
            entrada = 10001 #given

            bonus_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = bonus_teste.calcular_bonus() #when

            assert resultado  #then

    

    

