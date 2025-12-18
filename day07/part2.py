# Advent of Code Day 7 Part 2
from typing import Deque
from collections import deque
from time import time

Coord = tuple[int, int]


def get_input(filename: str) -> list[list[str]]:
    """Read input file and return 2D grid of characters."""
    with open(filename, "r") as input_file:
        return [[char for char in line.strip()] for line in input_file]


def display(data: list[list[str]]) -> None:
    """Print the current state of the grid."""
    for line in data:
        print("".join(line))


class Cell:
    """
    A cell in the grid with convenient property-based access to neighbors.
    Provides clean syntax for reading/writing the cell and its adjacent cells.
    """

    def __init__(self, data: list[list[str]], coord: Coord):
        self.data = data  # Reference to the grid being modified
        self.x = coord[1]
        self.y = coord[0]
        self.null_set = ""  # Return value for out-of-bounds reads

    @property
    def contents(self) -> str:
        """Get the character at this cell's position."""
        return self.data[self.y][self.x]

    @property
    def coord(self) -> Coord:
        return (self.y, self.x)

    @contents.setter
    def contents(self, char: "str") -> None:
        """Set the character at this cell's position."""
        self.data[self.y][self.x] = char

    @property
    def below(self) -> str:
        """Get the character in the cell below this one (returns empty string if out of bounds)."""
        if self.y + 1 < len(self.data):
            return self.data[self.y + 1][self.x]
        else:
            return self.null_set

    @property
    def coord_below(self) -> Coord | None:
        if self.y + 1 < len(self.data):
            return (self.y + 1, self.x)

    @below.setter
    def below(self, char: str) -> None:
        """Set the character in the cell below (safely handles out of bounds)."""
        try:
            self.data[self.y + 1][self.x] = char
        except IndexError:
            pass

    @property
    def above(self) -> str:
        """Get the character in the cell above this one (returns empty string if out of bounds)."""
        if self.y - 1 >= 0:
            return self.data[self.y - 1][self.x]
        else:
            return self.null_set

    @above.setter
    def above(self, char: str) -> None:
        """Set the character in the cell above (safely handles out of bounds)."""
        try:
            self.data[self.y - 1][self.x] = char
        except IndexError:
            pass

    @property
    def left(self) -> str:
        """Get the character in the cell to the left (returns empty string if out of bounds)."""
        if self.x - 1 >= 0:
            return self.data[self.y][self.x - 1]
        else:
            return self.null_set

    @property
    def coord_left(self) -> Coord | None:
        if self.x - 1 >= 0:
            return (self.y, self.x - 1)

    @left.setter
    def left(self, char: str) -> None:
        """Set the character in the cell to the left (safely checks bounds)."""
        if self.x - 1 >= 0:
            self.data[self.y][self.x - 1] = char

    @property
    def right(self) -> str:
        """Get the character in the cell to the right (returns empty string if out of bounds)."""
        if self.x + 1 <= len(self.data[0]):
            return self.data[self.y][self.x + 1]
        else:
            return self.null_set

    @property
    def coord_right(self) -> Coord | None:
        if self.x + 1 <= len(data[0]):
            return (self.y, self.x + 1)

    @right.setter
    def right(self, char: str) -> None:
        """Set the character in the cell to the right (safely handles out of bounds)."""
        try:
            self.data[self.y][self.x + 1] = char
        except IndexError:
            pass


def solve(data: list[list[str]]) -> int:
    """ """

    timelines: int = 0
    start: Coord = (0, 0)

    q: Deque[Coord] = deque()

    # Find start
    for x in range(len(data[0])):
        if data[0][x] == "S":
            start = (0, x)
            q.append(start)

    # BFS loop

    memo: dict[Coord, int] = {}
    memo[start] = 1
    visited: set[Coord] = set()

    while q:
        current_cell = Cell(data, q.popleft())

        if current_cell.coord in visited:
            continue

        visited.add(current_cell.coord)

        beams = memo.get(current_cell.coord, 0)  # Assign current cell beams

        if current_cell.below == "." and current_cell.coord_below:
            memo[current_cell.coord_below] = beams + memo.get(current_cell.coord_below, 0)
            q.append(current_cell.coord_below)

        elif current_cell.below == "^" and current_cell.coord_below:
            current_cell = Cell(data, current_cell.coord_below)
            if current_cell.coord_left:
                memo[current_cell.coord_left] = beams + memo.get(current_cell.coord_left, 0)
                q.append(current_cell.coord_left)
            if current_cell.coord_right:
                memo[current_cell.coord_right] = beams + memo.get(current_cell.coord_right, 0)
                q.append(current_cell.coord_right)

        elif current_cell.coord[0] == len(data) - 1:
            timelines += beams
        # print(memo)

    print(timelines)
    return timelines


if __name__ == "__main__":
    data = get_input("testinput.txt")
    assert solve(data) == 40

    data = get_input("input.txt")
    print(solve(data))
