def digit_sum():
    try:
        num = int(input("Enter an integer: "))
        total_sum = 0
        temp = abs(num)  # Use abs() to handle negative numbers
        
        while temp > 0:
            digit = temp % 10  # Get the last digit
            total_sum += digit  # Add the digit to the sum
            temp //= 10  # Remove the last digit
        
        print(f"The sum of the digits of {num} is {total_sum}")
        
    except ValueError:
        print("Please enter a valid integer.")

digit_sum()
