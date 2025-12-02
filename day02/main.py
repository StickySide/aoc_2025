def get_input(filename: str) -> list[str]:
    input = ""
    with open(filename, "r") as input_file:
        input: str = input_file.read()
    return input.split(",")


def make_range_list(id_range_string: str) -> list[str]:
    start, end = id_range_string.split("-")
    return [str(n) for n in range(int(start), int(end) + 1)]


def is_invalid_id(id: str) -> bool:
    search_string = (id + id)[1:-1]
    return id in search_string


def get_invalid_ids(id_range: str) -> list[int]:
    invalid_ids: list[int] = []
    ids = make_range_list(id_range)
    for id in ids:
        if is_invalid_id(id):
            invalid_ids.append(int(id))
    return invalid_ids


def total_invalid_ids(input: list[str]) -> int:
    total: int = 0
    for entry in input:
        for invalid_id in get_invalid_ids(entry):
            total += invalid_id
    return total


if __name__ == "__main__":
    input = get_input("input.txt")
    print(total_invalid_ids(input))
