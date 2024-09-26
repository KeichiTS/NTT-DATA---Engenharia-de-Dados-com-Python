# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:04:49 2024

@author: KeichiTS
"""

from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
    def realizar_transacao(self, conta, transacao):
        self.conta = conta
        self.registrar(conta)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
class PessoaFisica(Cliente):
     
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        super().__init__(endereco)
        
class Conta:
    
    def __init__(self, saldo, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '001'
        self._cliente = cliente
        self._historico = Historico() 
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo o suficiente')
            
        elif valor > 0:
            self._saldo -= valor
            print('Saque realizado com sucesso')
            return True
            
        else: 
            print('Operação falhou! O valor informado não é válido')
            
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('Deposito realizado com sucesso!')
        else:
            print('Valor invalido!')
            return False
        
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_de_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_de_saques = 3 
        
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacao if transacao['tipo'] == 'Saque']
            )
        #numero_saques = len(
        #   [transacao for transacao in self.historico.transacao if transacao['tipo'] == 'Saque']
        #    )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques
        
        if excedeu_limite:
            print('Operação falhou! O valor do saque excedeu limite!')
    
        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques atingido!')
            
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
                Agência:    {self.agencia}
                C/C:        {self.numero}
                Titular:    {self.cliente.nome}
            
            """

    def Historico():
        def __init__(self):
            self._transacoes = []
            
        @property
        def transacoes(self):
            return self._transacoes
        
        def adicionar_transacao(self, transacao):
            self._transacoes.append(
                {
                    'tipo': transacao.__class__.__name__,
                    'valor': transacao.valor,
                    'data': datetime.now().strftime('%d-m%-%Y %H:%M:%s'),
                }
            )
            
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractclassmethod
    def registrar(self, conta):
        pass
    
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transcao(self)
            
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor 
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)