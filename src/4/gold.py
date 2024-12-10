from shared import get_puzzle

puzzle = get_puzzle()
count = 0

for y, row in enumerate(puzzle[1:-1], start=1):
    for x, value in enumerate(row[1:-1], start=1):
        if value == "A":
            tr = puzzle[y - 1][x + 1]
            br = puzzle[y + 1][x + 1]
            bl = puzzle[y + 1][x - 1]
            tl = puzzle[y - 1][x - 1]
            if not ({"M", "S"} - {tr, bl} or {"M", "S"} - {tl, br}):
                count += 1

print(count)
