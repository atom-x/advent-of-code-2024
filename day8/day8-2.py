
secondary_anti_nodes = set()

def load_map():
    with open("day8/input.txt") as f:
        lines = f.readlines()
    return [list(line.strip()) for line in lines]

def find_antenas_type(map) -> set[str]:
    return {element for line in map for element in line if element != "."}

def calc_antinodes(antena_type, i, j, m, n, map, antenas_types):
    print(f"Calculating antinodes for: {i}, {j} and {m}, {n}")

    dx = (i - m)
    dy = (j - n)

    nx1 = i + dx
    ny1 = j + dy

    if (nx1 < 0 or ny1 < 0 or nx1 > len(map)-1 or ny1 > len(map[0])-1):
        print(f"Antinode out of bounds: {nx1}, {ny1}")
    else:
        print(f"Antinode found at: {nx1}, {ny1}")

        if (map[nx1][ny1] == "."):
            map[nx1][ny1] = "#"

        if map[nx1][ny1] in antenas_types and map[nx1][ny1] != antena_type:
            print(f"Antinode found at place of another antena: {nx1}, {ny1}")
            secondary_anti_nodes.add((nx1, ny1))

    nx2 = m - dx
    ny2 = n - dy

    if (nx2 < 0 or ny2 < 0 or nx2 > len(map)-1 or ny2 > len(map[0])-1):
        print(f"Antinode out of bounds: {nx2}, {ny2}")
    else:
        print(f"Antinode found at: {nx2}, {ny2}")

        if (map[nx2][ny2] == "."):
            map[nx2][ny2] = "#"

        if map[nx2][ny2] in antenas_types and map[nx2][ny2] != antena_type:
            print(f"Antinode found at place of another antena: {nx2}, {ny2}")



def find_antinodes(i, j, antena_type, map, antenas_types):
    print(f"Finding antinodes for: {i}, {j}")
    for m, line in enumerate(map):
        for n, element in enumerate(line):
            if (m == i and n == j) or element == ".":
                continue
            if element == antena_type:
                print(f"Paired antena found at: {m}, {n}")
                calc_antinodes(antena_type, i, j, m, n, map, antenas_types)



def main():
    map = load_map()
    antenas_types = find_antenas_type(map)
    for antena_type in antenas_types:
        print(f"Antena type: {antena_type}")

        for i, line in enumerate(map):
            for j, element in enumerate(line):
                if element == antena_type:
                    print(f"Antena found at: {i}, {j}")

                    find_antinodes(i, j, antena_type, map, antenas_types)


    print(map)

    print(sum (element == "#" for line in map for element in line))
    print(len(secondary_anti_nodes))
    print(sum (element == "#" for line in map for element in line) + len(secondary_anti_nodes))


if __name__ == "__main__":
    main()
