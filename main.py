from pythonds import PriorityQueue


fila = PriorityQueue()

status = True


def colocar():

    operacoes = input().split()


while status:
    comando = input().split()
    if comando[0] == 'enqueue':

        for _ in range(int(comando[1])):
            colocar()
