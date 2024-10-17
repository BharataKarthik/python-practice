def natural_num():
    while True:
        try:
            num = int(input("Enter a positive number:"))

            if num < 1:
                print("Please enter a positive number")
                continue

            total_sum = 0
            for i in range(1, num + 1):
                total_sum += i  # Sum up all numbers from 1 to num

            print(f"The sum of natural numbers up to {num} is {total_sum}")  # Print after loop finishes
            break  # Exit loop after correct input
        except ValueError:
            print("Enter valid numbers only")
            
natural_num()
