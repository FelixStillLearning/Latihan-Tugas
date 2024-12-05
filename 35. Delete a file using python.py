# 35. Delete a file using python.py
import os

path = "35a. file.txt"

try:
    os.remove(path)
except FileNotFoundError:
    print("file tidak ada")
except PermissionError:
    print("kamu tidak punya akses")
else:
    print(path + " file di hapus")