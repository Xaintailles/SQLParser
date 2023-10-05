# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 07:44:36 2023

@author: Calixte
"""

import pandas as pd
import re
from reserved_keywords import get_reserved_keywords

root_path = r'/Users/calixte.allier/'

file_path = root_path + r'airflow-coredwh/dags/transformations/facts/fact_rfm.sql'

def tokenize_a_file(file_path: str, sql_dialect: str) -> list:

    with open(file_path,'r') as f:
        query = f.read()

    all_tokens = query.split()

    df_all_tokens = pd.DataFrame(all_tokens, columns=['tokens'])

    df_all_tokens['next_token'] = df_all_tokens['tokens'].shift(-1)

    df_all_tokens['previous_token'] = df_all_tokens['tokens'].shift(1)

    all_tables_index = list(df_all_tokens[df_all_tokens.previous_token.isin(get_reserved_keywords(sql_dialect=sql_dialect))].index)

    list_after_reserved_keywords = list(df_all_tokens.iloc[all_tables_index]['tokens'])

    pattern = r'^[^.]+(\.[^.]+){2}$'

    matching_patterns = []

    for text_to_check in list_after_reserved_keywords:

        if re.match(pattern, text_to_check):
            matching_patterns.append(text_to_check)

    # Characters to remove
    chars_to_remove = ",!()){}`"

    # Remove specified characters from each string in the list
    cleaned_matching_patterns = list(set([''.join(char for char in string if char not in chars_to_remove) for string in matching_patterns]))

    # Display the cleaned list
    return cleaned_matching_patterns