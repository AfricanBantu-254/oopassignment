class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height is not None else width

    def area(self):
        return self.width * self.height


square = Rectangle(5)
rectangle = Rectangle(4, 6)
print("The Square's area is:", square.area())
print("The Rectangle's area:", rectangle.area())
