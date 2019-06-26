import random
name = input("Enter your name: ")
salary = int(input("Enter your salary: "))
raise_per = random.randint(1,99)
raise_amount = salary+raise_per*salary/100
print(f"{name}, your current salary is ${salary}")
print(f"Your raise is {raise_per}% of ${salary}")
print(f"{name}, your new salary is ${raise_amount}")

