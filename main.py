# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re
import os
import pandas as pd

def looking_for_table(searchable__string: str,semantic_elements: list) -> list:
    """
    Parameters
    ----------
    searchable__string : list
        String that contains the SQL query that you want to parse
    semantic_elements : list
        List of semantic elements that sit before your table name
        For exemple, JOIN, FROM, INSERT INTO

    Returns
    -------
    list
        Returns a list of table names
    """
    
    #nested list comprehension here
    #outer loops over the list of semantic elements
    #while inner goes over the full string and finds every occurence of the semantic element
    start_index = [[m.end() + 1 for m in re.finditer(semantic_element, searchable__string)] for semantic_element in semantic_elements]
    
    #gives a list of lists, need to flatten
    start_index = [item  for sublist in start_index for item in sublist]
    start_index.sort()
    
    #we get the end_index but getting the index of the next space after the start_index
    end_index = [searchable__string.find(' ', index) for index in start_index]
    
    #we look for the substring based on the 2 lists of indexes    
    all_tables = [searchable__string[start:end] for start,end in zip(start_index,end_index)]

    return all_tables

def read_repository(repos_path: str) -> list:
    """
    Parameters
    ----------
    repos_path : str
        root path of the repository that needs to be parsed.

    Returns
    -------
    list
        list of full path for every file contains under the root.
    """
    all_files_paths = []
    
    for dirpath, dirnames, filenames in os.walk(repos_path):
        if len(filenames) == 0:
            continue
        else:
            for filename in filenames:
                all_files_paths.append(dirpath +  "\\" + filename)
    
    return all_files_paths

all_queries = []
all_file_paths = []
               
for file_path in read_repository(r"C:\Users\Calixte\Desktop\Repos Example"):   
    with open(file_path,"r") as f:
        all_queries.append(f.read())
        all_file_paths.append(file_path)

source_to_search_for = ['FROM','JOIN']
destination_to_search_for = ['INSERT INTO','CREATE TABLE IF NOT EXISTS']

all_sources = []
all_destinations = []

for query in all_queries:
    all_sources.append(looking_for_table(query,source_to_search_for))
    all_destinations.append(looking_for_table(query,destination_to_search_for))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    