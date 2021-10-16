#Tempo de Jogo com Minutos

x=input().split()

hi=int(x[0]) #Hora inicial
mi=int(x[1]) #minuto inicial
hf=int(x[2]) #Hora final
mf=int(x[3]) #minuto final

dur_h=dur_m=0

auxi=hi*60+mi
auxf=hf*60+mf
if auxi == auxf:
    dur_h=24
elif auxf<auxi:
    tot_m=1440-auxi+auxf
    dur_h=int(tot_m/60)
    dur_m=tot_m-dur_h*60
else:
    tot_m=auxf-auxi
    dur_h=int(tot_m/60)
    dur_m=tot_m-dur_h*60

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(dur_h,dur_m))
