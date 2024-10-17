def multiplication_table():
    try:
        num = int(input("Enter the number: "))
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print("Please enter a valid number.")

multiplication_table()
