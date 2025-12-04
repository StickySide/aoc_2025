# Advent of code Day 3 Part 1


def get_input(filename: str) -> list[str]:
    input: list[str] = []
    with open(filename, "r") as input_file:
        for line in input_file:
            input.append(line.strip())
    return input


def get_two_biggest(battery_bank: str) -> tuple[int, int]:
    bank_list: list[int] = [int(battery) for battery in battery_bank]
    first: int = 0
    second: int = 0

    first = max(bank_list)

    if bank_list.index(first) == len(bank_list) - 1:  # Edge case, highest battery is the last one
        second = first  # Second battery has to be the last
        first = max(bank_list[:-1])  # First battery is the largest aside from the last
    else:
        second = max(bank_list[bank_list.index(first) + 1 :])  # Second battery is the largest after the first

    return first, second


def combine_digits(digits: tuple[int, int]) -> int:
    combined_string: str = str(digits[0]) + str(digits[1])
    return int(combined_string)


def get_total_joltage(input: list[str]) -> int:
    total_joltage: int = 0
    for line in input:
        print(f"--- Line: {line}")
        two_biggest: tuple[int, int] = get_two_biggest(line)
        print(f"    Two biggest batteries: {two_biggest}")
        largest_joltage: int = combine_digits(two_biggest)
        print(f"    Combined: {largest_joltage}")
        total_joltage += largest_joltage
    print(f"Total joltage: {total_joltage}")
    return total_joltage


if __name__ == "__main__":
    input = get_input("input.txt")
    get_total_joltage(input)
