from os import walk
from os.path import isfile

def custom_os_walk(repos_to_scan: list, excluding_directories: list, root_path: str) -> list:

    paths = []

    #We scan through all repositories and extract every paths
    for repo in repos_to_scan:
        repo_path = root_path + repo

        for (dirpath, dirnames, filenames) in walk(repo_path):
            for file in filenames:
                file_to_test = str(dirpath) + r'/' + str(file)
                if isfile(file_to_test) and file.find('sql') >= 0:
                    paths.append(file_to_test)

    paths_cleaned = []

    #We exclude some keywords from paths that are not relevant
    for string in paths:
        check = True
        for exclusion in excluding_directories:
            if string.find(exclusion) != -1:
                check = False
        
        if check:
            paths_cleaned.append(string)

    return paths_cleaned