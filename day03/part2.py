# Advent of code Day 3 Part 1


def get_input(filename: str) -> list[str]:
    input: list[str] = []
    with open(filename, "r") as input_file:
        for line in input_file:
            input.append(line.strip())
    return input


def get_twelve_biggest(battery_bank: str) -> list[str]:
    bank: list[str] = [battery for battery in battery_bank]
    biggest: list[str] = []

    for i in range(11, -1, -1):
        biggest_battery = max(bank[:-i]) if i != 0 else max(bank)
        biggest.append(biggest_battery)
        bank = bank[bank.index(biggest_battery) + 1 :]

    return biggest


def combine_digits(digits: list[str]) -> int:
    return int("".join(digits))


def get_total_joltage(input: list[str]) -> int:
    total_joltage: int = 0
    for line in input:
        twelve_biggest: list[str] = get_twelve_biggest(line)
        largest_joltage: int = combine_digits(twelve_biggest)
        total_joltage += largest_joltage
    return total_joltage


if __name__ == "__main__":
    testinput = get_input("testinput.txt")
    assert get_total_joltage(testinput) == 3121910778619
    input = get_input("input.txt")
    print(f"Total joltage: {get_total_joltage(input)}")
