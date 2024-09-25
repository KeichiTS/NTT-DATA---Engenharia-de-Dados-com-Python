# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:41:23 2024

@author: KeichiTS
"""
from abc import ABC,abstractclassmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractclassmethod
    def ligar(self):
        pass
    @abstractclassmethod
    def desligar(self):
        pass
    
    
    @property
    @abstractproperty
    def marca(self):
        pass
    
class ControleTV(ControleRemoto):
    def ligar(self):
        print('ligando a tv')
        print('tv ligada')
        
    def desligar(self):
        print('desligando a tv')
        print('tv desligada')
        
    @property
    def marca(self):
        return 'LG'
        
        
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('ligando o ar condicionado')
        print('ar ligado')
        
    def desligar(self):
        print('desligando o ar condicionado')
        print('ar desligado')
        
    @property
    def marca(self):
        return 'Pioneer'
    

controle = ControleTV()
controle.ligar()
controle.desligar()

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()
print(controle.marca)
print(controle_ar.marca)