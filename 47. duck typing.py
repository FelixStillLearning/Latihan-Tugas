'''
duck typing = 'If it looks like a duck, swims like a duck, and quacks like a duck, then it is a duck.'
            = concept where the object's behaviour is less important than its type
            = class type that an object is an instance of (or an instance of one of its subclasses)


            Duck typing adalah konsep dalam pemrograman yang digunakan dalam bahasa pemrograman dinamis
            seperti Python. Konsep ini mengacu pada cara sebuah objek diidentifikasi berdasarkan
                perilakunya (behavior) daripada tipe atau kelas spesifiknya.

'''

class duck :
    def walk (self):
        print ("hewan ini sedang berjalan")
    
    def talk (self):
        print ("hewan  ini bersuara qwuack quack")

class chicken:
    def walk (self):
        print ("hewan ini sedang berjalan")
    def talk (self):
        print ("hewan ini ersuara petok petok")

class person:
    def catch (self, duck):
        duck.walk()
        duck.talk()
        print("you caught the clitter")

duck = duck()
chicken = chicken()
person = person()

person.catch(chicken)