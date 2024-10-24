def count_digits():
    try:
        num = int(input("Enter an integer: "))

        if num < 0:
            num = abs(num)  # Taking the absolute value to handle negative numbers
        
        count = 0
        while num > 0:
            num //= 10  # Remove the last digit of the number
            count += 1

        print(f"The number of digits is {count}")

    except ValueError:
        print("Please enter a valid integer")

count_digits()
