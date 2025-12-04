# Advent of code Day 3 Part 2


def get_input(filename: str) -> list[str]:
    with open(filename, "r") as input_file:
        input = [line.strip() for line in input_file]
    return input


def get_twelve_biggest(battery_bank: str) -> list[str]:
    """Extract the 12 largest digits in the order they appear in the string."""
    bank: list[str] = [battery for battery in battery_bank]
    biggest: list[str] = []

    # Iteratively find largest digits, ensuring we reserve space for remaining selections
    # i counts down from 11 to 0, excluding the last i positions from consideration
    for i in range(11, -1, -1):
        biggest_battery = max(bank[:-i]) if i != 0 else max(bank)
        biggest.append(biggest_battery)
        # Update bank to everything after the selected digit
        bank = bank[bank.index(biggest_battery) + 1 :]

    return biggest


def combine_digits(digits: list[str]) -> int:
    return int("".join(digits))


def get_total_joltage(input: list[str]) -> int:
    """Calculate total joltage by finding the 12 biggest digits in each line."""
    total_joltage: int = 0
    for line in input:
        twelve_biggest: list[str] = get_twelve_biggest(line)
        largest_joltage: int = combine_digits(twelve_biggest)
        total_joltage += largest_joltage
    return total_joltage


if __name__ == "__main__":
    input = get_input("input.txt")
    print(f"Total joltage: {get_total_joltage(input)}")
