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
def check_update(update: list[int], rules: dict[int, list[int]]) -> bool:
    # return all(update[i+1] in rules[update[i]] for i in range(len(update) - 1))
    for i in range(len(update) - 1):
        if update[i+1] in rules[update[i]]:
            continue
        else:
            return False
    return True

def main():
    rules = read_rules()
    updates = read_updates()

    total_sum = 0
    for update in updates:
        if check_update(update, rules):
            # sum of middle elements
            total_sum += update[(len(update) // 2)]

    print(total_sum) # correct answer: 5651

if __name__ == "__main__":
    main()
