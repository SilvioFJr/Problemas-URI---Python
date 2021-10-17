#Aumento de Salário

x=round(float(input()),2)
xnew=0

if x>=0 and x<=400.00:
    xnew=x+x*0.15
    print('Novo salario: {:.2f}'.format(xnew))
    print('Reajuste ganho: {:.2f}'.format(x*0.15))
    print('Em percentual: 15 %')
elif x>=400.01 and x<=800.00:
    xnew=x+x*0.12
    print('Novo salario: {:.2f}'.format(xnew))
    print('Reajuste ganho: {:.2f}'.format(x*0.12))
    print('Em percentual: 12 %')
elif x>=800.01 and x<=1200.00:
    xnew=x+x*0.10
    print('Novo salario: {:.2f}'.format(xnew))
    print('Reajuste ganho: {:.2f}'.format(x*0.10))
    print('Em percentual: 10 %')
elif x>=1200.01 and x<=2000.00:
    xnew=x+x*0.07
    print('Novo salario: {:.2f}'.format(xnew))
    print('Reajuste ganho: {:.2f}'.format(x*0.07))
    print('Em percentual: 7 %')
elif x>2000.00:
    xnew=x+x*0.04
    print('Novo salario: {:.2f}'.format(xnew))
    print('Reajuste ganho: {:.2f}'.format(x*0.04))
    print('Em percentual: 4 %')

    