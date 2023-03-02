#Calculo de ano bissesto

print('Este programa calcula se o ano informado é bissexto ou não!!')
ano = int(input('Insira um ano: '))
dif = ano % 4

if dif > 0:
    print('{} NÃO É ANO BISSEXTO!!!'.format(ano))
else: print('{} É UM ANO BISSEXTO :)'.format(ano))