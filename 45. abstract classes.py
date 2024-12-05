
'''
abstract classes = class yang hanya berisi method abstract
abstract method = method yang bernilai abstract (punya deklarasi tapi tidak punya implementasi)

prevent user for creating instance of an abstract class
+ compels a user to override abstract methode in child class

'''
from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def go(self):
        pass
    def stop(self):
        pass

class Mobil(Kendaraan):
    def go(self):
        print("Mobil bergerak")
    def stop(self):
        print("Mobil berhenti")
    
class Motor(Kendaraan):
    def go(self):
        print("Motor bergerak")
    def stop(self):
        print("Motor berhenti")

# Membuat instance dari kelas
mobil_instance = Mobil()
motor_instance = Motor()

# Memanggil metode
mobil_instance.go()
motor_instance.go()

# Memanggil metode abstract
mobil_instance.stop()
motor_instance.stop()
