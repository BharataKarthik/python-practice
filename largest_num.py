def largest_number():
    num1= int(input("Please enter first number: "))
    num2= int(input("please enter second number: "))
    num3= int(input("please enter third number: "))

    largest = num1

    if num2 > largest:
        largest= num2

    if num3> largest:
        largest=num3

    print(f"The largest number among {num1}, {num2}, {num3} is {largest}")

largest_number()
