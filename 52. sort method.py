'''
sort() method = used with list #mengurutkan sesuai abjad
sort() function = used with iterables
'''

#anak_kelas = ["felix","gopal","reynal","firja","hari","angga"]

#anak_kelas.sort()
#anak_kelas.sort(reverse=True)
#anak_kelas_ygdisusun = sorted(anak_kelas,reverse=True)
#for i in anak_kelas:
#    print(i)

nama_orang = [("Felix", 20,"bandung"),
              ("cicip", 19, "bandung"),
              ("Restu", 21, "jakarta")]

umur = lambda umur: umur[1]
nama_orang.sort(key=umur,reverse=True)

for i in nama_orang:
    print (i)

