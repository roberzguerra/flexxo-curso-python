# -*- coding: utf-8 -*-


class Veiculo():
    """
    Declarando a classe veiculo
    """

    # Atributos da classe
    rodas = 4
    portas = 4
    porta_malas = 1
    nome_cor = ''
    nome_marca = ''
    nome_modelo = ''
    ano_fabricacao = None

    def __init__(self, rodas, portas):
        self.rodas = rodas
        self.portas = portas
    

class Carro(Veiculo):
    nome_marca = "Volkswagem"
    nome_modelo = "Gol"

    def __init__(self, rodas=0, portas=0):
        """
        Construtor da classe Carro.
        rodas e portas são parametros opcionais (pois possuem definição de valor(=0))
        """
        if portas:
            self.portas = portas
        if rodas:
            self.rodas = rodas

