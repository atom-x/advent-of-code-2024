import re

#!/usr/bin/env python3

text: str = ""
with open ("./input.txt", "r") as file:
    text = file.read()

arr = re.findall("mul\\(\\d{1,3},\\d{1,3}\\)|don\\'t\\(\\)|do\\(\\)", text)

while "don't()" in arr:
    indexDONT = arr.index("don't()")
    if "do()" not in arr:
        arr = arr[:indexDONT]
        continue

    indexDO = arr.index("do()")
    if indexDO < indexDONT:
        del arr[indexDO]
        continue
    arr = arr[:indexDONT] + arr[indexDO+1:]

print(arr)

sum: int = 0

for item in arr:
    if item == "do()":
        continue
    numbers = item[4:-1].split(",")
    sum += int(numbers[0]) * int(numbers[1])

print(sum)

# correct anwer: 107862689
