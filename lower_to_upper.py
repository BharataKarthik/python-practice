def lower_to_upper():
    while True:
        try:
            string = input("Enter a string (lowercase or mixed case): ")

            if not string.isalpha():
                print("Please enter a valid string (letters only)")
                continue

            if string.isupper():
                print("The string is already in uppercase")
                break
            else:
                lower_upper = string.upper()
                print(f"The string in uppercase is: {lower_upper}")
                break
        except Exception as e:
            print(f"An error occurred: {e}")

lower_to_upper()
