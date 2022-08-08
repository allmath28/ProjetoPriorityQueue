from queue import PriorityQueue

fila = PriorityQueue(maxsize=0)

status = True


def colocar():
    """Função para colocar na fila os processos"""
    operacoes = input().split()
    fila.put((operacoes[0], operacoes[1:]))


def scramble(itens):
    # Código para o comando scramble
    print('foi scramble')


def dekey(itens):
    # Código para o comando dekey
    print('foi dekey')


def go():
    item = fila.get()

    if item[1][0] == 'scramble':
        scramble(item[1])
    elif item[1][0] == 'dekey':
        dekey(item[1])


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

