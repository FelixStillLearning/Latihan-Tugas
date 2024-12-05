'''
methode chaining = menggabungkan sebuah method dengan method lain seperti method chaining 
                       each call performs an action on the return value of the previous call
'''

class car:
    def turn_on (self):
        print ("the engine is started")
        return self
    def accelerate (self):
        print ("the car is accelerating")
        return self
    def brake (self):
        print ("the car is braking")
        return self
    def turn_off (self):
        print ("the engine is off")
        return self
     
car.turn_on(car).accelerate(car).brake(car).turn_off(car)