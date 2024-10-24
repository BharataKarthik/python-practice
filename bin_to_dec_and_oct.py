# Function to convert binary to decimal and octal
def bin_to_dec_and_oct():
    try:
        # Taking binary input from the user
        binary = input("Enter a binary number: ")

        # Convert binary to decimal using int() with base 2
        decimal = int(binary, 2)

        # Convert decimal to octal using oct()
        octal = oct(decimal)

        print(f"The decimal equivalent of {binary} is {decimal}")
        print(f"The octal equivalent of {binary} is {octal[2:]}")
    
    except ValueError:
        print("Invalid binary number. Please enter a valid binary number.")

# Calling the function
bin_to_dec_and_oct()
