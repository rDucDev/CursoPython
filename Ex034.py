#Calculo de aumento de salário

sal = float(input('Insira o salário: '))

if sal > 1250:
    aumento = sal*1.15
else:
    aumento = sal*1.1
print('Salário de {:.2f} vai para {:.2f}.'.format(sal,aumento))