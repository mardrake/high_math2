import math

# Ввести координаты синего вектора
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
z1 = float(input('z1 = '))

lvec1 = math.sqrt(x1 * x1 + y1 * y1 + z1 * z1)

print('Length blue = ', lvec1)

# Ввести координаты красного вектора
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
z2 = float(input('z2 = '))

lvec2 = math.sqrt(x2 * x2 + y2 * y2 + z2 * z2)

print('Length red = ', lvec2)

lvec3 = math.sqrt(lvec2 * lvec2 - lvec1 * lvec1)

print('Length green = ', lvec3)
