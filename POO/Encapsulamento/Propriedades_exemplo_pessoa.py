# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:09:40 2024

@author: KeichiTS
"""

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
    
    def get_nome(self):    ##Alternativa não pythonica 
        return self._nome

    def get_idade(self):    ##Alternativa não pythonica 
        return 2024 - self._ano_nascimento

pessoa = Pessoa(nome = 'Joao', ano_nascimento = 2020)
print(f"Nome : {pessoa.nome} \tIdade : {pessoa.idade}")
print(f"Nome : {pessoa.get_nome()} \tIdade : {pessoa.get_idade()}")    ##Alternativa não pythonica 