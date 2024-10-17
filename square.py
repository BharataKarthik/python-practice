def square():
    while True:
        try:
          num = int(input("Enter the number: "))
          square= num**2
          print(f"Square of {num} is {square}")
          break
        except ValueError:
            print("Enter valid numbers only")

square()
