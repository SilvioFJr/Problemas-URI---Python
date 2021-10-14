# Média 3 ... 1040

x = input().split()

x0 = round(float(x[0]), 1)
x1 = round(float(x[1]), 1)
x2 = round(float(x[2]), 1)
x3 = round(float(x[3]), 1)

med = (x0*2.0+x1*3.0+x2*4.0+x3)/float(2+3+4+1)

if med >= 7.0:
    print('Media: {:.1f}'.format(med))
    print('Aluno aprovado.')
elif med < 5.0:
    print('Media: {:.1f}'.format(med))
    print('Aluno reprovado.')
elif med >= 5.0 and med < 6.9:
    print('Media: {:.1f}'.format(med))
    print('Aluno em exame.')
    ex = input()
    print('Nota do exame: {:.1f}'.format(float(ex)))
    med2 = (med+float(ex))/2.0
    if med2 >= 5.0:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(med2))
    elif med2 <= 4.9:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(med2))
