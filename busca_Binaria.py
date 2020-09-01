# ALGORITMO DE BUSCA BINÁRIA EM PYTHON 
# Este é um algoritmo de busca binária criado em Python, além da busca ele também marca a posição do elemento e o tempo decorrido.

import time

def busca_binaria(array, buscar):
    i = 0
    f = len(array) - 1
    meio = 0
    while i <= f:
        meio = (f + i) // 2
        if array[meio] < buscar:
            i = meio + 1
        elif array[meio] > buscar:
            f = meio - 1
        else:
            return meio

    return -1


array = [1, 5, 8, 15, 27, 30, 45, 67, 75, 84, 97, 108, 117, 123, 134]
print('', array)

buscar = int(input('Entre com um numero: '))
posicao = busca_binaria(array, buscar)

if posicao != -1:
    print('Elemento ', buscar, ' encontrado na posição: ', posicao)
else:
    print('Elemento ', buscar, ' não existe')

tempo = time.time() // 1000000
print('Tempo levado: ', tempo, ' milissegundos')

print('Enter pra fechar...')
input()
