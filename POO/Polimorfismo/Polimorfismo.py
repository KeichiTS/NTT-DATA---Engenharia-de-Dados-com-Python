# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 09:54:55 2024

@author: KeichiTS
"""

class Passaro:
    def voar(self):
        print('Voando')
        

class  Pardal(Passaro):
    def voar (self):
        super().voar()
        
class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não voa')
        
        
#EXEMPLO RUIM DE HERANÇA PARA GANHAR O MÉTODO "voar"
class Aviao(Passaro):
    def voar(self):
        print('Avião está decolando')
        
def plano_voo(obj):
    obj.voar()
    
#p1 = Pardal()
#p2 = Avestruz()

#plano_voo(p1)
#plano_voo(p2)

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())