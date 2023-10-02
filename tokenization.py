# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 07:44:36 2023

@author: Calixte
"""

query = 'SELECT * FROM staging.all_orders  t1 LEFT JOIN (SELECT * FROM staging.platform) t2 on t1.platform_id = t2.platform_id'

all_tokens = query.split()

table_tokens = [i for i, e in enumerate(all_tokens) if e == 'FROM']

print(table_tokens)   