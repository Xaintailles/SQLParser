# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 07:44:36 2023

@author: Calixte
"""

import pandas as pd
import re

from reserved_keywords import get_reserved_keywords

query = 'SELECT * FROM just-data-warehouse.staging.all_orders  t1 LEFT JOIN (SELECT * FROM {queryid}.staging.platform) t2 on t1.platform_id = t2.platform_id'

all_tokens = query.split()

df_all_tokens = pd.DataFrame(all_tokens, columns=['tokens'])

df_all_tokens['next_token'] = df_all_tokens['tokens'].shift(-1)

df_all_tokens['previous_token'] = df_all_tokens['tokens'].shift(1)

all_tables_index = list(df_all_tokens[df_all_tokens.previous_token.isin(get_reserved_keywords(sql_dialect='gcp'))].index)

list_after_reserved_keywords = list(df_all_tokens.iloc[all_tables_index]['tokens'])

pattern = r'^[^.]+(\.[^.]+){2}$'

matching_patterns = []

for text_to_check in list_after_reserved_keywords:

    if re.match(pattern, text_to_check):
        matching_patterns.append(text_to_check)

# Characters to remove
chars_to_remove = ",!()){}"

# Remove specified characters from each string in the list
cleaned_matching_patterns = list(set([''.join(char for char in string if char not in chars_to_remove) for string in matching_patterns]))

# Display the cleaned list
print(cleaned_matching_patterns)