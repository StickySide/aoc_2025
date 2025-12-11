# Advent of code Day 6 Part 2


def get_input(filename: str) -> list[str]:
    """Read input file and return list of lines."""
    with open(filename, "r") as input_file:
        return [line for line in input_file]


def get_product(nums: list[int]) -> int:
    """Calculate the product of all numbers in the list."""
    total: int = 1
    for num in nums:
        total *= num
    return total


def get_answer(data: list[str]):
    """
    Process the grid right-to-left, reading columns as multi-digit numbers.
    Numbers are accumulated in a buffer until an operator (+ or *) is encountered.
    """
    array: list[list[str]] = []

    # Reverse each row character-by-character to read right-to-left
    # Filter out newlines but keep spaces (important for column alignment)
    for row in data:
        columns = [num for num in row[::-1] if num != "\n"]
        array.append(columns)

    print("ARRAY:")
    for row in array:
        print(f"Row length: {len(row)}, Row: {row[:20]}")  # Print first 20 chars
    num_rows = len(array)
    num_columns = max(len(row) for row in array)  # Use max length to handle variable-width rows

    columns: list[list[str]] = []

    total: int = 0

    # Extract vertical columns from the reversed horizontal rows
    for i in range(0, num_columns):
        column: list[str] = []
        for j in range(0, num_rows):
            if i < len(array[j]):  # Check if this row has enough columns
                column.append(array[j][i])
            else:
                column.append(" ")  # Pad with space if row is too short
        columns.append(column)

    # Reconstruct multi-digit numbers from vertical character columns
    # Each column represents one position in the final numbers (reading top to bottom)
    number_buffer: list[str] = []
    for column in columns:
        built_number: list[str] = []
        for char in column:
            built_number.append(char)
        number_buffer.append("".join(built_number).strip())

    # Process numbers and operators from right to left
    # Accumulate numbers in buffer until an operator is found
    buffer: list[int] = []
    for numbers in number_buffer:
        # Case 1: Pure number (no operator) - add to buffer
        if numbers and numbers[-1] not in ["+", "*"]:
            buffer.append(int("".join(numbers)))
        # Case 2: Number ending with '+' - add number, then sum buffer
        elif numbers and numbers[-1] == "+":
            buffer.append(int("".join(numbers[:-1])))
            total += sum(buffer)
            buffer = []
        # Case 3: Number ending with '*' - add number, then multiply buffer
        elif numbers and numbers[-1] == "*":
            buffer.append(int("".join(numbers[:-1])))
            total += get_product(buffer)
            buffer = []

    return total


if __name__ == "__main__":
    data = get_input("testinput.txt")
    answer = get_answer(data)
    assert answer == 3263827

    data = get_input("input.txt")
    answer = get_answer(data)
    print(answer)
