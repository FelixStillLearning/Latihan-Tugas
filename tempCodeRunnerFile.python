import time 

print(time.ctime (0)) #untuk mengetahui waktu Sekarang
print(time.time()) #untuk mengetahui detik
print(time.ctime(time.time())) #untuk mengetahui waktu Sekarang

time_object = time.localtime() #untuk mengetahui waktu Sekarang dalam bentuk struktur
time_object = time.gmtime() 
print(time_object) 

#dan ketika di print maka akan menampilkan struktur waktu Sekarang dengan berbagai variabel nya 
# dan cara untuk memisahkannya kita bisa menggunakan 
local_time = time.strftime('%Y-%m-%d %H:%M:%S', time_object)
print (local_time)

time_string = "21 april 2024"
time_object = time.strptime(time_string, '%d %B %Y')
print (time_object)
time_tuple = (2024, 4, 21, 0, 0, 0, 0, 0, 0)
print (time.mktime(time_tuple))