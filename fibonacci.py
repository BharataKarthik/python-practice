def fibonacci():
    while True:
        try:
            num_terms = int(input("Enter the number of terms: "))

            if num_terms <= 0:
                print("Please enter a positive number")
                continue

            fib_sequence = []
            a, b = 0, 1
            for _ in range(num_terms):
                fib_sequence.append(a)
                a, b = b, a + b

            print(f"The Fibonacci series of {num_terms} terms is: {fib_sequence}")
            break  # Break the loop after successful calculation

        except ValueError:
            print("Please enter a valid positive number")

fibonacci()
