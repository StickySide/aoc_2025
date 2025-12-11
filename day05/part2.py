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

    # Sort the ranges by the starting number
    ranges.sort(key=lambda ranges: ranges[0])
    print(f"Sorted ranges: {ranges}")

    # Initialize list with first interval
    merged: list[tuple[int, int]] = [ranges[0]]
    amount_fresh_ids: int = 0

    print(f"Merge list: {merged}")
    for a, b in ranges[1:]:
        x, y = merged[-1]

        print(f"Comparing {x}-{y} and {a}-{b}")
        # If there is overlap, but the merged interval covers the entire new interval
        if y >= b:
            continue
        # If merged overlaps just the end of the interval
        elif y >= a:
            merged[-1] = (x, b)  # Merge them and update the last merged interval
            print(f" They overlap! Merging {x}-{b}")
        elif a > y:
            merged.append((a, b))  # Otherwise add the non-overlapped interval to the merge list
            print(" No overlap")

    # Calculate the amount of 'fresh' ingredients, and total them
    for a, b in merged:
        amount_fresh_ids += b - a + 1

    return amount_fresh_ids


if __name__ == "__main__":
    testinput = get_input("testinput.txt")
    test_fresh = get_amount_fresh_ids(testinput)

    assert test_fresh == 14

    puzzle_input = get_input("input.txt")
    print(get_amount_fresh_ids(puzzle_input))
