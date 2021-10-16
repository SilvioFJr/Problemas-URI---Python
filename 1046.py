#Tempo de Jogo

x=input().split()

x0 = int(x[0])
x1 = int(x[1])

dur=0
aux=x0
if x0==x1:
    dur=24
else:
    while aux != x1:
        if aux == 24:
            aux=0
        else:
            aux+=1
            dur+=1


print('O JOGO DUROU {} HORA(S)'.format(dur))