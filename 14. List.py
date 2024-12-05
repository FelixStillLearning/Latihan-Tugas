#List = used to store a multiple values in 1 single variable

makanan = ["nasi goreng","nasi uduk","nasi Kuning","nasi lemak"]

makanan[0] = "kepala kakap"
print(makanan)
print(makanan[0])
print(makanan[2])

#jika ingin menambahkan item ke list gunakan
makanan.append("sate")
#jika ingin menghapus item dri list
makanan.remove("nasi lemak")
#jika ingin menghapus last item dari list
makanan.pop()
#jika ingin menambhkan item pada index tertentu 
makanan.insert(0,"gulali")
#jika ingin melist sesuai abjad
makanan.sort()
#Menghapus semua list
makanan.clear()

for i in makanan:
    print(i)
