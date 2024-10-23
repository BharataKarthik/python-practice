def generate_pascals_triangle(n):
    triangle = []  # Initialize an empty list to store rows

    for i in range(n):
        # Start each row with a 1
        row = [1] * (i + 1)  # Each row has 'i+1' elements
        # Calculate the values inside the row (excluding the first and last elements)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        # Add the row to the triangle
        triangle.append(row)

    return triangle

# Input: number of rows
n = int(input("Enter the number of rows: "))
pascals_triangle = generate_pascals_triangle(n)

# Print Pascal's Triangle
for row in pascals_triangle:
    print(row)
