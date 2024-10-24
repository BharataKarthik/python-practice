def is_armstrong():
    try:
        num = int(input("Enter an integer: "))
        total_sum = 0
        temp = num
        num_digits = len(str(num))  # Count the number of digits

        while temp > 0:
            digit = temp % 10  # Get the last digit
            total_sum += digit ** num_digits  # Raise the digit to the power of num_digits and add to total_sum
            temp //= 10  # Remove the last digit

        if total_sum == num:
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is not an Armstrong number.")
    
    except ValueError:
        print("Please enter a valid integer.")

is_armstrong()
