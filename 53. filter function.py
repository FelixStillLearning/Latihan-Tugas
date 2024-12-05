''' 
filter funtion = mengembalikan list yang memenuhi kriteria yang ditentukan 
filter(function, iterable )
'''

nama_teman = [("budi", 90),
            ("andi", 80),
            ("joko", 100),
            ("siti", 70),
            ("felix", 60),]

nilai = lambda data: data[1] >= 75

kkm = filter(nilai,nama_teman)
for i in kkm :
    print(i)