def leap_year():
    year = int(input("Please enter the year: "))

    if (year % 400==0):
        print(f"{year} is a Leap Year")

    elif (year %100 ==0):
        print(f"{year} is not a Leap year")

    elif (year % 4 ==0):
        print(f"{year} is a Leap year")

    else:
        print(f"{year} is not a Leap year")

leap_year()
