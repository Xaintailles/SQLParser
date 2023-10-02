# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 17:44:38 2023

@author: Calixte
"""

""" 
check the following link for GCP resevred keywords
https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#reserved_keywords
"""

def get_reserved_keywords(sql_dialect: str) -> list:
    
    valid_sql_dialects = [
        'gcp'
        ]
    
    gcp_keywords = [
        'ALL',
        'AND',
        'ANY',
        'ARRAY',
        'AS',
        'ASC',
        'ASSERT_ROWS_MODIFIED',
        'AT',
        'BETWEEN',
        'BY',
        'CASE',
        'CAST',
        'COLLATE',
        'CONTAINS',
        'CREATE',
        'CROSS',
        'CUBE',
        'CURRENT',
        'DEFAULT',
        'DEFINE',
        'DESC',
        'DISTINCT',
        'ELSE',
        'END',
        'ENUM',
        'ESCAPE',
        'EXCEPT',
        'EXCLUDE',
        'EXISTS',
        'EXTRACT',
        'FALSE',
        'FETCH',
        'FOLLOWING',
        'FOR',
        'FROM',
        'FULL',
        'GROUP',
        'GROUPING',
        'GROUPS',
        'HASH',
        'HAVING',
        'IF',
        'IGNORE',
        'IN',
        'INNER',
        'INTERSECT',
        'INTERVAL',
        'INTO',
        'IS',
        'JOIN',
        'LATERAL',
        'LEFT',
        'LIKE',
        'LIMIT',
        'LOOKUP',
        'MERGE',
        'NATURAL',
        'NEW',
        'NO',
        'NOT',
        'NULL',
        'NULLS',
        'OF',
        'ON',
        'OR',
        'ORDER',
        'OUTER',
        'OVER',
        'PARTITION',
        'PRECEDING',
        'PROTO',
        'QUALIFY',
        'RANGE',
        'RECURSIVE',
        'RESPECT',
        'RIGHT',
        'ROLLUP',
        'ROWS',
        'SELECT',
        'SET',
        'SOME',
        'STRUCT',
        'TABLESAMPLE',
        'THEN',
        'TO',
        'TREAT',
        'TRUE',
        'UNBOUNDED',
        'UNION',
        'UNNEST',
        'USING',
        'WHEN',
        'WHERE',
        'WINDOW',
        'WITH',
        'WITHIN',
        ]
    
    if sql_dialect not in valid_sql_dialects:
        raise ValueError(f'Please enter an sql dialect within the following list: {valid_sql_dialects}')
    elif sql_dialect == 'gcp':
        reserved_keywords = gcp_keywords
    
    return reserved_keywords

print(get_reserved_keywords(sql_dialect='gcp'))