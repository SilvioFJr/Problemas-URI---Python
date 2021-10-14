# Lanche ... 1038

x = input().split()

x0 = int(x[0])  # código
x1 = int(x[1])  # quantidade

if x0 == 1:
    print('Total: R$ {:.2f}'.format(float(x1)*4.00))
elif x0 == 2:
    print('Total: R$ {:.2f}'.format(float(x1)*4.50))
elif x0 == 3:
    print('Total: R$ {:.2f}'.format(float(x1)*5.00))
elif x0 == 4:
    print('Total: R$ {:.2f}'.format(float(x1)*2.00))
elif x0 == 5:
    print('Total: R$ {:.2f}'.format(float(x1)*1.50))
