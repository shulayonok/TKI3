import numpy as np


# Строим поле Галуа определённой размерности
def GF(p):
    GF = np.arange(p)
    return GF


# Таблица сложения элементов поля
def add_table(p):
    add_table = np.zeros((p, p))
    for i in range(1, p):
        add_table[i, 0] = i - 1
    for j in range(1, p):
        add_table[0, j] = j - 1
    for i in range(1, p):
        for j in range(1, p):
            add_table[i, j] = ((i - 1) + (j - 1)) % p
    return add_table


# Таблица умножения элементов поля
def multi_table(p):
    mult_table = np.zeros((p, p))
    for i in range(1, p):
        mult_table[i, 0] = i - 1
    for j in range(1, p):
        mult_table[0, j] = j - 1
    for i in range(1, p):
        for j in range(1, p):
            mult_table[i, j] = (mult_table[0, j] * mult_table[i, 0]) % p
    return mult_table


def print_poly(poly):
    polynom = []
    poly = poly[::-1]
    for i, bit in enumerate(poly):
        if bit and i == 0:
            polynom.append(str(bit))
        elif bit and i == 1:
            polynom.append(f'{bit}X')
        elif bit:
            polynom.append(f'{bit}X^{i}')
    if len(polynom) == 0:
        polynom.append('0')
    return ' + '.join(polynom[::-1])


# Новые полиномы
def poly_GF(p, m, primitive_polynomial):
    poly_GF = [np.poly1d([1]), np.poly1d([1, 0]), np.poly1d([12, 11])]
    for i in range(3, p ** m):
        s_mul = np.polymul(poly_GF[i - 1], poly_GF[1])
        div, mod = np.polydiv(s_mul, primitive_polynomial)
        mod_p = np.mod(mod, p).astype(int)
        poly_GF.append(np.poly1d(mod_p))
    return poly_GF


field = GF(13)
print(field)
print()
print(add_table(13))
print()
print(multi_table(13))
print()
# Построение расширенного поля GF(p^m)
primitive_polynomial = np.poly1d([1, 1, 2])
poly_GF = poly_GF(13, 2, primitive_polynomial)

for i in range(len(poly_GF)):
    print(f'X^{i} = {print_poly(list(poly_GF[i]))}')

