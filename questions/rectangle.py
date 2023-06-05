class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def perimeter(self,length,width):
        return 2*(length+width)

    def area(self,length,width):
        return length*width

if __name__=="__main__":
    obj=Rectangle(2,4)
    print(obj.perimeter(4,2))
    print(obj.area(4,2))

