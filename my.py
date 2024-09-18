
##ASSIGNMENT 5

# Get user input
num = int(input("Enter a number: "))
age = int(input("Enter your age: "))
month = int(input("Enter a month (1-12): "))
year = int(input("Enter a year: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# Check if the number is positive, negative, or zero
if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")

# Check if the number is divisible by both 2 and 3 or anyone of them or not divisible by both
if num % 2 == 0 and num % 3 == 0:
    print(f"{num} is divisible by both 2 and 3.")
elif num % 2 == 0:
    print(f"{num} is divisible by 2 but not 3.")
elif num % 3 == 0:
    print(f"{num} is divisible by 3 but not 2.")
else:
    print(f"{num} is not divisible by both 2 and 3.")

# Check eligibility to vote
if age >= 18:
    nationality = input("Are you Pakistani? (yes/no): ")
    if nationality.lower() == "yes":
        print("You are eligible to vote.")
    else:
        print("Please obtain a valid ID to vote.")
else:
    print("You are not eligible to vote.")

# Determine age category
if age <= 12:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 59:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Print number of days in a month
if month in [1, 3, 5, 7, 8, 10, 12]:
    print(f"Month {month} has 31 days.")
elif month == 2:
    print(f"Month {month} has 28 days.")
else:
    print(f"Month {month} has 30 days.")

# Check if a year is a leap year
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
    ##Assignment 6
    

1. #Insert Value at Index
def insert_value(arr, index, value):
    arr.insert(index, value)
    return arr

my_array = [1, 2, 3, 5]
updated_array = insert_value(my_array, 3, 4)
print(updated_array)


2. #Shopping Cart Program

def add_items(cart, item):
    cart.append(item)
    print(f"\n{item} added to your cart")
    return cart

def remove_items(cart, item):
    if item in cart:
        cart.remove(item)
        print(f"\n{item} removed from your cart")
    else:
        print(f"\n{item} not found in cart")
    return cart

def update_items(cart, new_item, replace_item):
    if replace_item in cart:
        index = cart.index(replace_item)
        cart[index] = new_item
        print(f"\n{replace_item} changed to {new_item}")
    else:
        print(f"\n{replace_item} not found in the cart.")
    return cart

print("\n\n")
print("        =======================")
print("          Online Shopping App")
print("        =======================")

cart = []
pin = 1234

while True:
    print("\n-------------------")
    print("1. Add item")
    print("2. Remove item")
    print("3. Change item")
    print("4. Print & payment")
    print("5. Exit")
    print("-------------------")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        item = input("\n--> Enter item to add: ")
        print("__________________________")
        cart = add_items(cart, item)
        print(cart)
        print("__________________________")

    elif choice == "2":
        item = input("\n--> Enter item to remove: ")
        print("__________________________")
        cart = remove_items(cart, item)
        print(cart)
        print("__________________________")

    elif choice == "3":
        replace_item = input("\n--> Enter item to replace: ")
        new_item = input("--> Enter new item: ")
        print("__________________________")
        cart = update_items(cart, new_item, replace_item)
        print(cart)
        print("__________________________")

    elif choice == "4":
        print(cart)
        print("__________________________")
        print("\t\n--> Payment successful received!")
        print("__________________________")

    elif choice == "5":
        print("Exiting...")
        exit()
        break

    else:
        print("Option not found!")




3. #Print First 25 Integers

i = 1
while i <= 25:
    print(i)
    i += 1

4. #Print First 10 Even Numbers

count = 1
num = 2

while count <= 10:
    print(num)
    num += 2
    count += 1

5. #Calculate Factorial

def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

number = int(input("Enter a positive integer: "))
print("Factorial of", number, "is", factorial(number))

6. #Remove Negative Numbers

numbers = [10, -3, 7, -1, 0, 5, -6]
positive_numbers = []

for num in numbers:
    if num >= 0:
        positive_numbers.append(num)

print(positive_numbers)

7. #Sum of Numbers

def sum_of_array(numbers):
    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    return total

numbers = [4, 7, 2, 9, 6]
print("Sum of the array:", sum_of_array(numbers))


8. #Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius_temps):
    fahrenheit_temps = []
    i = 0
    while i < len(celsius_temps):
        fahrenheit = (celsius_temps[i] * 9/5) + 32
        fahrenheit_temps.append(fahrenheit)
        i += 1
    return fahrenheit_temps

celsius_temps = []

n = int(input("How many temperatures do you want to convert? "))

i = 0
while i < n:
    temp = float(input(f"Enter temperature {i+1} in Celsius: "))
    celsius_temps.append(temp)
    i += 1

fahrenheit_temps = celsius_to_fahrenheit(celsius_temps)
print("Temperatures in Fahrenheit:", fahrenheit_temps)

9. #Remove Odd Numbers

def remove_odd_numbers(numbers):
    even_numbers = []
    i = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0: 
            even_numbers.append(numbers[i])
        i += 1
    return even_numbers

numbers = [10, 15, 22, 33, 40, 55, 60]
filtered_numbers = remove_odd_numbers(numbers)
print("Array after removing odd numbers:", filtered_numbers)

    
    
    
    
