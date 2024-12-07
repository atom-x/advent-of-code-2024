#!/usr/bin/env python3


lines: list[str] = []
first_list: list[int] = []
second_list: list[int] = []
distance: int = 0

with open('./input.txt', 'r') as file:
    lines = file.readlines()

first_list = [int(line.split('  ')[0]) for line in lines]
second_list = [int(line.split('  ')[1]) for line in lines]

first_list.sort()
second_list.sort()

for f, s in zip(first_list, second_list):
    distance += abs(f-s)

# distance = sum(abs(f - s) for f, s in zip(first_list, second_list))

print(distance)

# correct answer: 1830467
