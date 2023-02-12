# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re

to_search_for = ['FROM','LEFT JOIN']

test_string = 'SELECT * FROM dwh.fact_order LEFT JOIN dwh.dim_order FROM'

def looking_for_table(searchable__string,semantic_elements):
    all_indexes = []
    for semantic_element in semantic_elements:
        all_indexes.append([m.start() for m in re.finditer(semantic_element, searchable__string)])
    
    #gives a list of lists, need to flatten
    all_indexes = [item for sublist in all_indexes for item in sublist]
    all_indexes.sort()
    return all_indexes

print(looking_for_table(test_string,to_search_for))
