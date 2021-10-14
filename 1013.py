# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''  # O maior de 3 ... 1013


num = input().split()

a = int(num[0])
b = int(num[1])
c = int(num[2])

m1 = ((abs(a-b)+a+b)/2)
M = ((abs(m1-c)+m1+c)/2)

print("%.0f eh o maior" % M)
