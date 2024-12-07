#!/usr/bin/env python3

lines: list[str] = []
numbers: list[int] = []
safe_count: int = 0

def check_line(line: str) -> bool:
    numbers = [int(t) for t in line.split(' ')]
    print(numbers)
    if check_numbers(numbers):
        return True
    else:
        print("try to fix")
        for index in range(1, len(numbers)+1):
            new_list = numbers.copy()
            print(f"removing {numbers[index-1]}")
            del new_list[index-1]
            print(new_list)
            if check_numbers(new_list):
                return True
        return False

def check_numbers(numbers: list[int]) -> bool:
    sign = 0
    for index in range(1, len(numbers)):
        diff = numbers[index] - numbers[index - 1]

        if (diff > 0 and sign == -1) or (diff < 0 and sign == 1) or not (1 <= abs(diff) <= 3):
            # print("this line is not safe")
            return False

        sign = (diff > 0) - (diff < 0)

    return True

with open('./input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:

    if check_line(line):
        safe_count += 1
        print("this line is safe")

print(safe_count)
