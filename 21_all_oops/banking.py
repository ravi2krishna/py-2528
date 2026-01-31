# Implement Encapsulation 
class BankAccount:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.__balance = balance   

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


# Implement Abstraction 
from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

# Implement Inheritance 
class SavingsAccount(Account):
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
            
class CurrentAccount(Account):
    def __init__(self, balance, overdraft_limit):
        self.__balance = balance
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount): # polymorphic in nature 
        if amount <= self.__balance + self.overdraft_limit:
            self.__balance -= amount
        else:
            print("Overdraft limit exceeded")

