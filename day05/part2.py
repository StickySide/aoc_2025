# Advent of Code Day 5 Part 2


def get_input(filename: str) -> list[str]:
    """Read input file and return list of lines."""
    with open(filename, "r") as input_file:
        return [line.strip() for line in input_file]


def split_range_and_ingredients(data: list[str]) -> tuple[list[str], list[str]]:
    """Split input into ranges and ingredient IDs, separated by blank line."""
    split_point: int = data.index("")
    return data[:split_point], data[split_point + 1 :]


def build_ranges(data: list[str]) -> list[tuple[int, int]]:
    """Parse range strings (e.g., '1-5') into tuples of (lower, upper) bounds."""
    ranges: list[tuple[int, int]] = []

    for string in data:
        lower, upper = string.split("-")
        ranges.append((int(lower), int(upper)))

    return ranges


def get_amount_fresh_ids(data: list[str]) -> int:
    ranges, _ = split_range_and_ingredients(data)
    ranges = build_ranges(ranges)

    fresh_ids: set[int] = set()

    for lower, upper in ranges:
        for number in range(int(lower), int(upper) + 1):
            fresh_ids.add(number)

    return len(fresh_ids)


if __name__ == "__main__":
    testinput = get_input("testinput.txt")
    test_fresh = get_amount_fresh_ids(testinput)
    assert test_fresh == 14

    puzzle_input = get_input("input.txt")
    print(get_amount_fresh_ids(puzzle_input))
