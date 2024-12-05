# Tuple = Collection which is ordered and unchangeable 
#         used to group together related data

mahasiswa = ("Felix",19,"Pria")

print(mahasiswa.count("Felix"))
print(mahasiswa.index("Pria"))

for i in mahasiswa:
    print(i)

for k in range(len(mahasiswa)):
    print(mahasiswa[k])

if "Felix" in mahasiswa:
    print ("ada di tuple")