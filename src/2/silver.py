# 402
from shared import get_reports

def initial_check(a: int, b: int):
    return 0 < abs(b - a) <= 3, increasing_check if a < b else decreasing_check

def increasing_check(a: int, b: int):
    return 0 < b - a <= 3, increasing_check

def decreasing_check(a: int, b: int):
    return 0 < a - b <= 3, decreasing_check


def report_is_safe(report: list[int]):
    check = initial_check

    report_iter = iter(report)
    prev_value = next(report_iter)

    for next_value in report_iter:
        ok, check = check(prev_value, next_value)
        if not ok:
            return 0
        prev_value = next_value
    return 1

print(sum(map(report_is_safe, get_reports())))
