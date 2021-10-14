# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''  # Distância Entre Dois Pontos  1015


x = input().split()
y = input().split()


x1 = float(x[0])
x2 = float(y[0])

y1 = float(y[1])
y2 = float(x[1])

d = (
    (
        ((x2-x1)**2)
        +
        ((y2-y1)**2)
    )
    ** 0.5)

print("%.4f" % d)
