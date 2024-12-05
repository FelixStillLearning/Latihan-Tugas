'''
Reading File using python
'''
try:
    with open ('fille.tx') as file:
        print (file.read())
except FileNotFoundError:
        print ("file ga ada")

try:
    with open ('fille.txt') as file:
        print (file.read())
except FileNotFoundError:
        print ("file ga ada")