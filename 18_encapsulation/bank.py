class BankAccount:
    def __init__(self, balance):
        # Public variable (accessible from anywhere)
        self.account_owner = "John Doe"
        
        # Protected variable (convention for internal use)
        self._account_type = "Savings"
        
        # Private variable (name mangled)
        self.__balance = balance

    # Private method (name mangled)
    def __display_balance_info(self):
        return f"Current balance information: {self.__balance}"

    # Public method to access the private method and variable
    def check_balance(self):
        print(self.__display_balance_info())

# Usage
account = BankAccount(1000)

# Accessing public attribute (works)
print(f"Owner: {account.account_owner}")

# Accessing protected attribute (works, but discouraged by convention)
print(f"Type: {account._account_type}")

# Calling public method (works)
account.check_balance()

# Attempting to access private variable directly (raises AttributeError)
# print(account.__balance) # This line would cause an error

# Accessing the "private" variable using name mangling (works, but strongly discouraged)
print(f"Mangled balance access: {account._BankAccount__balance}")
