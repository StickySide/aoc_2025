# Advent of Code Day 5 Part 1


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


def get_fresh_ingredients(ids: list[int], ranges: list[tuple[int, int]]) -> list[int]:
    """
    Filter ingredient IDs that fall within any of the valid ranges.
    An ingredient is fresh if its ID is within at least one range (inclusive).
    """
    fresh_ingredients: list[int] = []

    for id in ids:
        # Check if this ID falls within any valid range
        for lower, upper in ranges:
            if lower <= id <= upper:
                fresh_ingredients.append(id)
                break  # Stop checking once we find a matching range

    return fresh_ingredients


def get_number_fresh_ingredients(data: list[str]) -> int:
    """
    Main solver: parse input and count how many ingredients are fresh.
    Fresh ingredients are those whose IDs fall within valid ranges.
    """
    ranges, ingredients = split_range_and_ingredients(data)
    ids = [int(ingredient) for ingredient in ingredients]
    ranges = build_ranges(ranges)
    return len(get_fresh_ingredients(ids, ranges))


if __name__ == "__main__":
    testinput = get_input("testinput.txt")
    test_fresh = get_number_fresh_ingredients(testinput)
    assert test_fresh == 3

    puzzle_input = get_input("input.txt")
    print(get_number_fresh_ingredients(puzzle_input))
