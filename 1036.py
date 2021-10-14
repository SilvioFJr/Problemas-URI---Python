x = input().split()
x1 = x2 = 0
a = float(x[0])
b = float(x[1])
c = float(x[2])

delta = (b**2)-(4*a*c)


if (delta < 0) or (a == 0):
    print('Impossivel calcular')
else:
    x1 = round((-b+(delta**0.5))/(2*a), 5)
    x2 = round((-b-(delta**0.5))/(2*a), 5)
    print('R1 = {}\nR2 = {}'.format(x1, x2))
