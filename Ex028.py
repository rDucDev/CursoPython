#Jogo da Adivinhação

import random
lista = [1,2,3,4,5,6]
npc = random.choice(lista)
npessoa = int(input('Escolha o mesmo numero que eu! (entre 1 e 6): '))
print('PROCESSANDO...')
from time import sleep
sleep(2) #ESPERA

print('O PC escolheu {}.'.format(npc))
print('Você escolheu {}'.format(npessoa))

if npc == npessoa:
    print('Caraio escolhemos o mesmo')
else: print('ERROUUU')

