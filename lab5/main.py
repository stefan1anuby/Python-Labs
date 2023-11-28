import random , math


# Ex1
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle(Shape):
    def __init__(self, x, y , radius):
        super().__init__(x, y)
        self.radius = radius

    def getPerimeter(self):
        return 2 * math.pi * self.radius
    
    def getArea(self):
        return math.pi * (self.radius ** 2)
    
    
class Rectangle(Shape):
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def getArea(self):
        return self.height * self.width
    
    def getPerimeter(self):
        return 2 * (self.height + self.width)
    
class Triangle(Shape):
    def __init__(self, x1, y1 , x2 , y2 , x3 , y3):
        super().__init__(x1, y1)
        
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def _distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def getArea(self):
        a = self._distance(self.x1, self.y1, self.x2, self.y2)
        b = self._distance(self.x2, self.y2, self.x3, self.y3)
        c = self._distance(self.x3, self.y3, self.x1, self.y1)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def getPerimeter(self):
        a = self._distance(self.x1, self.y1, self.x2, self.y2)
        b = self._distance(self.x2, self.y2, self.x3, self.y3)
        c = self._distance(self.x3, self.y3, self.x1, self.y1)
        return a + b + c
    
triangle = Triangle(1,1,0,0,2,2)
print(triangle.getPerimeter())


# Ex5
class Animal:
    def __init__(self , speed):
        self.speed = speed

class Mammal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        
    def spawn_living_child(self):
        return Mammal(self.speed + random.random())
    
class Bird(Animal):
    
    def __init__(self, speed, flyspeed):
        super().__init__(speed)
        self.flyspeed = flyspeed
        self.state = 'grounded'
        
    def lay_egg(self):
        return "egg"
    
    def take_off(self):
        self.state = 'flying'
        
    def land(self):
        self.state = 'grounded'

class Fish(Animal):
    
    def __init__(self, speed):
        super().__init__(speed)
        self.home = (0,0)
        
    def make_home(self, position):
        x, y = position
        self.home = (x, y)

# Ex6
class LibraryItem:
    def __init__(self):
        self.in_library = True
    def check_out(self):
        self.in_library = False
    def ret(self):
        self.in_library = True
    def display_info(self):
        print("Unidentified object")
    
class Book(LibraryItem):
    def __init__(self):
        super().__init__()
    def display_info(self):
        print("Interesting book")
    
class DVD(LibraryItem):
    def __init__(self):
        super().__init__()
    def display_info(self):
        print("Interesting DVD")
    
class Magazine(LibraryItem):
    def __init__(self):
        super().__init__()
    def display_info(self):
        print("Interesting magazine")

catalog = [Magazine(), Book(), Book(), Book(), DVD(), DVD()]

for c in catalog:
    c.display_info()