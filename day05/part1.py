def get_input(filename: str) -> list[str]:
    """Read input file and return list of lines."""
    with open(filename, "r") as input_file:
        return [line.strip() for line in input_file]


def split_range_and_ingredients(data: list[str]) -> tuple[list[str], list[str]]:
    split_point: int = data.index("")
    return data[:split_point], data[split_point + 1 :]


def build_ranges(data: list[str]) -> set[int]:
    ranges: set[int] = set()

    for string in data:
        lower, upper = string.split("-")
        for numbers in range(int(lower), int(upper) + 1):
            ranges.add(numbers)

    return ranges


def get_fresh_ingredients(ids: list[int], ranges: set[int]) -> list[int]:
    fresh_ingredients: list[int] = []
    for id in ids:
        if id in ranges:
            fresh_ingredients.append(id)
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
    print(puzzle_input)
    print(get_number_fresh_ingredients(puzzle_input))
