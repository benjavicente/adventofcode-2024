def get_map():
    rows = []
    while True:
        try:
            rows.append(list(input()))
        except EOFError:
            break
    return rows


direction_deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def get_guard_position(gamemap: list[list[str]]):
    for y, row in enumerate(gamemap):
        for x, value in enumerate(row):
            if value == "^":
                return x, y
    raise ValueError("No guard found")
