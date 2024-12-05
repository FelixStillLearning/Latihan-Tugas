'''
membuat class dan sub class 
yang dimana class memiliki hal yang dimiiki class tapi berbeda dengan sub class lain
'''

class hewan:

    alive = True 

    def makan(self):
        print ("hewan ini bisa makan")
    def tidur(self):
        print("hewan ini bisa tidur")

class kelinci(hewan):
    def lari(self):
        print("hewan ini bisa lari")
class elang(hewan):
    def terbang(self):
        print("hewan ini bisa terbang")
class ikan(hewan):
    def renang(self):
        print("hewan ini bisa renang")

kelinci = kelinci()
elang = elang()
ikan = ikan()

print(kelinci.alive)
elang.makan()
ikan.tidur()

kelinci.lari()
ikan.renang()