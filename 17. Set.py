# Set = Collection which is unordered, unindexed and no duplicate values

utensils = {"fork","spoon","knife","napkin"}
dishes = {"bowl","plate","cup","napkin"}

# ada beberapa command yang bisa dipake ke sets
#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear() 
#utensils.update (dishes) menggabungkan salh satu set ke set lain
dinner_table = utensils.union(dishes)

for i in dinner_table:
    print (i)

#mencari yg tidak ada dimasing masing
print (dishes.difference(utensils))
print (utensils.difference(dishes))
#mencari yang sama
print (dishes.intersection(utensils))
