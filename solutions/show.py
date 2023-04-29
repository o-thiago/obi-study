"""
Um grupo de amigos quer comprar ingressos para um show da sua banda preferida.
O show acontece num teatro que tem N filas de assentos, cada fila com M
assentos. Os amigos querem comprar ingressos de forma que os assentos dos
amigos:
• sejam todos na mesma fila,
• sejam contíguos (ou seja, um vizinho ao outro) e
• sejam na fila mais próxima possível do palco.
Dado um mapa descrevendo os assentos disponíveis, ajude os amigos a encontrarem
os ingressos de acordo com as condições acima
"""


def is_seat_empty(seat: int) -> bool:
    return seat == 0


def solve(people_amount: int, show_matrix: list[list[int]]):
    for i, row in enumerate(show_matrix):
        consecutives = 0

        for seat in row:
            if is_seat_empty(seat):
                consecutives += 1
            else:
                consecutives = 0

        if consecutives >= people_amount:
            return i + 1

    return -1


if __name__ == "__main__":
    friends_amount, rows_amount, _ = map(int, input().strip().split(" "))
    show_matrix = [list(map(int, input().strip().split(" ")))
                   for _ in range(rows_amount)]

    print(solve(friends_amount, show_matrix))
