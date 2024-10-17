def x_to_power_y():
    while True:
        try:
          num1 = int(input("Enter the number(x): "))
          num2 = int(input("Enter the number(y): "))
          power = num1 ** num2
          print(f"{num1} to the power of {num2} is {power}")

          another = input("Do you want to continue? (y/n): ").lower()
          if another != "y":
              print("Thank You")
              break
        except ValueError:
            print("Enter valid numbers only")

x_to_power_y()
