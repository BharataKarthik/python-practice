def find_largest(arr):
    if len(arr) == 0:
        return "The array is empty. Please provide a valid list of numbers."
    
    # Initialize the largest number with the first element of the array
    largest = arr[0]
    
    # Iterate through the array to find the largest element
    for num in arr:
        if num > largest:
            largest = num
    
    return largest

# Input: list of numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
result = find_largest(numbers)
print(f"The largest number in the array is: {result}")
