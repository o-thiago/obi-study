"""
Duas amigas estão na fila para comprar ingressos para uma sessão de cinema.
O preço dos ingressos, em Reais, é dado na tabela abaixo:

Idade Preço
até 17 anos 15
18 a 59 anos 30
60 anos ou mais 20

Dadas as idades das amigas, escreva um programa para calcular o total a ser
pago pelos dois ingressos
"""


def get_total_cost(age: int):
    if age < 18:
        return 15
    elif age < 60:
        return 30
    else:
        return 20


def solve(ages: list[int]):
    all_costs = map(get_total_cost, ages)
    total_cost = sum(all_costs)

    return total_cost


if __name__ == "__main__":
    ages = list(map(int, [input() for _ in range(2)]))

    print(solve(ages))
