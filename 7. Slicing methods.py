#Slicing = membuat substring dengan mengambil dri string lain
#indexing [] atau slice
#[start:stop;step]

nama ="Felix Angga Resky"
huruf_depan = nama[0]
nama_depan = nama [:6]
nama_tengah = nama [6:11]
nama_belakang = nama [12:]
#bisa juga seperti ini 
nama_lengkap = nama [:]
huruf_ganjil = nama [::2]
huruf_setiap_3_huruf = nama [::3]
nama_terbalik =nama[::-1]

#print (huruf_depan)
#print (nama_depan)
#print (nama_tengah)
#print (nama_belakang)
#print (nama_lengkap)
#print (huruf_ganjil)
#print (huruf_setiap_3_huruf)
#print (nama_terbalik)


#slice()
website1 = "https://www.itenas.ac.id"
website2 = "https://www.wikipedia.ac.id"
slice = slice (12,-6)

print (website1[slice])
print (website2[slice])