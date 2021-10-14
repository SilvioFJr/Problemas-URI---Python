# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


# Conversão de tempo 1019

x = int(input())  # tempo em segundos
h = 0
m = 0
s = 0
# 1min=60seg || 1h=60min=3600seg ||556

h = x//3600

if (h == 0):
    m = x//60
else:
    m = (x-h*3600)//60

s = x-h*3600-m*60
print(str(h)+":"+str(m)+":"+str(s))
