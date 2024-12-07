
directions = {
    "^": (-1, 0, ">"),
    ">": (0, 1, "v"),
    "v": (1, 0, "<"),
    "<": (0, -1, "^")
}

def find_guard_position(office_map, guard):
    for i in range(len(office_map)):
        for j in range(len(office_map[i])):
            if office_map[i][j] == guard:
                return i, j
    return None

def is_wall(i, j, office_map):
    return office_map[i][j] == "#"

def is_out_of_bounds(i, j, office_map):
    return i < 0 or i >= len(office_map) or j < 0 or j >= len(office_map[i])

def main():

    # Define direction movements and their respective next states
    directions = {
        "^": (-1, 0, ">"),
        ">": (0, 1, "v"),
        "v": (1, 0, "<"),
        "<": (0, -1, "^")
    }

    total_sum = 0

    with open("day6/input.txt") as f:
        groups = f.read().splitlines()
    office_map = [list(group) for group in groups]

    guard_position = find_guard_position(office_map, "^")


    if (guard_position is None):
        print("Guard not found")
        return

    left_office: bool = False
    i, j = guard_position
    while not left_office:
        current_direction = office_map[i][j]
        di, dj, next_direction = directions[current_direction]

        ni = i + di
        nj = j + dj

        office_map[i][j] = "X"

        if is_out_of_bounds(ni, nj, office_map):
            left_office = True
            break

        if is_wall(ni, nj, office_map):
            i += directions[next_direction][0]
            j += directions[next_direction][1]
            office_map[i][j] = next_direction
        else:
            i = ni
            j = nj
            office_map[i][j] = current_direction


    total_sum = sum(row.count('X') for row in office_map)
    print(f"Guard visited {total_sum} positions") # Correct answer: 4982

if __name__ == "__main__":
    main()
