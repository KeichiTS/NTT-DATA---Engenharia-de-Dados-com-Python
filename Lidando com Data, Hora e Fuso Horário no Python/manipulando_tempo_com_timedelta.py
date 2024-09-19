# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:04:07 2024

@author: KeichiTS
"""

from datetime import datetime, timedelta, date, time

tipo_carro = 'G' #P, M ou G
tempo_pequeno = 10
tempo_medio = 20
tempo_grande = 30
data_atual = datetime.now()


if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(days = tempo_pequeno) 
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(days = tempo_medio) 
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
else:
    data_estimada = data_atual + timedelta(days = tempo_grande) 
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
    
print(date.today() - timedelta(days = 1))
resultado = datetime(2023, 7, 25, 10, 19, 20)- timedelta(hours = 1)
print(resultado.time())

print(datetime.now().date())