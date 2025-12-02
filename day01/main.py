# Advent of Code 2025 - Day 1 part 2


class Dial:
    def __init__(self) -> None:
        self.dial_position: int = 50
        self.zero_count: int = 0

    def reset(self) -> None:
        self.dial_position = 50
        self.zero_count = 0

    def rotate(self, direction: str, distance: int) -> None:
        starting_position: int = self.dial_position

        if direction == "L":
            self.dial_position -= distance
        elif direction == "R":
            self.dial_position += distance

        # Resolve quotient, and new dial position
        quotient, self.dial_position = divmod(self.dial_position, 100)
        count: int = abs(quotient)

        # Edge Cases
        # Turned left and landed on zero, add one to the count
        if direction == "L" and self.dial_position == 0:
            count += 1
        # Started at zero, turned left, subtract one from the count
        elif direction == "L" and starting_position == 0:
            count -= 1

        # Update zero count
        self.zero_count += count

    def solve(self, input: list[str]) -> None:
        print("Rotating dial...")
        for line in input:
            self.rotate(direction=line[0], distance=int(line[1:]))
        print(f"The password is {self.zero_count}")


def get_input(filename: str) -> list[str]:
    input: list[str] = []
    with open(filename, "r") as input_file:
        for line in input_file:
            input.append(line.strip())
    return input


if __name__ == "__main__":
    dial = Dial()
    input = get_input("input.txt")
    dial.solve(input)
