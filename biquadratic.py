import sys
import math
import cmath

def input_coefficients():
    print("Введите коэффициенты A, B и C по очереди")
    coefficients_array = []
    for i in range(3):
        while True:
            try:
                value = float(input(f"Коэффициент {chr(65 + i)}: "))
                coefficients_array.append(value)
                break
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число.")
    return coefficients_array

def solve_biquadratic(a, b, c):

    if a == 0:
        # Уравнение сводится к квадратному: b*x^2 + c = 0
        if b == 0:
            return [] if c != 0 else ["Любое число"]  # c = 0: любое x, иначе решений нет
        y = -c / b
        if y < 0:
            # Только комплексные корни
            sqrt_y = cmath.sqrt(y)
            return [sqrt_y, -sqrt_y]
        else:
            sqrt_y = math.sqrt(y)
            return [sqrt_y, -sqrt_y]
    # Решаем квадратное относительно y = x^2: a*y^2 + b*y + c = 0
    D = b**2 - 4*a*c
    roots = []
    for sqrt_func in (cmath.sqrt,):
        d = sqrt_func(D)
        y1 = (-b + d) / (2*a)
        y2 = (-b - d) / (2*a)
        for y in (y1, y2):
            # x^2 = y => x = ±sqrt(y)
            sqrt_y = sqrt_func(y)
            roots.append(sqrt_y)
            roots.append(-sqrt_y)
    # Убираем дублирующиеся корни (например, если y=0)
    unique_roots = []
    for r in roots:
        if not any(abs(r - ur) < 1e-8 for ur in unique_roots):
            unique_roots.append(r)
    return unique_roots

def print_solutions(solutions):
    print("Решения уравнения:")
    for i, sol in enumerate(solutions, 1):
        if isinstance(sol, complex):
            print(f"x{i} = {sol.real:.2f} + {sol.imag:.2f}i")
        else:
            print(f"x{i} = {sol:.2f}")

def main():
    if len(sys.argv) == 4 and sys.argv[1].replace('.', '', 1).isdigit() and sys.argv[2].replace('.', '', 1).isdigit() and sys.argv[3].replace('.', '', 1).isdigit():
        coefficient_a, coefficient_b, coefficient_c = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    else:
        coefficient_a, coefficient_b, coefficient_c = input_coefficients()
    print(f"Коэффициенты: A={coefficient_a}, B={coefficient_b}, C={coefficient_c}")

    roots = solve_biquadratic(coefficient_a, coefficient_b, coefficient_c)
    print_solutions(roots)

if __name__ == "__main__":
    main()
