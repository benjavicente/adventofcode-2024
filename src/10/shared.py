def get_topographic_map():
    rows = []
    while True:
        try:
            rows.append([int(c) for c in input().strip()])
        except EOFError:
            return rows
