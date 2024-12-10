def get_lists():
    left = []
    right = []

    try:
        while True:
            line = input()
            numbers = line.split()
            assert len(numbers) == 2
            left.append(int(numbers[0]))
            right.append(int(numbers[1]))
    except EOFError:
        pass

    return left, right
