#Q1. Create a RectangleGeometry class which takes in length and breadth as initialize parameter. Make two methods getArea and getPerimeter inside this class.  Which when invoked returns area and perimeter of each rectangle instance.

class RectangleGeometry():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def get_area(self):
        return self.length * self.breadth

    def get_perimeter(self):
        return 2 * (self.length + self.breadth)

result=RectangleGeometry(6,9)
print("Area:",result.get_area())
print("Perimeter:",result.get_perimeter())

