x = input().split()
x1 = x2 = 0
a = float(x[0])
b = float(x[1])
c = float(x[2])

delta = (b**2)-(4*a*c)


if (delta < 0) or (a == 0):
    print('Impossivel calcular')
else:
    x1 = (-b+(delta**0.5))/(2*a)
    x2 = (-b-(delta**0.5))/(2*a)
    print('R1 = {:.5f}\nR2 = {:.5f}'.format(x1, x2))
