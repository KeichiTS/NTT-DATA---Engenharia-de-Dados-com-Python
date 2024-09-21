# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 00:28:58 2024

@author: KeichiTS
"""

def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_vendas = 0 
    for i in range(len(vendas)):
        total_vendas += vendas[i]
    media_vendas = total_vendas / len(vendas)
        
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    print('Coloque o numero de vendas realizadas por mês no ano')
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    lista_entrada = entrada.split(',')
    map_int = map(int, lista_entrada)
    lista_int = list(map_int)
    
    vendas = lista_int
    
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))