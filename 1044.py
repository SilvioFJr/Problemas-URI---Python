#Múltiplos

x=input().split()

x0=int(x[0])
x1=int(x[1])

'''Para verificar se um número é múltiplo de outro, basta encontrar um número 
inteiro de modo que a multiplicação entre eles resulte no primeiro número.
m=n*k'''
if x0<x1:
    aux=x0
    x0=x1
    x1=aux
else:
    pass

if (x0%x1==0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')

