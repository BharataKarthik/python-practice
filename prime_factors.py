# Function to find and print prime factors of a number
def find_prime_factors(num):
    print(f"Prime factors of {num}:")
    
    # Divide by 2 until num becomes odd
    while num % 2 == 0:
        print(2, end=" ")
        num = num // 2
    
    # Now num must be odd, so we can check only odd numbers
    for i in range(3, int(num**0.5) + 1, 2):
        while num % i == 0:
            print(i, end=" ")
            num = num // i
    
    # If num is still greater than 2, then it's a prime number
    if num > 2:
        print(num)

# Taking input from the user
number = int(input("Enter a number: "))

# Calling the function
find_prime_factors(number)
