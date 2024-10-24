def reverse_number():
    try:
        num = int(input("Enter an integer: "))
        negative = False

        if num < 0:
            negative = True  # If the number is negative, set a flag
            num = abs(num)  # Work with the absolute value of the number

        reversed_num = 0

        while num > 0:
            remainder = num % 10  # Get the last digit of the number
            reversed_num = (reversed_num * 10) + remainder  # Shift digits and add the last digit
            num //= 10  # Remove the last digit

        if negative:
            reversed_num = -reversed_num  # Restore the negative sign if the input was negative

        print(f"Reversed number: {reversed_num}")

    except ValueError:
        print("Please enter a valid integer")

reverse_number()
