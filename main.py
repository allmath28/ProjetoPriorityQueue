from queue import PriorityQueue

fila = PriorityQueue(maxsize=0)

status = True


def colocar():
    """Função para colocar na fila os processos"""
    operacoes = input().split()
    fila.put((operacoes[0], operacoes[1:]))


def scramble(itens):
    # Código para o comando scramble

    print(itens)


def dekey(itens):
    # Código para o comando dekey
    contador = itens[0]
    lista = itens[1:]
    for i in range(contador):
        a = lista[0]
        b = lista[1]
        if a > b:
            lista[0] = a
            lista[1:len(lista)+1] = lista[2:len(lista)+1]
            lista.append(b)
        elif a < b:
            lista[0] = b
            lista[1:len(lista) + 1] = lista[2:len(lista) + 1]
            lista.append(a)
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

        for _ in range(int(comando[1])):
            colocar()

    elif comando[0] == 'go':
        go()

    elif comando[0] == 'stop':
        status = False
        stop()
