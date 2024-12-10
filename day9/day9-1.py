
def read_map(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        return list(file.read().strip())

def transform_to_blocks(disk_map: list[str]) -> list[str]:
    blocks = []
    id = 0
    for index, element in enumerate(disk_map):
        count = int(element)
        if index % 2 == 0:
            blocks.extend([id] * count)
            id +=1
        else:
            blocks.extend(['.'] * count)
    return blocks

def compact(blocks: list[str]) -> list[str]:
    for index in range(len(blocks) - 1, 0, -1):
        element = blocks[index]

        if (element == "."):
            continue

        free_call_idx = blocks.index(".")

        if free_call_idx > index:
            print("List has been compacted")
            break

        blocks[free_call_idx] = element
        blocks[index] = '.'

    return blocks

def calc_check_sum(blocks: list[str]) -> int:
    return sum (
        index * int(element)
        for index, element in enumerate(blocks)
        if element != "."
    )

def main():
    disk_map = read_map("day9/input-test.txt")
    blocks = transform_to_blocks(disk_map)
    compacted = compact(blocks)
    check_sum = calc_check_sum(compacted)
    print(check_sum) # Correct answer is 6225730762521

if __name__ == "__main__":
    main()
