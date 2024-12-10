import re
from shared import get_lines

instruction_expr = re.compile(r"(mul|don\'t|do)\((\d{1,3},\d{1,3})?\)")
active = True
count = 0

for line in get_lines():
    for instruction, args in instruction_expr.findall(line):
        if instruction == "mul" and active:
            a, b = args.split(",")
            count += int(a) * int(b)
        elif instruction == "don't":
            active = False
        elif instruction == "do":
            active = True

print(count)
