# Вариант
from math import sqrt


variant = (31 + 8) % 3 + 1
print(f"V = {variant}")

def triangle_type(a, b, c):
    """
    -1 - triangle doesn't exists;\n
     0 - equilateral triangle;\n
     1 - isosceles triangle;\n
     2 - general triangle.\n
    """
    if not (a + b > c and a + c > b and b + c > a):
        return -1

    if a == b == c:
        return 0

    if a - b == 0 or a - c == 0 or b - c == 0:
        return 1

    return 2

def quad_equation_solver(a, b, c):
    if a == 0:
        return ()

    discriminant = b**2 - 4 * a * c
    
    if discriminant < 0:
        return ()

    if discriminant == 0:
        x = -b / (2 * a)
        return (x,)

    x1 = (-b + sqrt(discriminant)) / (2 * a)
    x2 = (-b - sqrt(discriminant)) / (2 * a)

    return (x1, x2)


    
if __name__ == "__main__":

    # Задание 1

    (a, b, c) = input("Введите стороны треугольника через пробел: ").split()
    a, b, c = float(a), float(b), float(c)
    t_type = triangle_type(a, b, c)
    
    match t_type:
        case -1:
            print("Треугольник не существует")
        case 0:
            print("Треугольник равносторонний")
        case 1:
            print("Треугольник равнобедренный")
        case 2:
            print("Треугольник общего вида")


    # Задание 2

    (a, b, c) = input("Введите коеффициенты уравнения через пробел: ").split()
    a, b, c = float(a), float(b), float(c)

    solution = quad_equation_solver(a, b, c)

    print(f"Уравнение\n({a})*X^2 + ({b})*X + ({c}) = 0")
    print("Количество корней: ", len(solution))
    
    for k, v in enumerate(solution):
        print(v)







    
    

