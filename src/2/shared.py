def get_reports():
    try:
        while True:
            line = input()
            numbers = line.split()
            yield list(map(int, numbers))
    except EOFError:
        pass
