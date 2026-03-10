# CLASSES AND OBJECTS

# Basic class definition
class Person :
    # Class attribute (sharedby all instances)
    species = "Homo sapiens"

    # Constructor method
    def __init__(self, name, age):
        # Insatnce attributes
        self.name = name
        self.age = age

    # Insatnce method
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    # Method with parameters
    def have_birthdays(self):
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age}"
    
    # Creating objects (insatces)
    person1 = Person("Mabel", 28)
    person2 = Person("Mike", 35)

    # Accessing attributes
    print(person1.name)  #"Mabel"
    print(person1.age)  # 28

    # Calling methods
    print(person1.introduce())
    print(person1.have_birthdays())

    # Class attributes
    print(Person.species)  #"Homo sapiens"
    print(person1.species)  #"Homo sapiens"

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
         self.balance += amount
         self.transaction_history.append(f"Deposited ${amount}")
         return f"Deposited $(amount). New balance: $(self.balance)"
        else:
         return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
           self.balance -= amount
           self.transition_history.append(f"withdraw ${amount}")
        else:
           return"Invalid withdrawal amount or insufficient funds"


    def get_balance(self):
        return f"Current balance: ${self.balance}"

    def get_transaction_history(self):
        return self.transaction_history

# Using the BankAccount class
account = BankAccount("12345","Alice",1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())

    
    


