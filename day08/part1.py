from math import sqrt

coord = tuple[int, int, int]


def get_input(filename: str) -> list[coord]:
    with open(filename, "r") as input_file:
        return [
            (int(coord[0]), int(coord[1]), int(coord[2])) for coord in [line.strip().split(",") for line in input_file]
        ]


def distance(p: coord, q: coord) -> float:
    return sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2)


if __name__ == "__main__":
    data = get_input("testinput.txt")
    print(data)
    print(distance(data[0], data[1]))
