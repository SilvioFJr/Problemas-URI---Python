# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


# Idade em Dias ...1020

x = int(input())  # idade em dias
a = 0
m = 0
d = 0

a = x//365

if (a == 0):
    m = x//30
else:
    m = (x-a*365)//30

d = x-a*365-m*30
print(str(a)+" ano(s)")
print(str(m)+" mes(es)")
print(str(d)+" dia(s)")
