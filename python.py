# -*- coding: utf-8 -*-
# Template padrão para scripts python

# Diferenças operadores de comparação
# PT  :  PHP    :   PYTHON
# OU      ||           or
#  E      &&    :      and
# Contem   -    :      in


from classes.classes import Veiculo, Carro

__author__="Rober Guerra"
__date__ ="$15/10/2018 21:00:00$"


def dolar(valor):
    
    resultado = 0
    if (type(valor) == float or type(valor) == int):
        resultado = valor * 3.74
    else:
        print('Tipo do valor inválido. Passe um valor inteiro ou decimal.')
    return resultado
        


if __name__ == "__main__":
    #resultado = dolar('100')
    #print("Resultado = %f" % resultado)
    print('instanciando classe Veiculo:')
    
    # Estamos declarando a classe Carro e passando para o seu construtor
    # 2 parametros nomeados: 
    #   rodas = 4
    #   portas = 2
    v1 = Carro(rodas=4, portas=2)

    v1.ano_fabricacao = 2010
    
    # Duas formas de printar a mensagem:
    print("Marca: %s, Modelo: %s" % (v1.nome_marca, v1.nome_modelo))
    print("  Veiculo possui " + str(v1.rodas) + " rodas.");
    print("  Veiculo possui %d rodas e %d portas." % (v1.rodas, v1.portas) )
    print("  Veiculo ano %d." % (v1.ano_fabricacao))





    
