# Create a function that takes an integer n and returns the factorial of factorials.
# See below examples for a better understanding:
#
# Examples
# fact_of_fact(4) ➞ 288
# # 4! * 3! * 2! * 1! = 288
#
# fact_of_fact(5) ➞ 34560
#
# fact_of_fact(6) ➞ 24883200

def factorial(i):
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j
    return fact


def fact_of_fact(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * factorial(i)
    print(fact)


if __name__ == "__main__":
    fact_of_fact(4)  # ➞ 288
    fact_of_fact(5)  # ➞ 34560
    fact_of_fact(6)  # ➞ 24883200
