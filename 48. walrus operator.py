'''
walrus operator :=

python update 3.8
assigntment expression aka alrus operator
assign value to variables as part of a larger expression  


happy = True 
print (happy)

print(sad := False)


foods = list()
while True:
    food = input("makanan apa yang kamu suka?")
    if food == "quit":
        break
    foods.append(food)

'''

foods = list()
while food := input("makanan apa yang kamu suka?") != "quit":
    foods.append(food)