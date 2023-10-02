# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 07:44:36 2023

@author: Calixte
"""

import pandas as pd
from reserved_keywords import get_reserved_keywords

query = 'SELECT * FROM staging.all_orders  t1 LEFT JOIN (SELECT * FROM staging.platform) t2 on t1.platform_id = t2.platform_id'

all_tokens = query.split()

df_all_tokens = pd.DataFrame(all_tokens, columns=['tokens'])

df_all_tokens['next_token'] = df_all_tokens['tokens'].shift(-1)

df_all_tokens['previous_token'] = df_all_tokens['tokens'].shift(1)

all_tables_index = list(df_all_tokens[df_all_tokens.previous_token.isin(get_reserved_keywords(sql_dialect='gcp'))].index)

print(df_all_tokens.iloc[all_tables_index])