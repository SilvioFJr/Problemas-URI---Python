x = input().split()
x0 = int(x[0])
x1 = int(x[1])
x2 = int(x[2])
lista = [x0, x1, x2]
list.sort(lista)

for i in lista:
    print(i)

print()

for n in range(3):
    print(x[n])
