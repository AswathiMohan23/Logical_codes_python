# 6. Implement a class called "Circle" with attributes radius and color.
# Include methods to calculate the area and circumference of the circle.
import math


class Circle:
    def __init__(self,radius,color):
        self.__radius=radius
        self.__color=color

    @property
    def area(self):
        return math.pow(self.__radius,2)*3.14

    @property #here method behaves like a variable
    def circumference(self):
        return 2*3.14*self.__radius


if __name__=="__main__":
    obj=Circle(3,"red")
    print(obj.area)
    print(obj.circumference)
    obj2=Circle(5,"blue")
    print(obj2.area)
    print(obj2.circumference)
