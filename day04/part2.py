# Advent of Code Day 4 Part 2


def get_input(filename: str) -> list[str]:
    """Read input file and return list of lines."""
    with open(filename, "r") as input_file:
        return [line.strip() for line in input_file]


def roll_accessible(array: list[str], y: int, x: int) -> bool:
    """Check if a roll (@) is accessible (has fewer than 4 adjacent rolls)."""
    adjacent_rolls: int = 0

    # Check all 8 surrounding cells
    for i, j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        # Verify coordinates are within bounds (handles literal edge cases)
        if len(array) > y + i >= 0 and len(array[y]) > x + j >= 0:
            if array[y + i][x + j] == "@":
                adjacent_rolls += 1

    # Roll is accessible if it has fewer than 4 adjacent rolls
    return adjacent_rolls < 4


def tally_rolls(array: list[str]) -> int:
    """
    Iteratively remove accessible rolls until none remain.
    Each iteration removes rolls with < 4 adjacent rolls, which may make new rolls accessible.
    """
    working_array: list[str] = array
    tally: int = 0
    updating: bool = True
    iterations: int = 0

    # Keep removing accessible rolls until no more can be removed
    while updating:
        iterations += 1
        updating = False

        # Process each cell in the grid
        for y in range(len(working_array)):
            line = [x for x in working_array[y]]
            for x in range(len(line)):
                if line[x] == "@":
                    # Check if this roll is accessible
                    if roll_accessible(working_array, y, x):
                        tally += 1
                        line[x] = "."  # Remove accessible roll
                        working_array[y] = "".join(line)
                        updating = True  # Continue iterating

    # Display the final grid
    for line in working_array:
        print(line)
    print(f"Iterations: {iterations}")

    return tally


if __name__ == "__main__":
    testinput = get_input("testinput.txt")
    assert tally_rolls(testinput) == 43

    data = get_input("input.txt")
    print(tally_rolls(data))
