# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:34:03 2024

@author: KeichiTS
"""

class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def latir(self):
        print('auau')
        
    def dormir(self):
        self.acordado = False
        print('Zzzzz...')
        
cao_1 = Cachorro('Chapie', 'amarelo', False)
cao_2 = Cachorro('Aladim', 'branco e preto')

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)