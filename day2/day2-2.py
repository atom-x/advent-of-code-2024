#!/usr/bin/env python3

safe_count: int = 0

def check_line(line: str) -> bool:
    numbers = [int(t) for t in line.split()]
    if check_numbers(numbers):
        return True
    for index in range(len(numbers)):
        new_list = numbers[:index] + numbers[index+1:]
        if check_numbers(new_list):
            return True
    return False

def check_numbers(numbers: list[int]) -> bool:
    sign = 0
    for index in range(1, len(numbers)):
        diff = numbers[index] - numbers[index - 1]
        if (diff > 0 and sign == -1) or (diff < 0 and sign == 1) or not (1 <= abs(diff) <= 3):
            return False
        sign = (diff > 0) - (diff < 0)
    return True

with open('./input.txt', 'r') as file:
    lines = file.readlines()

safe_count = sum(1 for line in lines if check_line(line))

print(safe_count)
