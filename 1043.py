# Triângulo 1043

x = input().split()

a = float(x[0])
b = float(x[1])
c = float(x[2])

# Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra: 
# um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e 
# menor que a soma dos outros dois lados.

if ((a> abs(b-c)) and (a<(b+c))):
    print('Perimetro = {:.1f}'.format(a+b+c))
else:
    print('Area = {:.1f}'.format(((a+b)*c)/float(2)))
