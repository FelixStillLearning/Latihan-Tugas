nama = "FelixCorleone"
date = "04082004"
print (len(nama))
print (nama.find ("F"))
print (nama.find ("C"))
#untuk mencari sebuah karakter didalam string

print (nama.capitalize())
#untuk kapital karakter paling depan di dalam string

print (nama.upper())
#untuk capslock semua karakter didalam string

print (nama.lower())
#untuk membuat karakter menjadi kecil semua

print (nama.isdigit())
print (date.isdigit())
#jika input string berisi huruf maka output nya false 
#jika input string berisi angka maka output nya true

print (nama.isalpha())
print (date.isalpha())
'''''
jika input string berisi huruf maka outputnya true
jika inout string berisi angka maka outout nya false
(tidak termasuk spasi)
'''
print (nama.count("e"))
#menghitung total jumalh karakter yang disebutkan

print (nama.replace("e","o"))
#untuk mengubah karakter dengan apa yang kita mau

print (nama*3)
#fitur untuk mengalikan variable
