# Create the instance attributes fullname and email in the Employee class. Given a
# persons first and last names:Form the fullname by simply joining the first and last name together,
# separated by a space.Form the email by joining the first and last name together with a . in between,
# and follow it with @company.com at the end. Make sure the entire email is in lowercase.
# Examples
# emp_1 = Employee("John", "Smith")
# emp_2 = Employee("Mary",  "Sue")
# emp_3 = Employee("Antony", "Walker")
# emp_1.fullname ➞ "John Smith"
#
# emp_2.email ➞ "mary.sue@company.com"
# emp_3.firstname ➞ "Antony"

def solution(input_list):
    email_list = []
    full_name = " ".join(input_list)
    email_list.append(input_list[0])
    email_list.append(input_list[1] + "@company")
    email_list.append("com")
    email = ".".join(email_list)
    print("full name is : ", full_name)
    print("email is : ", email)


if __name__ == "__main__":
    input_list = ["John", "Smith"]
    solution(input_list)
