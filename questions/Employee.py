# Design a class called "Employee" with attributes name, salary, and experience.
# Implement a method to
# give an annual raise to the employee based on their experience.

class CustomException(Exception):
    def __init__(self, experience, message="Experience is below 1 year"):
        self.experience = experience
        self.message = message
        super().__init__(self.message)


class Employee:
    def __init__(self, name, salary, experience):
        self.__name = name
        self.__salary = salary
        self.__experience = experience

    @property
    def get_anual_raise(self):
        if self.__experience == 5:
            self.__salary += 15000
            return self.__salary
        elif 2 <= self.__experience < 5:
            self.__salary += 10000
            return self.__salary
        elif 1 <= self.__experience < 2:
            self.__salary += 5000
            return self.__salary
        raise CustomException(self.__experience)


if __name__ == "__main__":
    obj1 = Employee("Tom", 50000, 2)
    obj2 = Employee("ravi", 90000, 5)
    obj3 = Employee("jerry", 30000, 1)
    print(obj1.get_anual_raise, obj2.get_anual_raise, obj3.get_anual_raise)
