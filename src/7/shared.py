from typing import Callable

def get_equations():
    while True:
        try:
            entry = input().strip()
            result, numbers = entry.split(":")
            yield int(result), list(map(int, numbers.strip().split()))
        except EOFError:
            return

def find_result(objective: int, numbers: list[int], operations: list[Callable[[int, int], int]]):
    # Asumiendo que la operaciones dan un resultado siempre mayor a sus números
    if numbers[0] > objective:
        return False

    if len(numbers) == 1:
        return numbers[0] == objective

    a = numbers[0]
    b = numbers[1]
    rest = numbers[2:]
    return any(find_result(objective, [operation(a, b)] + rest, operations) for operation in operations)
