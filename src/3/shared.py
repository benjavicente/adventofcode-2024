def get_lines():
    while True:
        try:
            yield input()
        except EOFError:
            break
