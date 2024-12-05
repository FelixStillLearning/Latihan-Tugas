#function = a block of code which only runs when it is called

def sayHello(name='Felix'):
    print('Hello' + name)
    print('have A nice day')
sayHello()

def hello ():
    print ("hello")
    print ("Felix Corleone")

hello()
hello()
hello()

def penjumlahan (x,y):
    return x + y

print ("hasil penjumlahan = " + str(penjumlahan(20,12)))

def perkalian(i, j):
    print("masukkan angka pertama:")
    angka_pertama = int(input())
    print("masukkan angka kedua:")
    angka_kedua = int(input())
    return angka_pertama * angka_kedua

print("hasil perkalian = " + str(perkalian(20,14)))

def x (nama_depan,nama_belakang):
    print ('hello' + ' ' + nama_depan + ''+ nama_belakang)
    print ('jangan lupa makan bisi mati')

print (x("Felix", "Corleone"))