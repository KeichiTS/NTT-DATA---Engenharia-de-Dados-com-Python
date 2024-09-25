# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:25:22 2024

@author: KeichiTS
"""

class Pessoa:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade 
        
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        #print(cls)
        idade = 2024 - ano
        return Pessoa(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18 
        

p = Pessoa.criar_de_data_nascimento(ano = 1994, mes = 3, dia = 21, nome = 'Guilherme')
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(17))
print(Pessoa.e_maior_idade(20))