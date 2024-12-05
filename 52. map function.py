
'''
map function = used to apply a function to every item in an iterable (list, tuple, etc.)

map(function,iterable)

'''

#ini adalah contoh tuple 
toko_baju = [("baju", 10.000),
             ("celana", 20.000),
             ("celana panjang", 30.000)]

ke_amerika = map(lambda item: (item[0], item[1]/15000), toko_baju)

toko_amerika = list(ke_amerika)

for i in toko_amerika:
    print(i) 

