direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def load_map(file_name: str):
    with open(file_name) as f:
        lines = f.readlines()
    return [list(line.strip()) for line in lines]

def find_positions_of_zero(topo_map):
    return [
            (row_index, col_index)
            for row_index, row in enumerate(topo_map)
            for col_index, element in enumerate(row)
            if element == "0"
        ]

def find_next_positions(position, topo_map) -> list[tuple[int, int]]:
    x, y = position
    number = int(topo_map[x][y]) + 1
    max_x, max_y = len(topo_map), len(topo_map[0])

    return [
            (x + dx, y + dy)
            for dx, dy in direction
            if 0 <= x + dx < max_x and 0 <= y + dy < max_y
            and topo_map[x + dx][y + dy] != "."
            and int(topo_map[x + dx][y + dy]) == number
        ]

def calc_score(position, topo_map) -> set[tuple[int, int]]:
    if topo_map[position[0]][position[1]] == "9":
        return {position}

    positions = find_next_positions(position, topo_map)

    score_set = set()
    for pos in positions:
        score_set.update(calc_score(pos, topo_map))
    return score_set

def main():
    topo_map = load_map("day10/input.txt")
    positions_of_zero = find_positions_of_zero(topo_map)
    total_score = sum(len(calc_score(position, topo_map)) for position in positions_of_zero)
    print(total_score) # Correct answer is 557

if __name__ == "__main__":
    main()
