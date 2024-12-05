'''
move a file using python
'''

import os
source = "34a. pindahkan file.txt"
destination = "C:\\Users\\Felix Corleone\\Documents"

try:
    if os.path.exists(destination):
        print("file ada")
    else:
        os.replace(source, destination)
        print(source + " dah dipindahkan")
except:
    print(source + " file tidak ada")