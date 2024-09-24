# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:45:29 2024

@author: KeichiTS
"""

class Veiculo():
    
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self):
        print('ligando o motor')
        
    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, carregado, cor, placa, numero_rodas):
        self.carregado = carregado
        super().__init__(cor, placa, numero_rodas)
    def esta_carregado(self):
        print(f'{"Sim" if self.carregado else "Não"} estou carregado')

moto = Motocicleta(cor = 'preta', placa = 'ABC1234', numero_rodas = 2)
print(moto)
moto.ligar_motor()

carro = Carro(cor = 'branco', placa = 'XYZ9876', numero_rodas = 4)
carro.ligar_motor()

caminhao = Caminhao(cor = 'roxo', placa = 'AAA1111', numero_rodas = 8, carregado = True)
caminhao.ligar_motor()
caminhao.esta_carregado()


print(moto)
print(carro)
print(caminhao)