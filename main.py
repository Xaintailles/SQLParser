from tokenization import tokenize_a_file
from os_walker import custom_os_walk

root_path = r'/Users/calixte.allier/'

file_path = root_path + r'airflow-coredwh/dags/transformations/facts/fact_rfm.sql'

print(tokenize_a_file(file_path=file_path, sql_dialect='gcp'))