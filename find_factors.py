# Function to find and print factors of a number
def find_factors(num):
    print(f"Factors of {num}:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print()  # To add a new line after printing all factors

# Taking input from the user
number = int(input("Enter a number: "))

# Calling the function
find_factors(number)
