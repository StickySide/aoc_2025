# Advent of code 2025 Day 2 Part 2


def get_input(filename: str) -> list[str]:
    with open(filename, "r") as input_file:
        return input_file.read().split(",")


def make_range_list(id_range_string: str) -> list[str]:
    """
    From the string format "xxx-yyy" return a list of strings from xxx to yyy
    """
    start, end = id_range_string.split("-")
    return [str(n) for n in range(int(start), int(end) + 1)]


def is_invalid_id(id: str) -> bool:
    """
    Return if an id number is invalid (has repetition twice or more)
    """
    search_string = (id + id)[1:-1]
    return id in search_string


def get_invalid_ids(id_range: str) -> list[int]:
    """
    Return a list of invalid IDs from an id range
    """
    invalid_ids: list[int] = []
    ids = make_range_list(id_range)
    for id in ids:
        if is_invalid_id(id):
            invalid_ids.append(int(id))
    return invalid_ids


def total_invalid_ids(input: list[str]) -> int:
    """
    Return a the sum total of all the invalid ids found in the input file
    """
    total: int = 0
    for entry in input:
        invalid_ids = get_invalid_ids(entry)
        print(
            f"Checking {entry}: {len(invalid_ids) if len(invalid_ids) > 0 else 'No'} invalid IDs found -"
        )
        for id in invalid_ids:
            print(f"    {id}")
        for invalid_id in invalid_ids:
            total += invalid_id
    return total


if __name__ == "__main__":
    input = get_input("input.txt")
    print(f"Sum of all invalid IDs: {total_invalid_ids(input)}")
