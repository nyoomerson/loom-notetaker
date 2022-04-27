import os 
import re

from os import scandir, walk

def scan_direct():

    x = os.scandir()

    directoryContent = []

    for i in x:
        i = str(i)[11:-2]
        directoryContent.append(i)

    return directoryContent

def match_direct(keyword):
    search_space = scan_direct()
    results = []
    for line in search_space:
        if re.search(keyword, line):
            results.append(line)
    return results
