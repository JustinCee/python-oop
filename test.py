class Shapes:
    def __init__(self, name, side):
        self.name = name
        self.side = side

    def Area(self):
        print("I am a :" + self.name + "\n" +
              "I have " + self.side + "sides")


obj_shape = Shapes("shape", "so many")
obj_shape.Area()


class Rectangle(Shapes):
    def __init__(self, len1, wid1):
        self.length = len1
        self.width = wid1

    def Area(self):
        result = self.length * self.width
        return result


obj_book = Rectangle(10, 7)
obj_screen = Rectangle(5, 7)
print("The area of a book is " + str(obj_book.Area()))
print("The area of a screen is " + str(obj_screen.Area()))


class Triangle(Shapes):
    def __init__(self, base1, height1):
        self.base = base1
        self.height = height1

    def Area(self):
        result = (0.5 * self.base * self.height)
        return result


class Circle(Shapes):
    def __init__(self, radius1, pi1):
        self.radius = radius1
        self.pi = pi1

    def Area(self):
        result = self.radius * self.pi
        return result
