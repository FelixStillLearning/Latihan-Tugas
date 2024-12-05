'''
multiple inheritance =  memiliki lebih dari satu induk class satu atau keduanya
analogi nya sperti rantai makanan 

''' 

class prey ():
    def makan(self):
        print("hewan ini bisa dimakan")

class predator ():
    def berburu(self):
        print("hewan ini bisa berburu mangsanya")

class kelinci(prey):
    def lari(self):
        print("hewan ini bisa lari")

class elang(predator):
    def terbang(self):
        print("hewan ini bisa terbang")

class ikan(prey, predator):
    def renang(self):
        print("hewan ini bisa renang")
        

print ("-------------------------")

kelinci = kelinci()
kelinci.makan()
kelinci.lari()

print ("-------------------------")

ikan = ikan()
ikan.berburu()
ikan.makan()
ikan.renang()

print ("-------------------------")
elang = elang()
elang.berburu()
elang.terbang()
