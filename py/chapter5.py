#Loops

# For loop
for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):      # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)
    
# While loop
count = 0
while count < 5:
    print(count)
    count += 1


#Loop control statements:

for i in range(10):
    if i == 3:
        continue  # Skip this iteration
    if i == 7:
        break     # Exit the loop
    print(i)


for i in range(2):
    for j in range(3):
        print(f"i: {i}, j: {j}")    

    for i in range(1,11):
        for j in range(1,11):
            print(i, "x", j, "=", i * j)

limit = 20
for num in range(2, limit + 1):
    is_prime = True
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        