def celsius_to_fahrenheit():
    while True:
        try:
            celsius = float(input("Enter degrees in celsius: "))
            fahrenheit = (celsius * 9/5)+32
            print(f" The {celsius}°C is equal to {fahrenheit}°F")

            another = input(print("Do you want to convert another temperature? (y/n)"))
            if another !="y":
                print("Thank you")
                break
        except ValueError:
            print("Enter the valid number")

celsius_to_fahrenheit()
