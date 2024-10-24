def is_palindrome():
    try:
        num = int(input("Enter an integer: "))
        original_num = num  # Store the original number to compare later

        reversed_num = 0
        while num > 0:
            remainder = num % 10  # Get the last digit
            reversed_num = (reversed_num * 10) + remainder  # Shift digits and add the last digit
            num //= 10  # Remove the last digit

        if original_num == reversed_num:
            print(f"{original_num} is a palindrome.")
        else:
            print(f"{original_num} is not a palindrome.")
            
    except ValueError:
        print("Please enter a valid integer.")

is_palindrome()
