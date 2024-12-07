import re

#!/usr/bin/env python3

text: str = ""
with open ("./input.txt", "r") as file:
    text = file.read()

print(text)

pat = re.compile("^mul\\(\\d{1,3},\\d{1,3}\\)$")
print(pat.match(text))

list = re.findall("mul\\(\\d{1,3},\\d{1,3}\\)", text)

sum: int = 0

for item in list:

    numbers = item[4:-1].split(",")
    sum += int(numbers[0]) * int(numbers[1])

print(sum)
# correct answer: 184122457
