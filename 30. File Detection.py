'''
File Detection dasar menggunakan python untuk mengecek apakah sebuah file ada atau tidak

'''
import os

jalur = "E:\\001 Mine\\Serti"

if os.path.exists(jalur):
    print ("file ada")
    if os.path.isfile(jalur):
        print ("file")
    elif os.path.isdir(jalur):
        print("itu adalah directory")
    else :
        print ("tidak ada")
else:
    print ("file tidak ada")

