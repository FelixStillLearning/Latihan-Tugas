'''
list chomprehension = a way to create a new list with less syntax
                        can mymic certain lambda function, easier to read
                        list = [expression for item in iretable]
                        list = [expression for item in iretable if conditional]
                        list = [expresiion if else for item iretable]
                        
                        
'''
pangkat2 = []               #buat list kosong 
for i in range (1,11):      #buat loop for 
    pangkat2.append(i*i)    #berikan perintah seriap ;oop mealkukan apa
print(pangkat2)

squares = [i * i for i in range(1,12)] #bisa disingkat menjadi seperti ini
print(squares)

students = [100,90,80,70,60,50,40,30,0]
passed_students = list(filter(lambda x: x > 60,students))
print (passed_students)

lulus_kelas = [i for i in students if i >= 60]
print(lulus_kelas)

diatas_kkm = [i if i >= 60 else "Failed" for i in students]
print(diatas_kkm)