def ascii_value():
    while True:
        char = input("Enter the character: ")
        
        if len(char) !=1:
            print("Please enter single character")
            continue

        ascii_val = ord(char)
        print(f"The Ascii value of {char} is {ascii_val}")
        break
        
ascii_value()
