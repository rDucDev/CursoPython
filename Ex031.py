#Preço da passagem

km = int(input('Essa viagem terá Qts KM de distancia?? '))
print(km)
if km > 200:
    preco = km*0.5
else:
    preco = km*0.45
print('Preço da viagem de {}km será de R${:.2f}'.format(km,preco))
