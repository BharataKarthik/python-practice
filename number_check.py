def number():
    number= int(input("Please enter the number: "))

    if number <0:
        print(f"{number} is negative")

    elif number ==0:
        print(f"{number} is zero")

    else:
        print(f"{number} is positive")

number()
