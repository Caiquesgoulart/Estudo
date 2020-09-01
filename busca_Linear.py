import time

array = [10, 8, 15, 20, 2, 64, 17, 40, 78, 3, 14, 96, 34]

print('Numeros na lista: ', array)
buscar = int(input('Entre com um numero: '))
achou = False
for i in range(len(array)):
    if array[i] == buscar:
        achou = True
        print('Termo ', buscar, ' encontrado na posição:  ', i)
        break
if achou == False:
    print('Termo ', buscar, ' não existe')

ms = time.time() // 1000000
print('Tempo levado: ', ms, ' milissegundos')

print('Enter pra fechar...')
input()