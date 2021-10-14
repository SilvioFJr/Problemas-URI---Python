# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''  # Área 1112

base = input().split()
pi = 3.14159

a = float(base[0])
b = float(base[1])
c = float(base[2])

tri = ((a*c)/float(2))
cir = (pi*c**2)
tra = (((a+b)*c)/float(2))
qua = (b**2)
ret = (a*b)

print("TRIANGULO: %.3f" % tri)
print("CIRCULO: %.3f" % cir)
print("TRAPEZIO: %.3f" % tra)
print("QUADRADO: %.3f" % qua)
print("RETANGULO: %.3f" % ret)
