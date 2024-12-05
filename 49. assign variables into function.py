'''
assign variables into function = mengisi variable ke dalam fungsi
contoh : 
''' 

def fungsi():
    a = 10
    b = 20
    c = a + b
    print(c)

penjumlahan = fungsi
fungsi()
penjumlahan()
print(penjumlahan)
print(fungsi)

#atau bisa dicoba seperti ini 

bilang = print

bilang("aku ganteng banget cuyyyyy")