# 4. Create a class called "Student" with attributes name and grade.
# Implement a method to calculate and return the letter grade based on a numeric score.


class Student:
    def __init__(self, name, score):
        self.output = []
        self.__name = name
        self.__score = score

    def assign(self, grade):
        self.output.append(self.__name)
        self.output.append(grade)
        return self.output

    @property
    def get_grade(self):
        if 45 < self.__score <= 50:
            return self.assign("A")
        elif 35 < self.__score <= 45:
            return self.assign("B")
        elif 25 < self.__score <= 35:
            return self.assign("C")
        else:
            return self.assign("D")


if __name__ == "__main__":
    obj1 = Student("Tom", 50)
    obj2 = Student("Jerry", 40)
    obj3 = Student("ravi", 12)
    print(obj1.get_grade, obj2.get_grade, obj3.get_grade)
