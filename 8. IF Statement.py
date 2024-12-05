#if statement = kumpulan kode yang akan di eksekusi jika kondisinya True

umur = int(input("berapakah umurmu?: "))

if umur == 100:
    print("tua banget lu")
elif umur >= 18:
    print("anda sudah dewasa")
elif umur < 0:
    print("anda belum lahir")
else:  
    print("anda masih bocah")

#akan yang pertama dulu karena berurutan dri yang pertama dahulu 

