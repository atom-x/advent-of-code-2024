
operators = ["+", "*", "||"]

# Read calibrations from file
def read_calibrations():
    with open('day7/input-test.txt', 'r') as f:
        lines = f.readlines()

    calibrations = []

    for line in lines:
        value, numbers_str = line.split(":")
        value = int(value.strip())
        numbers = list(map(int, numbers_str.strip().split()))
        calibrations.append([value, numbers])

    return calibrations

# Generate all possible combinations of operators
def generate_combinations(values, length, current_combination=None, combinations=None):
    if combinations is None:
        combinations = []
    if current_combination is None:
        current_combination = []

    if length == 0:
        combinations.append(current_combination[:])
        return combinations

    for value in values:
        current_combination.append(value)
        generate_combinations(values, length - 1, current_combination, combinations)
        current_combination.pop()

    return combinations

# Calculate sum based on the combination of operators
def calculate_sum(numbers, combination):
    sum = 0

    for i, operator in enumerate(combination):
        if sum == 0:
            sum = numbers[0]
        if operator == "+":
            sum = sum + numbers[i + 1]
        if operator == "*":
            sum = sum * numbers[i + 1]
        if operator == "||":
            sum = int(f"{sum}{numbers[i + 1]}")

    return sum

def main():
    total_sum = 0
    calibrations = read_calibrations()
    for test_value, numbers in calibrations:
        combinations = generate_combinations(operators, len(numbers) - 1)
        if any(test_value == calculate_sum(numbers, combination) for combination in combinations):
            total_sum += test_value

    print(f"Total sum: {total_sum}") # Correct answer:945341732469724

if __name__ == "__main__":
    main()
