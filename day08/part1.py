from math import sqrt
from itertools import combinations

# Type alias for a 3D coordinate (x, y, z)
coord = tuple[int, int, int]


def get_input(filename: str) -> list[coord]:
    """
    Read 3D coordinates from a file.

    Args:
        filename: Path to the input file with comma-separated coordinates

    Returns:
        List of 3D coordinate tuples (x, y, z)
    """
    with open(filename, "r") as input_file:
        # Parse each line: split by commas and convert to integer tuple
        return [
            (int(coord[0]), int(coord[1]), int(coord[2])) for coord in [line.strip().split(",") for line in input_file]
        ]


def distance(pair: tuple[coord, coord]) -> float:
    """
    Calculate the Euclidean distance between two 3D points.

    Args:
        pair: Tuple containing two 3D coordinates

    Returns:
        The Euclidean distance between the two points
    """
    p = pair[0]
    q = pair[1]
    # Apply the 3D distance formula: sqrt((x2-x1)² + (y2-y1)² + (z2-z1)²)
    return sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2)


if __name__ == "__main__":
    # Read 3D coordinates from the input file
    data = get_input("testinput.txt")

    # Generate all possible pairs of coordinates (combinations of 2)
    combos: list[tuple[coord, coord]] = [combo for combo in combinations(data, 2)]

    # Sort the pairs by their distance (closest pairs first)
    combos.sort(key=lambda x: distance(x))

    # Print all coordinate pairs in order of increasing distance
    for combo in combos:
        print(combo)
