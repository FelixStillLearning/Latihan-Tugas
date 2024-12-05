#Logical Operator (And,Or,Not) = digunakan untuk mengecek dua atau lebih conditional statemenet itu true atau tidak

suhu = int(input("masukkan suhu:"))

#if suhu >= 0 and suhu <= 30:
#    print ("cuacanya bagus")
#    print ("keluar yuk")
#elif suhu <= 0 or suhu >= 30:
#    print("cuacanya buruk")
#    print("dah diem dieumah aja")

if not (suhu >= 0 and suhu <= 30):
    print ("cuacanya bagus")
    print ("keluar yuk")
elif not (suhu <= 0 or suhu >= 30):
    print("cuacanya buruk")
    print("dah diem dieumah aja")
#Penambhaan Not Dalam if atau else hanya membuat reverse nya, tru menjadi false dan false menjadi true
#dan bisa hanya menggunakan 1 kondisi syaratv