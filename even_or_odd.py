def even_or_odd():
    number= int(input("Enter the number: "))

    if number % 2==0:
        return print(f"{number} is even")
    else:
        return print(f"{number} is odd")

even_or_odd()
