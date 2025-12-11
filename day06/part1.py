# Advent of code Day 6 Part 1


def get_input(filename: str) -> list[str]:
    """Read input file and return list of lines."""
    with open(filename, "r") as input_file:
        return [line.strip() for line in input_file]


def get_product(nums: list[int]) -> int:
    """Calculate the product of all numbers in the list."""
    total: int = 1
    for num in nums:
        total *= num
    return total


def get_answer(data: list[str]):
    """
    Process column-wise operations on a 2D array.
    Each column ends with an operator (+ or *) that determines how to combine the numbers above it.
    """
    array: list[list[str]] = []

    # Parse input into 2D array, splitting on spaces and filtering empty strings
    for row in data:
        columns = [num for num in row.split(" ") if num not in [""]]
        array.append(columns)

    num_rows = len(array)
    num_columns = len(array[0])

    column_answers: list[int] = []

    # Process each column
    for i in range(0, num_columns):
        column: list[str] = []
        # Extract all values in this column
        for j in range(0, num_rows):
            column.append(array[j][i])

        # Apply the operation specified by the last element
        if column[-1] == "+":
            column_answers.append(sum(int(num) for num in column[:-1]))
        elif column[-1] == "*":
            column_answers.append(get_product([int(num) for num in column[:-1]]))

    # Sum all column results
    return sum(column_answers)


if __name__ == "__main__":
    data = get_input("testinput.txt")
    answer = get_answer(data)
    assert answer == 4277556

    data = get_input("input.txt")
    answer = get_answer(data)
    print(answer)
