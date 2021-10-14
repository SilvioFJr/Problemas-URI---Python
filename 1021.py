# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''  # Notas e Moedas....1021

x = round(float(input()), 2)
tam_notas = tam_moedas = 6

vnotas = [100, 50, 20, 10, 5, 2]
vmoedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for val in range(tam_notas):
    aux = int(x/float(vnotas[val]))
    x = round((x-round((float(vnotas[val])*round(float(aux), 2)), 2)), 2)
    print(str(aux)+" nota(s) de R$ "+str(vnotas[val])+".00")


print("MOEDAS:")
for val in range(tam_moedas):
    aux = int(x/float(vmoedas[val]))
    # o problema de arredondamento foi resolvido limitando o valor do x em apenas 2 casas decimais
    x = round((x-round((float(vmoedas[val])*round(float(aux), 2)), 2)), 2)
    print(str(aux)+" moeda(s) de R$ "+str("%.2f" % vmoedas[val]))
