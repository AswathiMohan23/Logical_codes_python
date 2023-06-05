# 8. Design a class called "Bank" that represents a bank. It should have methods to create a
# new account, close an account, and display the total number of accounts.

class CustomException(Exception):
    def __init__(self, new_count, message="no account left to close"):
        self.new_count = new_count
        self.message = message
        super().__init__(self.message)


class Bank:
    def __init__(self):
        self.new_count = 0

    def new_account(self):
        self.new_count += 1

    def close_account(self):
        if self.new_count >= 1:
            self.new_count -= 1
            return
        raise CustomException(self.new_count)

    def display_accounts(self):
        return self.new_count


if __name__ == "__main__":
    obj = Bank()
    obj.new_account()
    obj.new_account()
    obj.close_account()
    print(obj.display_accounts())
