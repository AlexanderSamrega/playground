from prettytable import PrettyTable


def gcd(a, b, *, table=False):
    """
    Extended Euclidean algorithm: d == a*x + b*y
    :param a: 1st number
    :param b: 2nd number
    :param table: print steps of algorithm if true
    :return: (x, y, d), where x and y -- Bezout coefficients, d -- greatest common divisor of a and b
    """
    if a < b:
        a, b = b, a
    vector_a = (1, 0, a)
    vector_b = (0, 1, b)
    steps = PrettyTable(['x', 'y', 'r'])
    steps.add_row(vector_a)
    while vector_b[2] > 0:
        steps.add_row(vector_b)
        q = vector_a[2] // vector_b[2]
        x = vector_a[0] - vector_b[0] * q
        y = vector_a[1] - vector_b[1] * q
        r = vector_a[2] % vector_b[2]
        vector_a = vector_b
        vector_b = (x, y, r)
    if table:
        print(steps)
        print(f'GCD of {a} and {b} is {r} == {a} * ({x}) + {b} * ({y})')
    else:
        return vector_b


if __name__ == '__main__':
    a = int(input('a = '))
    b = int(input('b = '))
    gcd(a, b, table=True)
