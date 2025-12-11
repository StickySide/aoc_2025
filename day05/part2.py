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
    """
    Count total fresh ingredient IDs by merging overlapping ranges.
    Uses interval merging to avoid counting overlapping IDs multiple times.
    """
    ranges, _ = split_range_and_ingredients(data)
    ranges = build_ranges(ranges)

    # Sort the ranges by the starting number
    ranges.sort(key=lambda r: r[0])

    # Initialize list with first interval
    merged: list[tuple[int, int]] = [ranges[0]]
    amount_fresh_ids: int = 0

    # Process each subsequent range and merge overlapping intervals
    for a, b in ranges[1:]:
        x, y = merged[-1]

        # Case 1: New range is completely contained within the last merged range
        if y >= b:
            continue  # Skip, already covered
        # Case 2: New range partially overlaps (extends beyond the last merged range)
        elif y >= a:
            merged[-1] = (x, b)  # Extend the merged range to include new upper bound
        # Case 3: New range is completely separate (gap exists)
        elif a > y:
            merged.append((a, b))  # Add as a new separate interval

    # Calculate the amount of 'fresh' ingredients, and total them
    # Each interval [a, b] contains (b - a + 1) IDs
    for a, b in merged:
        amount_fresh_ids += b - a + 1

    return amount_fresh_ids


if __name__ == "__main__":
    testinput = get_input("testinput.txt")
    test_fresh = get_amount_fresh_ids(testinput)
    assert test_fresh == 14

    puzzle_input = get_input("input.txt")
    print(get_amount_fresh_ids(puzzle_input))
