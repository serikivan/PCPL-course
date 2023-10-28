import sys
import math


def get_coef(index, prompt):
    """Получение коэффициентов"""
    try:
        """Чтение из командной строки"""
        coef_input = sys.argv[index]
    except:
        """Ввод с клавиатуры"""
        try:
            coef_input = float(input(prompt))
        except ValueError:
            print("Not a valid value")
            return get_coef(index, prompt)
    return float(coef_input)


def get_sqRoots(root, result):
    """Вычисление корней квадратного уравнения вида x^2 = n"""
    if root >= 0:
        root = math.sqrt(root)
        if root > 0:
            result.append(-root)
        result.append(root)


def get_roots(a, b, c):
    """Вычисление корней уравнения"""
    result = []
    d = b * b - 4 * a * c
    print("Discriminant =", d)
    if d == 0.0:
        root = -b / (2.0 * a)
        get_sqRoots(root, result)
    elif d > 0.0:
        sqd = math.sqrt(d)
        root1 = (-b + sqd) / (2.0 * a)
        root2 = (-b - sqd) / (2.0 * a)
        get_sqRoots(root1, result)
        get_sqRoots(root2, result)
    return result


def main():
    a = get_coef(1, 'Enter real À:')
    b = get_coef(2, 'Enter real B:')
    c = get_coef(3, 'Enter real C:')
    print('You entered: {}x^4 + {}x^2 + {} = 0'.format(a, b, c))
    roots = get_roots(a, b, c)
    len_roots = len(roots)
    if len_roots == 0:
        print('There are no real roots')
    elif len_roots == 1:
        print('There is one real root:\n', *roots)
    else:
        print('There are {} real roots:'.format(len_roots))
        list(map(print, roots))


if __name__ == "__main__":
    main()
