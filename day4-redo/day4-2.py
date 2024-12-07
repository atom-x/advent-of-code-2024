def count_mas_x_patterns(matrix):
    def is_valid_mas_x(x, y):
        """Check if the 'X' pattern with 'MAS' exists at the center (x, y)."""
        # Validate boundaries to ensure the 'X' fits
        if x - 1 < 0 or x + 1 >= len(matrix) or y - 1 < 0 or y + 1 >= len(matrix[0]):
            return False

        # Top-left to bottom-right diagonal
        tl_br = [matrix[x - 1][y - 1], matrix[x][y], matrix[x + 1][y + 1]]
        # Top-right to bottom-left diagonal
        tr_bl = [matrix[x - 1][y + 1], matrix[x][y], matrix[x + 1][y - 1]]

        # Check both diagonals for 'MAS' or 'SAM'
        mas = ['M', 'A', 'S']
        sam = ['S', 'A', 'M']
        return (tl_br == mas or tl_br == sam) and (tr_bl == mas or tr_bl == sam)

    rows, cols = len(matrix), len(matrix[0])
    count = 0

    # Iterate through the matrix
    for x in range(rows):
        for y in range(cols):
            if is_valid_mas_x(x, y):
                count += 1

    return count

with open("./input.txt", "r") as file:
    matrix = file.readlines()

# Convert matrix into list of lists for easier indexing
matrix = [list(row) for row in matrix]

# Count 'MAS X' patterns
mas_x_count = count_mas_x_patterns(matrix)
print(f"The number of 'MAS' X patterns is: {mas_x_count}")
