# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:07:17 2024

@author: KeichiTS
"""

class Estudante:
    escola = 'DIO'
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    
aluno_1 = Estudante('Guilherme', 1)
aluno_2 = Estudante('Diovana', 2)
mostrar_valores(aluno_1, aluno_2) 


Estudante.escola = 'Python'
aluno_1.matricula = 4
aluno_3 = Estudante('Chappie', 3)
mostrar_valores(aluno_1, aluno_2, aluno_3) 