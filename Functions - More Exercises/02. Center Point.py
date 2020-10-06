def define_center_point(a, b, c, d):
    z_one = abs((a ** 2) + (b ** 2))
    z_two = abs((c ** 2) + (d ** 2))

    if z_one < z_two:
        return f'({int(a)}, {int(b)})'
    elif z_two < z_one:
        return f'({int(c)}, {int(d)})'
    else:
        return f'({int(a)}, {int(b)})'


x_one = float(input())
y_one = float(input())
x_two = float(input())
y_two = float(input())
print(define_center_point(x_one, y_one, x_two, y_two))