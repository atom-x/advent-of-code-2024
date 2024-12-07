def count_word_occurrences(matrix, word):
    def search_direction(x, y, dx, dy):
        """Search for the word starting from (x, y) in the direction (dx, dy)."""
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            # Check boundaries
            if nx < 0 or ny < 0 or nx >= len(matrix) or ny >= len(matrix[0]):
                return False
            if matrix[nx][ny] != word[i]:
                return False
        return True

    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    count = 0

    # Iterate through the matrix
    for x in range(rows):
        for y in range(cols):
            # Check all 8 directions
            for dx, dy in directions:
                if search_direction(x, y, dx, dy):
                    count += 1

    return count

with open("./input.txt", "r") as file:
    matrix = file.readlines()

# Convert matrix into list of lists for easier indexing
matrix = [list(row) for row in matrix]

# Count occurrences of the word
word = "XMAS"
occurrences = count_word_occurrences(matrix, word)
print(f"The word '{word}' occurs {occurrences} times.")
