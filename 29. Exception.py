# exception  = events that interrupt the normal flow of the program
'''
pembilang = int(input("masukkan pembilang : "))
penyebut = int(input("masukkan penyebut : "))
result = pembilang / penyebut
print (result)
'''

#tapi jika 5 dibagi o akan error
#oleh karena itu ada exception

""" 
oleh karena itu bisa di tulis seperti ini
"""
try:
    pembilang = int(input("masukkan pembilang : "))
    penyebut = int(input("masukkan penyebut : "))
    result = pembilang / penyebut
except ZeroDivisionError as e: 
    print (e)
    print ("kamu tidak bisa membagi angka dengan 0")
except ValueError as e:
    print (e)
    print ("kamu harus memasukkan angka")    
except Exception as e:
    print (e)
    print ("kamu memasukkan angka yang salah")
else:
    print (result)
finally:
    print ("program selesai")