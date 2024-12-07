from collections import defaultdict

# Read rules from the file and return them as a dictionary
def read_rules() -> dict[int, list[int]]:
    with open("day5/rules.txt") as f:
        rules_raw = f.read().splitlines()

    rules = defaultdict(list)

    for rule in rules_raw:
        index, value = map(int, rule.split("|"))
        rules[index].append(value)

    return rules

# Read updates from the file and return them as a list of lists
def read_updates() -> list[list[int]]:
    with open("day5/updates.txt") as f:
        updates = [[int(i) for i in update_raw.split(",")] for update_raw in f.read().splitlines()]

    return updates

# Check if the update is valid according to the rules
def valid_update(update: list[int], rules: dict[int, list[int]]) -> bool:
    # return all(update[i+1] in rules[update[i]] for i in range(len(update) - 1))
    for i in range(len(update) - 1):
        if update[i+1] in rules[update[i]]:
            continue
        else:
            return False
    return True

# Fix the update by swapping the elements that are not in the rules
def fix_update(invalid_update: list[int], rules: dict[int, list[int]]) -> list[int]:
    fixed = invalid_update.copy()
    i = 0
    while i < len(fixed) - 1:
        if fixed[i] != fixed[i + 1] and fixed[i + 1] not in rules[fixed[i]]:
            fixed[i], fixed[i + 1] = fixed[i + 1], fixed[i]
            i = max(i - 1, 0)  # Step back to recheck the previous pair
        else:
            i += 1
    return fixed

# Recursive version of the fix_update function. My initial verions.
def fix_update_rec(invalid_update: list[int], rules: dict[int, list[int]]) -> list[int]:
    fixed = invalid_update.copy()
    for i in range(len(invalid_update) - 1):
        if (invalid_update[i] == invalid_update[i+1] or invalid_update[i+1] in rules[invalid_update[i]]):
            continue
        else:
            fixed[i+1] = invalid_update[i]
            fixed[i] = invalid_update[i+1]
            fixed = fix_update(fixed, rules)
            break
    return fixed

def main():
    rules = read_rules()
    updates = read_updates()

    total_sum = 0

    for update in updates:
        if not valid_update(update, rules):
            fixed = fix_update(update, rules)
            total_sum += fixed[len(fixed) // 2]

    print(total_sum)  # correct answer: 4743

if __name__ == "__main__":
    main()
