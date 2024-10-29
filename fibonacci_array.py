def fibonacci_array(n):
    if n <= 0:
        return "Please enter a positive integer."
    
    # Initialize the array to store Fibonacci sequence
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to n terms
    for i in range(2, n):
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_term)
    
    return fib_sequence

# Input number of terms
num_terms = int(input("Enter the number of terms: "))
result = fibonacci_array(num_terms)
print(f"The Fibonacci sequence with {num_terms} terms is: {result}")
