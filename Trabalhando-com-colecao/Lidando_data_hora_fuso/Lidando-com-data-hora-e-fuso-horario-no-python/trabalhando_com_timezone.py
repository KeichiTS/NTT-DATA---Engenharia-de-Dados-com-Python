# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:34:00 2024

@author: KeichiTS
"""

import pytz
from datetime import datetime, timezone, timedelta

data = datetime.now(pytz.timezone('Europe/Oslo'))
data2 = datetime.now(pytz.timezone('America/Sao_Paulo'))

print(data)
print(data2)

data_oslo = datetime.now(timezone(timedelta(hours = 2), 'OSL'))
data_sao_paulo = datetime.now(timezone(timedelta(hours = -2), 'SP'))

print(data_oslo)
print(data_sao_paulo)