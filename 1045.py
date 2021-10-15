#Tipos de Triângulos

x=input().split()

a=float(x[0])
b=float(x[1])
c=float(x[2])

lista=[a,b,c]
lista.sort(reverse=True)
a=lista[0]
b=lista[1]
c=lista[2]

#print(lista, type(a), b, c)

if (a>=(b+c)):
    print('NAO FORMA TRIANGULO')
else:
    if ((a**2)==((b**2)+(c**2))):
        print('TRIANGULO RETANGULO')
    else:
        pass

    if ((a**2)>((b**2)+(c**2))):
        print('TRIANGULO OBTUSANGULO')
    else:
        pass

    if ((a**2)<((b**2)+(c**2))):
        print('TRIANGULO ACUTANGULO')
    else:
        pass

    if (a==b==c):
        print('TRIANGULO EQUILATERO')
    else:
        pass

    if ((a==b!=c)or(a==c!=b)or(b==c!=a)):
        print('TRIANGULO ISOSCELES')
    else:
        pass
