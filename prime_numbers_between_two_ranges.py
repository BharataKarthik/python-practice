# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Only check up to sqrt(num)
        if num % i == 0:
            return False
    return True

# Function to print prime numbers between two ranges
def prime_in_range(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")
    print()  # To add a new line after printing all primes

# Taking input from the user for range
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

# Calling the function
prime_in_range(start, end)
