# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:44:10 2024

@author: KeichiTS
"""

from datetime import date, datetime, time

data = date(2023, 7, 10)
print(data)

print(date.today())

data_hora = datetime(2023, 7, 10, 10, 30, 20)
print(data_hora)
print(datetime.today())

hora = time(10,20,0)
print(hora)