# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re
import os
import pandas as pd

def looking_for_table(searchable__string: str,
                      semantic_elements: list,
                      cleaning_list=['\n','(',')']) -> list:
    """
    Parameters
    ----------
    searchable__string : str
        string that will be searched for table references.
    semantic_elements : list
        List of SQL semantic that is used to identify tables.
    cleaning_list : list
        List of characters that we want to remove.

    Returns
    -------
    list
        List of tables that have been detected and parsed from the SQL string.

    """
    
    #nested list comprehension here
    #outer loops over the list of semantic elements
    #while inner goes over the full string and finds every occurence of the semantic element
    start_index = [[m.end() + 1 for m in re.finditer(semantic_element, searchable__string)] for semantic_element in semantic_elements]
    
    #gives a list of lists, need to flatten
    start_index = [item  for sublist in start_index for item in sublist]
    start_index.sort()
    
    #we get the end_index but getting the index of the next space after the start_index
    space_end_index = [searchable__string.find(' ', index) for index in start_index]
    line_end_index = [searchable__string.find('\n', index) for index in start_index]
    parenthesis_end_index = [searchable__string.find('(', index) for index in start_index]
    
    end_index = []
    
    #Stupid line of code here.
    #We identify new lines, spaces or (
    #From there we find where each of these elements is after the start index.
    #find returns -1 as default when not found, so we need to remove negative values.
    #Then we get the minimum of the positive numbers, and that is the cut-off
    
    for i in range(len(space_end_index)):
        
        all_next_indexes = []
        
        all_next_indexes.append(space_end_index[i])
        all_next_indexes.append(line_end_index[i])
        all_next_indexes.append(parenthesis_end_index[i])
        
        all_next_indexes = list(filter(lambda x : x > 0, all_next_indexes))
        
        end_index.append(min(all_next_indexes))
    
    #we look for the substring based on the 2 lists of indexes    
    all_tables = [searchable__string[start:end] for start,end in zip(start_index,end_index)]
    
    #doing some cleaning_up, based on the list we get begining of the function
    for string_to_replace in cleaning_list:
        all_tables = [s.replace(string_to_replace,'') for s in all_tables]

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
cleaning_list = ['\n','(',')']

all_sources = []
all_destinations = []


for query in all_queries:
    all_sources.append(looking_for_table(query,source_to_search_for,cleaning_list))
    all_destinations.append(looking_for_table(query,destination_to_search_for,cleaning_list))
    
print(min('Thisisanexample'.find(' '),'This isanexample'.find(' ')))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    