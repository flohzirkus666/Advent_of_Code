from utils.helpers import load_input


def part1(puzzle_input: str) -> None:
    """First puzzle solution"""
    rotations = 0
    dial_position = 50
    for row in puzzle_input.splitlines():
        if "L" in row:
            number = int(row.split("L")[1])
            new_position = dial_position - number
            dial_position = new_position % 100
        elif "R" in row:
            number = int(row.split("R")[1])
            new_position = dial_position + number
            dial_position = new_position % 100
        if dial_position == 0:
            rotations += 1
    print(f"Rotations: {rotations}")


if __name__ == "__main__":
    puzzle1_input = load_input(input_file="input/day01_pt1.txt")
    part1(puzzle1_input)
