# Design a class called "BankAccount" that represents a bank account.
# It should have methods to deposit,
# withdraw, and check the account balance.
class CustomException(Exception):
    pass
class BankAccount:
    def __init__(self,total_savings):
        self.__total_savings=total_savings

    def deposit(self,amount):
        self.__total_savings+=amount

    def withdraw(self, amount):
        if self.__total_savings >0 and self.__total_savings>amount:
            self.__total_savings-=amount
            return
        raise CustomException("")

    @property # getters
    def balance(self):
        return self.__total_savings


if __name__ == "__main__":
    account=BankAccount(0)
    account.deposit(500)
    account.withdraw(100)
    print(account.balance)