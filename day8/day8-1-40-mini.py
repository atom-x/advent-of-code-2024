def read_input(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def find_antennas(grid):
    antennas = {}
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            char = grid[row][col]
            if char not in '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((row, col))
    return antennas

def calculate_antinode_positions(antenna1, antenna2):
    row1, col1 = antenna1
    row2, col2 = antenna2
    mid_row = (row1 + row2) // 2
    mid_col = (col1 + col2) // 2
    # Distance between the antennas
    distance = abs(row1 - row2)
    # Calculate the positions of the antinodes
    if distance % 2 == 0:
        # Check for valid antinodes
        antinode1 = (mid_row - distance // 2, mid_col)
        antinode2 = (mid_row + distance // 2, mid_col)
        return [antinode1, antinode2]
    return []

def calculate_impact_of_signal(grid):
    antennas = find_antennas(grid)
    antinode_positions = set()

    # Check all pairs of antennas with the same frequency
    for freq, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                antenna1 = positions[i]
                antenna2 = positions[j]
                antinodes = calculate_antinode_positions(antenna1, antenna2)
                for antinode in antinodes:
                    row, col = antinode
                    # Ensure antinode is within bounds
                    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                        antinode_positions.add((row, col))

    return len(antinode_positions)

# Main execution
if __name__ == "__main__":
    grid = read_input('day8/input.txt')
    impact = calculate_impact_of_signal(grid)
    print(f"Impact of the signal: {impact}")
