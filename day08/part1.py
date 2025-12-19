from math import sqrt
from itertools import combinations

coord = tuple[int, int, int]


def get_input(filename: str) -> list[coord]:
    with open(filename, "r") as input_file:
        return [
            (int(coord[0]), int(coord[1]), int(coord[2])) for coord in [line.strip().split(",") for line in input_file]
        ]


def distance(pair: tuple[coord, coord]) -> float:
    p = pair[0]
    q = pair[1]
    return sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2)


if __name__ == "__main__":
    data = get_input("testinput.txt")

    combos: list[tuple[coord, coord]] = [combo for combo in combinations(data, 2)]

    combos.sort(key=lambda x: distance(x))

    for combo in combos:
        print(combo)
