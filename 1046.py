#Tempo de Jogo

x=input().split()

x0 = int(x[0])
x1 = int(x[1])

# Duração em horas; o jogo dura no mínimo 1 h e no máximo 24 h
dur = (x1 - x0) % 24 or 24


print('O JOGO DUROU {} HORA(S)'.format(dur))