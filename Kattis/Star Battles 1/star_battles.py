import fileinput
import sys

board = []
marks = []
region_tally = {}
row_tally = [0] * 10
column_tally = [0] * 10

line = 0

def hasPreviousAdjacent(row, column):
    w = (column > 0) and marks[row][column - 1] == "*"
    nw = (row > 0 and column > 0) and marks[row - 1][column - 1] == "*"
    ne = (row > 0 and column < 9) and marks[row - 1][column + 1] == "*"
    n = (row > 0) and marks[row - 1][column] == "*"

    return w or nw or ne or n


for line_content in fileinput.input():
    line += 1

    cells = list(line_content.strip())
    row_content = []

    if line <= 10:
        board.append(row_content)
        for region_name in cells:
            region_tally[region_name] = 0
            row_content.append(region_name)
    elif line <= 20:
        marks.append(row_content)
        row = line - 11
        for column, character in enumerate(cells):
            if character == "*":
                region_name = board[row][column]
                if (
                    region_tally[region_name] == 2
                    or row_tally[row] == 2
                    or column_tally[column] == 2
                    or hasPreviousAdjacent(row, column)
                ):
                    print("invalid")
                    sys.exit()
                region_tally[region_name] += 1
                row_tally[row] += 1
                column_tally[column] += 1
            row_content.append(character)

for count in region_tally.values():
    if count != 2:
        print("invalid")
        sys.exit()

for count in row_tally:
    if count != 2:
        print("invalid")
        sys.exit()

for count in column_tally:
    if count != 2:
        print("invalid")
        sys.exit()

print("valid")