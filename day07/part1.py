# Advent of Code Day 7 Part 1


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

    def __init__(self, data: list[list[str]], x: int, y: int):
        self.data = data  # Reference to the grid being modified
        self.x = x
        self.y = y
        self.null_set = ""  # Return value for out-of-bounds reads

    @property
    def contents(self) -> str:
        """Get the character at this cell's position."""
        return self.data[self.y][self.x]

    @contents.setter
    def contents(self, char: "str") -> None:
        """Set the character at this cell's position."""
        self.data[self.y][self.x] = char

    @property
    def below(self) -> str:
        """Get the character in the cell below this one (returns empty string if out of bounds)."""
        if self.y + 1 <= len(self.data):
            return self.data[self.y + 1][self.x]
        else:
            return self.null_set

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

    @right.setter
    def right(self, char: str) -> None:
        """Set the character in the cell to the right (safely handles out of bounds)."""
        try:
            self.data[self.y][self.x + 1] = char
        except IndexError:
            pass


def solve(data: list[list[str]]) -> int:
    """
    Simulate beam propagation through the grid.
    - S: Starting position, emits beam downward
    - ^: Splitter, splits vertical beam into left and right beams
    - .: Empty space, allows beam to pass through
    - |: Active beam marker
    """
    splits: int = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            cell = Cell(data, x, y)

            # Rule 1: Start position - emit beam downward
            if cell.contents == "S":
                cell.below = "|"
                print(f"Found start at {x}, {y}")

            # Rule 2: Splitter with incoming beam - split into left and right
            elif cell.contents == "^" and cell.above == "|":
                splits += 1
                cell.left = "|"
                cell.right = "|"

            # Rule 3: Empty space with beam above - propagate beam downward
            elif cell.contents == "." and cell.above == "|":
                cell.contents = "|"

        display(data)
    return splits


if __name__ == "__main__":
    data = get_input("testinput.txt")
    assert solve(data) == 21

    data = get_input("input.txt")
    print(solve(data))
