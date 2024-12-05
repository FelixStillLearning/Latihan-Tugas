#str.format() = optional method that gives user more control when displaying outputs

hewan = "sapi"
makan = "rumput"
print("pagi hari "+hewan+" makan "+makan+" segar")

print("pagi hari {} makan {} segar".format(hewan,makan))

#positional argument
print("pagi hari {1} makan {0} segar".format(hewan,makan))

#keyword argument
print("pagi hari {animal} makan {animal} segar".format(animal="cow",food="grass"))



look = "ganteng"
sifat = "baik"
text = "felix itu {} dan juga {}"

print(text.format(look,sifat))

nama = "felix"

print ("halo nama ku adalah {}".format(nama))
print ("halo nama ku adalah {:10} nama ku jarang disebut".format(nama))
print ("halo nama ku adalah {:<10} nama ku keren".format(nama))
print ("halo nama ku adalah {:>10} siapa dia".format(nama))
print ("halo nama ku adalah {:^10} nama ku keren".format(nama))

tinggi = 1000
print("tinggi ku adalah {:,}".format(tinggi))
print("tinggi ku adalah {:.3f}".format(tinggi))
print("tinggi ku adalah {:b}".format(tinggi))
print("tinggi ku adalah {:o}".format(tinggi)) #octal 
print("tinggi ku adalah {:x}".format(tinggi)) #hexadecimal
print("tinggi ku adalah {:E}".format(tinggi)) #notasi ilmiah

