
from shared import get_reports

def is_increasing(report: list[int]):
    # Se puede asumir que tiene largo >= 5
    # Al menos la mitad (2) de las comparaciones deben ser incrementales
    # Esto es, dado que:
    # 1. Un valor no incremental en el peor caso, puede estar al medio, rompiendo 2 de 4 comparaciones
    # 2. Si no es incremental, entonces sin valores es 0 y con 1 metido entremedio puede causar solo 1 comparación verdadera
    return sum((report[0] < report[1], report[1] < report[2], report[2] < report[3], report[3] < report[4])) >= 2

def is_in_range(a: int, b: int, *, increasing: bool):
    sign = 1 if increasing else -1
    return 0 < sign * (b - a) <= 3

def report_is_safe_with_extra_attept(report: list[int], remaining_attepts=1):
    increasing = is_increasing(report)

    report_iter = iter(report)
    prev_value = next(report_iter)

    for i, next_value in enumerate(report_iter):
        if is_in_range(prev_value, next_value, increasing=increasing):
            prev_value = next_value
        elif remaining_attepts == 0:
            return 0
        else:
            # TODO: No me gustó esta solución
            # Ni funciona para varios intentos
            # Es como algo super puntual que se podría optimizar mucho
            without_prev = report[:i] + report[i + 1:]
            without_next = report[:i + 1] + report[i + 2:]
            return any((
                report_is_safe_with_extra_attept(without_prev, remaining_attepts - 1),
                report_is_safe_with_extra_attept(without_next, remaining_attepts - 1)
            ))

    return 1

print(sum(map(report_is_safe_with_extra_attept, get_reports())))
