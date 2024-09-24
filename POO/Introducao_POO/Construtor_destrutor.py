# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 19:21:32 2024

@author: KeichiTS
"""

class Cachorro():
    def __init__(self, nome, cor, acordado = True):
        print('iniciando classe')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado 
    
    
    def __del__(self):
        print('removeu a instancia da classe')
    
    def falar(self):
        print('au au')
        

def criar_cachorro():
    c = Cachorro(nome = 'Winny', cor = 'Chocolate')
    print(c.nome)
    return c
    del c

c = criar_cachorro()
c.falar() 

#del c #No spyder é necessário pq o código não é encerrado no final do processo