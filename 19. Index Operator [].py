#Index Operator [] = gives access to a sequence's elements (strings, lists, tuples, and arrays) by their positic

nama ="felix Corleone"
if (nama[0].islower()):
    print(nama.capitalize())

nama_depan = nama[:5].upper()
nama_belakang = nama [6:].lower()
huruf_terakhir = nama [-1]

print(nama_depan)
print(nama_belakang)
print(huruf_terakhir)

