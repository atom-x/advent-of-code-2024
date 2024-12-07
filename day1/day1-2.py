#!/usr/bin/env python3

first_list = []
second_list = []
similarity_score = 0

with open('./input.txt', 'r') as file:
    for line in file:
        numbers = line.split()
        first_list.append(int(numbers[0]))
        second_list.append(int(numbers[1]))

similarity_score = sum((first_list[i]*second_list.count(first_list[i]))
    for i in range(len(first_list)))

print(similarity_score)

# correct answer: 26674158
