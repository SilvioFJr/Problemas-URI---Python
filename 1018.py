# Cédulas...1018


x = int(input())  # 270
valores = [100, 50, 20, 10, 5, 2, 1]  # Valores de notas disponíveis

print(x)
for val in range(7):
    quociente = x//valores[val]
    x -= quociente*valores[val]  # 70

    print(str(quociente)+' nota(s) de R$', str(valores[val])+',00')
