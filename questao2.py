primeiro_num = int(input('Digite 1ª valor: '))
segundo_num = int(input('Digite 2ª valor: '))
maior = 0
diferenca = 0
diferenca_anterior = 0
primeiro_ant = 0
segundo_ant = 0
contador = 1
num_par = 0

while (primeiro_num != 0 and segundo_num != 0) :
    diferenca = abs(primeiro_num - segundo_num)
    if diferenca > diferenca_anterior :
        maior = diferenca
        num_par = contador
        primeiro_ant = primeiro_num
        segundo_ant = segundo_num
        contador += 1

    primeiro_num = int(input('Digite 1ª valor: '))
    segundo_num = int(input('Digite 2ª valor: '))

print('Maior diferença: ', maior, ' ', num_par, 'ª', ' ', '( ', primeiro_ant, ' ', segundo_ant, ')')
