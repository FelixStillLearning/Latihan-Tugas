'''
super function = used to access the parent class methods
                    it returns the temporary objects of the parent class when used

    super() = used to return the parent class
''' 

class rectangle:
    def __init__ (self,length,width):
        self.length = length
        self.width = width

class square (rectangle):
    
    def __init__ (self,length,width):
        super().__init__(length,width)
    def area (self):
        return self.length * self.width
class cube (rectangle):
    def __init__ (self,length,width,height):
        super().__init__(length,width)
        self.height = height
    def volume (self):
        return self.length * self.width * self.height


square = square(4,5)
cube = cube(4,5,6)

print (square.area())
print (cube.volume())