#nested loops = the 'inner Loop' will finish before the 'outer loop'

rows = int(input("How Many rows? :"))
collumns = int(input("how many colluns? : "))
symbol = input("input a symbol :")

for i in range (rows):
    for j in range (collumns):
        print (symbol, end = "")
    print()
