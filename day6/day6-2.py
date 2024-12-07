import copy

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


def is_stuck_in_loop(office_map):
    left_office: bool = False
    in_loop: bool = False
    guard_position = find_guard_position(office_map, "^")

    if (guard_position is None):
        print("Guard not found")
        return False
    i, j = guard_position
    visited_positions = {}

    while not (left_office or in_loop):
        current_direction = office_map[i][j]
        di, dj, next_direction = directions[current_direction]

        ni = i + di
        nj = j + dj

        pos_dir_tuple = (i, j, current_direction)
        if pos_dir_tuple in visited_positions:
            visited_positions[pos_dir_tuple] += 1
            if visited_positions[pos_dir_tuple] >= 5:
                in_loop = True
                break
        else:
            visited_positions[pos_dir_tuple] = 1

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
    return in_loop

def simulate_guard(office_map, guard_position):
    i, j = guard_position
    visited_positions = {}
    left_office = False

    while not left_office:
        current_direction = office_map[i][j]
        di, dj, next_direction = directions[current_direction]

        ni, nj = i + di, j + dj

        office_map[i][j] = "X"

        if is_out_of_bounds(ni, nj, office_map):
            left_office = True
            break

        pos_dir_tuple = (i, j, current_direction)
        if pos_dir_tuple in visited_positions:
            visited_positions[pos_dir_tuple] += 1
            if visited_positions[pos_dir_tuple] >= 3:
                return True  # Loop detected
        else:
            visited_positions[pos_dir_tuple] = 1

        if office_map[ni][nj] == "#":
            i, j = i + directions[next_direction][0], j + directions[next_direction][1]
            office_map[i][j] = next_direction
        else:
            i, j = ni, nj
            office_map[i][j] = current_direction

    return False  # No loop detected

def count_loop_variations(office_map):
    loop_count = 0
    original_map = [row[:] for row in office_map]  # Make a copy of the original map

    for i in range(len(office_map)):
        for j in range(len(office_map[i])):
            if office_map[i][j] == ".":
                office_map[i][j] = "#"
                guard_position = find_guard_position(office_map, "^")
                if guard_position and simulate_guard([row[:] for row in office_map], guard_position):
                    loop_count += 1
                office_map[i][j] = "."  # Reset the position

    return loop_count


def main():

    with open("day6/input.txt") as f:
        groups = f.read().splitlines()
    office_map = [list(group) for group in groups]

    # total_loops = 0

    # for i in range(len(office_map)):
    #     for j in range(len(office_map[i])):
    #         if office_map[i][j] == "^":
    #             continue
    #         new_map = list(map(lambda x: x[:], office_map))
    #         new_map[i][j] = "#"
    #         total_loops += 1 if is_stuck_in_loop(new_map) else 0

    # print(f"Total loops: {total_loops}") # Correct answer:

    guard_position = find_guard_position(office_map, "^")

    if guard_position is None:
        print("Guard not found")
        return

    loop_variations = count_loop_variations(office_map)
    print(f"Number of map variations that lead to a loop: {loop_variations}")

if __name__ == "__main__":
    main()
