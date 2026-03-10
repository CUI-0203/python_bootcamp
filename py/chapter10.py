# FUNTIONS

# Functions with parameters
def greet_user(name):
    print(f"Hello,{name}!")

greet_user("Alice")

# Functions with return values
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  #8

# Default parameter values
def greet_with_tittle(name, title="MRr."):
    return f"Hello,{title}{name}!"

print(greet_with_tittle("Smith"))  # "Hello,Mr. Smith!"
print(greet_with_tittle("Johnson","Dr.")) # "Hello,Dr. Johnson!"

# *args - variable number of arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5)) # 15

# **kwargs - keyword arguments
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=30, city="New York")

# Cobining *args and **kwargs
def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="Alice", age=25)

# Lambda functions(anonymous functions)
square = lambda x: x ** 2
print(square(5)) # 25

add = lambda x, y: x + y
print(add(3, 4)) # 7

#exercise

def is_prime(n):
    if n<=1:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    
        return True
    
print(is_prime(3))

    
    