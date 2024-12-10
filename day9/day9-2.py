
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

def find_first_occurrence(lst: list, length: int) -> int:
    sequence = ['.'] * length
    seq_len = len(sequence)
    for i in range(len(lst) - seq_len + 1):
        if lst[i:i + seq_len] == sequence:
            return i
    return -1


def compact_by_fyle(blocks: list[str]) -> list[str]:
    sequence = []
    for index in range(len(blocks) - 1, 0, -1):
        element = blocks[index]

        if element == ".":
            continue

        if element in sequence or len(sequence) == 0:
            sequence.append(element)

        if index != 0 and blocks[index - 1] != element:
            length = len(sequence)
            idx = find_first_occurrence(blocks, length)
            if idx < index and idx != -1:
                blocks[idx:idx + length] = sequence
                blocks[index:index + length] = ['.'] * length
            sequence = []
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
    # print(blocks)
    compacted = compact_by_fyle(blocks)
    # print(compacted)
    check_sum = calc_check_sum(compacted)
    print(check_sum) # Correct answer is 6250605700557

if __name__ == "__main__":
    main()
