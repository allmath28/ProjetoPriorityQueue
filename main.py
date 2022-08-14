from queue import PriorityQueue
import re

fila = PriorityQueue(maxsize=0)

status = True
cont = 0


def colocar():
    """Função para colocar na fila os processos"""
    operacoes = input().split()
    fila.put((operacoes[0], operacoes[1:]))


def scramble(itens):
    # Código para o comando scramble

    texto = itens

    contador = 0
    linha = ''

    for i in texto:
        if i == '(':
            contador += 1
        elif i == ')' and contador:
            contador -= contador
        elif not contador:
            linha += i

    check = re.findall('\(([\w~_#&*]+)|([\w~_#&*]+)\)', texto)

    linha = list(linha)

    for i in check:
        linha.insert(0, ''.join(i))

    linha = ''.join(linha)
    linha = linha.replace(")", "")
    linha = linha.replace(' ', '')

    if len(linha) > 0:
        print(linha)
    else:
        pass


def dekey(itens):
    # Código para o comando dekey
    contador = itens[0]
    lista = itens[1:]
    for i in range(contador):
        a = lista[0]
        b = lista[1]

        if a < b:
            lista[0] = b
            lista[1:len(lista) + 1] = lista[2:len(lista) + 1]
            lista.append(a)
        else:
            lista[0] = a
            lista[1:len(lista) + 1] = lista[2:len(lista) + 1]
            lista.append(b)
    print(''.join(map(str, lista)))


def go():
    item = fila.get()

    if item[1][0] == 'scramble':
        # Criação da string para manipulação pelo Scramble
        string = item[1][1:]
        string = ''.join(string)
        scramble(string)  # Chamada da função Scrumble

    elif item[1][0] == 'dekey':

        lista = item[1][1:]
        lista = list(map(int, lista))
        dekey(lista)


def stop():
    print(f'{fila.qsize()} processo(s) órfão(s).')


while status:
    comando = input().split()
    if comando[0] == 'enqueue':

        cont = int(comando[1])
        for _ in range(cont):
            colocar()

    elif comando[0] == 'go' and fila.qsize() > 0:
        go()

    elif comando[0] == 'stop':
        status = False
        stop()
