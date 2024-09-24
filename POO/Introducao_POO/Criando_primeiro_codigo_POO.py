# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:37:34 2024

@author: KeichiTS
"""

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro = 18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
        
    def buzinar(self):
        print('plim plim')
    def parar(self):
        print('parando a bicicleta')
        print('bicicleta parada')
    def correr(self):
        print('vruuuuum')
        
    # def __str__(self):
    #     return f'Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}'

    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
b1 = Bicicleta('vermelha', 'caloi', '2022', 600)

b1.buzinar()
b1.parar()
b1.correr()

print(b1.cor, b1.modelo, b1.ano, b1.ano)

b2 = Bicicleta(cor = 'amarela', modelo = 'monark', ano = 2019, valor = 300)
Bicicleta.buzinar(b2) # == b2.buzinar()
print(b2)