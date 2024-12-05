#Loop control Statement = change the control flow of the loop 
#break,Continue,Pass

while True :
    name = input ("enter your name :")
    if name == "Felix":
        break

phone_number = "0895-3841-21689"

for i in phone_number:
    if i == "-":
        continue
    print (i,end = "")

for j in range (1,21):
    if j == 13:
        pass
    else:
        print(j)