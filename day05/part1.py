def get_input(filename: str) -> list[str]:
    """Read input file and return list of lines."""
    with open(filename, "r") as input_file:
        return [line.strip() for line in input_file]


def split_range_and_ingredients(data: list[str]) -> tuple[list[str], list[str]]:
    split_point: int = data.index("")
    return data[:split_point], data[split_point + 1 :]


def build_ranges(data: list[str]) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []

    for string in data:
        lower, upper = string.split("-")
        ranges.append((int(lower), int(upper)))

    # print(f"Ranges: {ranges}")
    return ranges


def get_fresh_ingredients(ids: list[int], ranges: list[tuple[int, int]]) -> list[int]:
    fresh_ingredients: list[int] = []

    for id in ids:
        for lower, upper in ranges:
            # print(f"Testing id: {id} in {lower} - {upper}")
            if id <= upper and id >= lower:
                fresh_ingredients.append(id)
                break

    return fresh_ingredients


def get_number_fresh_ingredients(data: list[str]) -> int:
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
