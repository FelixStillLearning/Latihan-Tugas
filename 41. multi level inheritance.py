'''
multi level inheritance = subclass dari subclass
'''

class organisme ():
    Alive = True 

class Hewan(organisme):
    def makan(self):
        print("hewan ini bisa makan")

class Kucing(Hewan):
    def tidur(self):
        print("hewan ini bisa tidur")

kucing = Kucing()
kucing.makan()
kucing.tidur()

print ("kucing ini hidup : ", kucing.Alive)