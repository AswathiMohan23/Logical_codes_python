# 10. Create a class called "EmployeeManagement" that represents a company's employee management
# system. It should have methods to add an employee, remove an employee, and display the list of
# employees.

class EmployeeManager:
    def __init__(self):
        self.employee_record=[]

    def add_employee(self,name):
        self.employee_record.append(name)

    def remove_employee(self,name):
        self.employee_record.remove(name)

    def display(self):
        return self.employee_record


if __name__=="__main__":
    obj=EmployeeManager()
    obj.add_employee("Tom")
    obj.add_employee("Jerry")
    obj.add_employee("riya")
    obj.add_employee("reshma")
    print(obj.display())
    obj.remove_employee("riya")
    print(obj.display())
