def get_puzzle():
    rows = []
    while True:
        try:
            rows.append(list(input()))
        except EOFError:
            break
    return rows
