# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 17:43:23 2024

@author: KeichiTS
"""

class Conta:
    def __init__(self, nro_agencia, saldo = 0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia
        
    def depositar(self, valor):
        # ...
        self._saldo += valor
    
    def sacar(self, valor):
        # ...
        self._saldo -= valor
        
    def mostrar_saldo(self):
        # ...
        return self._saldo
    
conta = Conta(nro_agencia = '001', saldo = 0)
conta.depositar(200)
print(conta._saldo)
print(conta.nro_agencia)
print(conta.mostrar_saldo())