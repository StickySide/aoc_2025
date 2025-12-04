# Advent of Code Day 4 Part 1


def get_input(filename: str) -> list[str]:
    """Read input file and return list of lines."""
    with open(filename, "r") as input_file:
        return [line.strip() for line in input_file]


def roll_accessible(array: list[str], y: int, x: int) -> bool:
    """Check if a roll (@) is accessible (has fewer than 4 adjacent rolls)."""
    adjacent_rolls: int = 0

    # Check all 8 surrounding cells
    for i, j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        # Verify coordinates are within bounds (handles edge cases)
        if len(array) > y + i >= 0 and len(array[y]) > x + j >= 0:
            if array[y + i][x + j] == "@":
                adjacent_rolls += 1

    # Roll is accessible if it has fewer than 4 adjacent rolls
    return adjacent_rolls < 4


def tally_rolls(array: list[str]) -> int:
    """Count accessible rolls and mark them with 'x' in the output."""
    tally: int = 0
    new_array: list[str] = []

    # Process each cell in the grid
    for y in range(len(array)):
        new_line = ""
        for x in range(len(array[y])):
            if array[y][x] == "@":
                # Check if this roll is accessible
                if roll_accessible(array, y, x):
                    tally += 1
                    new_line += "x"  # Mark accessible roll
                else:
                    new_line += array[y][x]  # Keep inaccessible roll
            else:
                new_line += array[y][x]  # Keep non-roll cells unchanged
        new_array.append(new_line)

    # Display the marked grid
    for line in new_array:
        print(line)
    return tally


if __name__ == "__main__":
    testinput = get_input("testinput.txt")
    assert tally_rolls(testinput) == 13

    data = get_input("input.txt")
    print(tally_rolls(data))
