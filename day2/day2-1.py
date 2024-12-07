#!/usr/bin/env python3

lines: list[str] = []
numbers: list[int] = []
safe_count: int = 0

with open('./input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    text = line.split(' ')
    numbers = [int(t) for t in text]
    print(numbers)

    sign = 0
    for index in range(1, len(numbers)):
        diff = numbers[index] - numbers[index - 1]

        if (diff > 0 and sign == -1) or (diff < 0 and sign == 1) or not (1 <= abs(diff) <= 3):
            break

        sign = (diff > 0) - (diff < 0)

        if index == len(numbers) - 1:
            safe_count += 1
            print("this line is safe")

print(safe_count)
