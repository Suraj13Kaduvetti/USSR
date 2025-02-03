def create_matrix(rows, cols):
    """Create a binary matrix based on user input."""
    matrix = []
    print(f"Enter the values for a {rows}x{cols} binary matrix (0s and 1s):")
    for i in range(rows):
        while True:
            row = input(f"Row {i + 1}: ").strip().split()
            if len(row) == cols and all(val in ['0', '1'] for val in row):
                matrix.append([int(val) for val in row])
                break
            else:
                print("Invalid input. Please enter exactly 0s and 1s.")
    return matrix

def calculate_hash_functions(num_hash_functions, params, rows):
    """Calculate hash function values based on given parameters."""
    hash_values = []
    for x in range(num_hash_functions):
        y, n = params[x]
        hash_value = ((y * x) + n) % rows  # Ensure hash values are within the range of rows
        hash_values.append(hash_value)
        print(f"Hash function value for index {x} (y={y}, n={n}): {hash_value}")
    return hash_values

def main():
    # Step 1: Get dimensions of the binary matrix
    rows = int(input("Enter the number of rows for the binary matrix: "))
    cols = int(input("\nEnter the number of columns for the binary matrix: "))

    # Step 2: Create the binary matrix
    binary_matrix = create_matrix(rows, cols)

    # Step 3: Get number of hash functions
    num_hash_functions = int(input("Enter the number of hash functions: "))

    # Step 4: Get parameters (y, n) for each hash function
    params = []
    for i in range(num_hash_functions):
        y = int(input(f"Enter value for y for hash function {i + 1}: "))
        n = int(input(f"Enter value for n for hash function {i + 1}: "))
        params.append((y, n))

    m = int(input("Enter value for m (number of columns in new matrix): "))

    # Step 5: Create a new matrix with num_hash_functions rows and m columns
    new_matrix = [[0] * m for _ in range(num_hash_functions)]

    # Step 6: Calculate and display hash function values
    print("\nCalculating hash function values:")
    hash_values = calculate_hash_functions(num_hash_functions, params, rows)

    # Step 7: Populate new_matrix with original binary_matrix values based on hash values
    print("\nPopulating new matrix based on calculated hash values:")
    for i in range(num_hash_functions):
        for j in range(m):
            if j < cols:  # Ensure we don't exceed column bounds
                new_matrix[i][j] = binary_matrix[hash_values[i]][j]
                print(f"new_matrix[{i}][{j}] = binary_matrix[{hash_values[i]}][{j}] -> {new_matrix[i][j]}")

    # Final output
    print("\nFinal new matrix:")
    for row in new_matrix:
        print(row)

if __name__ == "__main__":
    main()
