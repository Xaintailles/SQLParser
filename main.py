# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re

#TO DO: bug when handling LEFT JOIN, we get index of JOIN
source_to_search_for = ['FROM','JOIN']
destination_to_search_for = ['INSERT INTO']

query = 'INSERT INTO dwh.fact_order (SELECT * FROM dwh.fact_order fo LEFT JOIN dwh.dim_order do on do.orderid = fo.orderid LEFT JOIN staging.all_orders so on so.source_order_id = do.sourceorderid)'

def looking_for_table(searchable__string,semantic_elements):
    start_index = []
    
    #here we grab every index for the first letter of the semantic elements
    for semantic_element in semantic_elements:
        start_index.append([m.end() + 1 for m in re.finditer(semantic_element, searchable__string)])
    
    #gives a list of lists, need to flatten
    start_index = [item  for sublist in start_index for item in sublist]
    start_index.sort()
    
    end_index = []
    
    for index in start_index:
        end_index.append(searchable__string.find(' ', index))
        
    all_tables = []
    
    for start, end in zip(start_index,end_index):
        all_tables.append(searchable__string[start:end])

    return all_tables

all_sources = looking_for_table(query,source_to_search_for)
all_destinations = looking_for_table(query,destination_to_search_for)

print(all_sources, all_destinations)
