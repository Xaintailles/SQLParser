from tokenization import tokenize_a_file
from os_walker import custom_os_walk
import pandas as pd

root_path = r'/Users/calixte.allier/'

repositories = [
    'airflow-coredwh',
]

excluding_directories = [
    'migrations',
    'refactored',
    'git',
    'test',
]

all_file_paths = custom_os_walk(repos_to_scan=repositories, excluding_directories=excluding_directories, root_path=root_path)

all_depedencies = {}

for file in all_file_paths:
    all_depedencies[file] = tokenize_a_file(file_path= file, sql_dialect='gcp')

flat_data = {'Key': list(all_depedencies.keys()), 'Value': list(all_depedencies.values())}

df_all_dependencies = pd.DataFrame.from_dict(flat_data, orient='columns')

df_all_dependencies.to_csv('all_dependencies.csv')