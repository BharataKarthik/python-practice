def upper_to_lower():
    while True:
        try:
            user_input = input("Enter a string in uppercase: ")

            if not user_input.isalpha():  # Check if the input contains only letters
                print("Please enter a valid string with letters only.")
                continue

            if user_input.islower():
                print("The string is already in lowercase.")
            else:
                lower_case_string = user_input.lower()
                print(f"The lowercase version is: {lower_case_string}")
            break  # Exit the loop after successful conversion

        except Exception as e:
            print(f"An error occurred: {e}")

upper_to_lower()
