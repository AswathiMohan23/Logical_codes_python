# 3.Given an integer, create a function that returns the next prime.
# If the number is prime, return the number itself.
#
# Examples
# next_prime(12) ➞ 13
#
# next_prime(24) ➞ 29
#
# next_prime(11) ➞ 11
# 11 is a prime, so we return the number itself.

def is_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def next_prime(num):
    count = 0
    i = 1
    if is_prime(num):
        return num
    else:
        while count == 0:
            if is_prime(num + i):
                count += 1
                return num + i
            else:
                i = i + 1


if __name__ == "__main__":
    print(next_prime(11))  # ➞ 11
    print(next_prime(24))  # ➞ 29
    print(next_prime(12))  # ➞ 13
