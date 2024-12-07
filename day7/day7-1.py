
operators = ['+', '*']
def generate_combinations(values, length, current_combination="", combinations=None):
    if combinations is None:
        combinations = []

    if length == 0:
        combinations.append(current_combination)
        return combinations

    for value in values:
        generate_combinations(values, length - 1, current_combination + value, combinations)

    return combinations


with open('day7/input.txt', 'r') as f:
    lines = f.readlines()

calibrations = []

for line in lines:
    # print(line)
    split = line.split(":")
    value = split[0].strip()
    numbers = [int(i) for i in split[1].strip().split(" ")]
    calibrations.append([value, numbers])

total_sum = 0

for calibration in calibrations:
    print(f"Calibration: {calibration}")
    test_value = int(calibration[0])
    numbers = calibration[1]
    combinations = generate_combinations(operators, len(numbers) - 1)
    # print(f"Combinations: {combinations}")
    for combination in combinations:
        # print(f"Combination: {combination}")
        sum = 0

        num_operators = list(combination)
        # print(f"Operators: {num_operators}")
        # print(f"Numbers: {numbers}")
        for i in range(len(num_operators)):
            if sum == 0:
                sum = numbers[0]
            operator = num_operators[i]
            if operator == "+":
                sum = sum + numbers[i + 1]
            if operator == "*":
                sum = sum * numbers[i + 1]

        # print(f"Sum: {sum}")
        if (test_value == sum):
            print(f"Found sum: {sum}")
            total_sum += sum
            break

    # print(combinations)

print(f"Total sum: {total_sum}") # Correct answer:1611660863222
