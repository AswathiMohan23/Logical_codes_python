"""
Bank class:

    Attributes: name (string), branches (list of Branch objects)
    Methods:
    add_branch(branch): Add a new branch to the bank.
    get_total_balance(): Return the total balance of all accounts in the bank.
    get_customer_with_highest_balance(): Return the customer object with the highest balance in the bank.

Branch class:
    Attributes: name (string), customers (list of Customer objects)
    Methods:
    add_customer(customer): Add a new customer to the branch.
    get_total_balance(): Return the total balance of all accounts in the branch.
    get_customer_with_highest_balance(): Return the customer object with the highest balance in the branch.

Customer class:
    Attributes: name (string), accounts (list of Account objects)
    Methods:
    add_account(account): Add a new account to the customer.
    get_total_balance(): Return the total balance of all accounts of the customer.
    get_account_with_highest_balance(): Return the account object with the highest balance of the customer.
Account class:
    Attributes: account_number (string), balance (float)
    Methods: None
    Your task is to implement these classes and write a program to simulate the banking system. The program should create a bank with multiple branches and customers, each having multiple accounts. It should then perform the following operations:

Add branches, customers, and accounts to the bank.
Deposit and withdraw money from the accounts.
Retrieve and display the total balance of the bank, branch, and customer.
Retrieve and display the customer and account with the highest balance in the bank.
"""


def finding_sum(i, value):
    sum = i + value
    return sum


class Bank:
    def __init__(self, name):
        self.name = name
        self.branch = {}

    def add_branch(self, branch_name):
        self.branch.update({self.name: branch_name})
        return self.branch

    def get_total_balance(self, balance_dict):
        sum = 0
        for i in balance_dict:
            value = balance_dict.get(i)
            sum = finding_sum(sum, value)
        return sum

    def customer_with_highest_balance(self, balance_dict):
        return max(balance_dict, key=balance_dict.get)


class Branch:
    def __init__(self, branch_name):
        self.name = branch_name
        self.customers = {}

    def add_customers(self, customer_list):
        self.customers.update({self.name: customer_list})
        return self.customers

    def get_balance_of_all_the_accounts(self, added_account_list):
        result = []
        sum = 0
        for i in added_account_list:  # [{"1":}]
            for j in i:
                dict_value = i[j]
                result.append(dict_value[1])
        for i in result:
            sum = finding_sum(i, sum)
        return sum


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, list_of_accounts, num, balance):
        self.accounts = list_of_accounts
        dict1 = list_of_accounts[0]
        last_key = list(dict1)[-1]
        key_value = last_key + 1
        self.accounts.append({key_value: [num, balance]})

        return self.accounts

    def get_total_balance(self, added_account_list):
        self.accounts = added_account_list
        sum = 0
        for i in self.accounts:
            for j in i:
                dict_value = i[j]
                sum = finding_sum(sum, dict_value[1])
        return sum

    #
    def get_account_with_highest_balance(self, added_account_list):
        self.accounts = added_account_list
        result = {}
        for i in self.accounts:
            for j in i:
                dict_value = i[j]
                result.update({dict_value[0]: dict_value[1]})
            return max(result, key=result.get)


class Account:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance


if __name__ == "__main__":
    balance_dict = {}
    acc1 = Account("1234", 1234.00)
    acc2 = Account("1134", 500.00)
    acc3 = Account("4567", 1000.00)
    list_of_accounts = [{1: [acc1.acc_num, acc1.balance], 2: [acc2.acc_num, acc2.balance]}]
    cust = Customer("Tom")
    added_account_list = cust.add_account(list_of_accounts, acc3.acc_num, acc3.balance)
    balance = cust.get_total_balance(added_account_list)
    balance_dict.update({cust.name: balance})
    print("total balance = ", balance)
    highest_acc = cust.get_account_with_highest_balance(added_account_list)
    print("acc with highest balance = ", highest_acc)
    branch = Branch("Tom")
    added_customer = branch.add_customers(added_account_list)  # after adding branch
    print("added a customer :", added_customer)
    balance_of_all_accounts = branch.get_balance_of_all_the_accounts(added_account_list)
    print("total amount in all the accounts :", balance_of_all_accounts)
    bank = Bank("mangalore")
    branches = bank.add_branch(added_customer)
    print(bank.add_branch(added_customer))
    print("===============================================================================")
    acc3 = Account("1010", 100.00)
    acc4 = Account("2020", 200.00)
    acc5 = Account("3030", 50.00)
    list_of_accounts = [{1: [acc3.acc_num, acc3.balance], 2: [acc4.acc_num, acc4.balance]}]
    cust = Customer("John")
    added_account_list = cust.add_account(list_of_accounts, acc5.acc_num, acc5.balance)
    balance = cust.get_total_balance(added_account_list)
    balance_dict.update({cust.name: balance})
    print("total balance = ", balance)
    highest_acc = cust.get_account_with_highest_balance(added_account_list)
    print("acc with highest balance = ", highest_acc)
    branch = Branch("John")
    added_customer = branch.add_customers(added_account_list)  # after adding branch
    print("added a customer :", added_customer)
    balance_of_all_accounts = branch.get_balance_of_all_the_accounts(added_account_list)
    print("total amount in all the accounts :", balance_of_all_accounts)
    bank = Bank("calicut")
    print(bank.add_branch(added_customer))
    print("=====================================================================")
    print("\ntotal balance in all account : ", bank.get_total_balance(balance_dict))
    print("\ncustomer with max balance : ", bank.customer_with_highest_balance(balance_dict))
