# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
a = input().split()
a1 = int(a[0])
a2 = int(a[1])
a3 = float(a[2])

b = input().split()
b1 = int(b[0])
b2 = int(b[1])
b3 = float(b[2])

s = (float(a2)*a3)+(float(b2)*b3)
print("VALOR A PAGAR: R$ %.2f" % s)
