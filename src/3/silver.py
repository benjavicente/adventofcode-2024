import re
from shared import get_lines

mul_expr = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
count = 0

for line in get_lines():
    for a, b in mul_expr.findall(line):
        count += int(a) * int(b)

print(count)
