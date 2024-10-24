# Function to calculate GCD using Euclidean Algorithm
def calculate_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Function to calculate LCM
def calculate_lcm(x, y):
    return (x * y) // calculate_gcd(x, y)  # Formula for LCM

# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = calculate_gcd(num1, num2)
lcm = calculate_lcm(num1, num2)

print(f"The GCD of {num1} and {num2} is {gcd}")
print(f"The LCM of {num1} and {num2} is {lcm}")
