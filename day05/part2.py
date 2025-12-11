# Advent of Code Day 5 Part 2
from time import time


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

    # Parse the data
    ranges, _ = split_range_and_ingredients(data)
    ranges = build_ranges(ranges)

    # Sort the ranges by the starting number
    ranges.sort(key=lambda r: r[0])

    # Initialize list with first interval
    merged: list[tuple[int, int]] = [ranges[0]]

    # Process each subsequent interval and merge overlaps
    for a, b in ranges[1:]:
        x, y = merged[-1]

        # If the intervals overlap
        if a <= y:
            merged[-1] = (x, max(b, y))  # Extend the merged range to include new upper bound

        # If the intervals do not overlap
        elif a > y:
            merged.append((a, b))  # Add as a new separate interval

    # Calculate the amount of 'fresh' ingredients, and total them
    # Each interval [a, b] contains (b - a + 1) IDs
    return sum(b - a + 1 for a, b in merged)


if __name__ == "__main__":
    testinput = get_input("testinput.txt")
    test_fresh = get_amount_fresh_ids(testinput)
    assert test_fresh == 14

    puzzle_input = get_input("input.txt")
    start_time = time()
    print(get_amount_fresh_ids(puzzle_input))
    print(f"Answer found in {time() - start_time} seconds")
