import os 

from os import scandir, walk

def scan_direct():

    x = os.scandir()

    directoryContent = []

    for i in x:
        print(i)
        directoryContent.append(i)

scan_direct()
