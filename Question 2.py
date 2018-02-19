#Q2. Create a class Circle which has a class variable PI with the value=22/7. Make two methods getArea and getCircumference inside this Circle class. Which when invoked returns area and circumference of each circle instances.

class Circle():
    PI=22/7
    def __init__(self,radius):
        self.radius=radius

    def get_area(self):
        return self.PI * self.radius * self.radius

    def get_circumference(self):
        return 2 * self.PI * self.radius * self.radius

result=Circle(4)
print("Area:",result.get_area())
print("Circumference:",result.get_circumference())
