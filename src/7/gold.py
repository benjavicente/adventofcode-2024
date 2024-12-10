from shared import get_equations, find_result
from operator import add, mul

# TODO: esta solución esta funcionando lento, sería bueno mandarle profiling

def concat(a: int, b: int):
    return a * 10 ** int(len(str(b))) + b

count = 0
for result, numbers in get_equations():
    if find_result(result, numbers, [add, mul, concat]):
        count += result

print(count)
