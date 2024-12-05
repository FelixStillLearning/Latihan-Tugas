'''
pass object as aargument = pass an object as an argument to a function

'''

class mobil :

    color = None 

class motor :

    color = None

def change_color(vehicle, color) :

    vehicle.color = color
    

mobil_1 = mobil()
mobil_2 = mobil()
mobil_3 = mobil()


motor_1 = motor()
motor_2 = motor()
motor_3 = motor()

change_color(mobil_1, "red")
change_color(mobil_2, "blue")
change_color(mobil_3, "green")

change_color(motor_1, "red")
change_color(motor_2, "blue")
change_color(motor_3, "green")

print(mobil_1.color)
print(mobil_2.color)
print(mobil_3.color)

print(motor_1.color)
print(motor_2.color)
print(motor_3.color)

