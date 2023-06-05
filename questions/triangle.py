# 9. Implement a class called "Triangle" with attributes side1, side2, and side3.
# Include a method to check if the triangle is equilateral, isosceles, or scalene.

class Triangle:
    def __init__(self, side1, side2, side3):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    @property
    def type_of_triangle(self):
        if self.__side1 != self.__side2 and self.__side1 != self.__side3 and self.__side2 != self.__side3:
            return "scalene"
        elif self.__side1 == self.__side2 and self.__side1 == self.__side3 and self.__side2 == self.__side3:
            return "equilateral"
        else:
            return "isosceles"


if __name__ == "__main__":
    # consider side3 as base and side1 and side2 as opposite sides
    obj = Triangle(4, 4, 4)
    print(obj.type_of_triangle)
    obj1 = Triangle(4, 4, 5)
    print(obj1.type_of_triangle)
    obj3 = Triangle(4, 3, 5)
    print(obj3.type_of_triangle)
