import re

def filter_corrupted(arr) -> list[str]:
    result = []
    skip = False
    for item in arr:
        if item == "don't()":
            skip = True
        elif item == "do()":
            skip = False
        elif not skip:
            result.append(item)
    return result

def calculate_sum(arr) -> int:
    total: int = 0
    for item in arr:
        x, y = map(int, item[4:-1].split(","))
        total += x * y
    return total

def main():
    with open ("./input.txt", "r") as file:
        text = file.read()

    pattern = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"
    arr = re.findall(pattern, text)
    filtered = filter_corrupted(arr)
    print(calculate_sum(filtered))
    # correct anwer: 107862689

if __name__ == "__main__":
    main()
