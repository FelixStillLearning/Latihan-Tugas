#Nested Function Calls = Function inside another function
#                       Function call inside another function
# innermost function calls are resolved first and then outermost function 
# returned value is passed to outermost function or main function or next innermost function

num = input("Enter a number")
num = float(num)
num = abs(num)
num = round (num)
print(num)

print (round(abs(float(input("masukkan angka :")))))
angka = float(input("masukkan angka: "))
hasil = round(abs(angka))
print(float(hasil))