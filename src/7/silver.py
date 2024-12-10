from shared import get_equations, find_result
from operator import add, mul

count = 0
for result, number in get_equations():
    if find_result(result, number, [add, mul]):
        count += result

print(count)
