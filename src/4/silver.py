from shared import get_puzzle

puzzle = get_puzzle()
height = len(puzzle)
width = len(puzzle[0])

def directions(x: int, y: int):
    if x + 3 < width:
        yield 1, 0
    if 3 <= x:
        yield -1, 0
    if y + 3 < height:
        yield 0, 1
    if 3 <= y:
        yield 0, -1
    if x + 3 < width and y + 3 < height:
        yield 1, 1
    if 3 <= x and y + 3 < height:
        yield -1, 1
    if x + 3 < width and 3 <= y:
        yield 1, -1
    if 3 <= x and 3 <= y:
        yield -1, -1

count = 0
for y, row in enumerate(puzzle):
    for x, value in enumerate(row):
        if value == "X":
            for dx, dy in directions(x, y):
                count += all(puzzle[y + dy * i][x + dx * i] == letter for i, letter in enumerate("MAS", start=1))

print(count)
