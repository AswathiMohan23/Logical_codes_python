# 3. Implement a class called "Car" with attributes make, model, and year.
# Include methods to start the car,
# stop the car, and display the car's information.


class Car:
    output = []

    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def assigning(self):
        self.output.append(self.__make)
        self.output.append(self.__model)
        self.output.append(self.__year)
        return self.output

    def starting(self):
        if "stop" in self.output:
            self.output.remove("stop")
        self.output.append("start")

    def stopping(self):
        if "start" in self.output:
            self.output.remove("start")
        self.output.append("stop")

    @property
    def display(self):
        return self.output


if __name__ == "__main__":
    obj = Car("abc", "xyz", 2010)
    obj.assigning()
    obj.starting()
    print(obj.display)
    obj.stopping()
    print(obj.display)
