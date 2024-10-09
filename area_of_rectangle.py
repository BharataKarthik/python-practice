def area_of_rectangle():
     while True:
        try:
            length = float(input("Enter the length: "))
            breadth = float(input("Enter the breadth: "))

            if length < 0 or breadth <0:
                print("Inputs cannot be in negative")
                continue

            area= length*breadth
            print(f"The area of the rectangle is {area} square units")
            return area
        except ValueError:
            print("Please enter numeric values only")

area_of_rectangle()
