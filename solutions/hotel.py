"""
O hotel da Colônia de Férias dos Professores está com uma promoção para as férias de julho. A
promoção é válida para quem chegar a partir do dia 1 de julho e sair no dia 1 de agosto.
O preço da diária do hotel é menor para quem chegar mais cedo, e vai aumentando a cada dia. Mais
precisamente, a promoção funciona assim:
• A diária do hotel para cada quem chegar no dia 1 é D Reais. Assim, quem chegar no dia 1
vai pagar um total de 31 × D Reais.
• A diária do hotel aumenta A reais por dia. Ou seja, a diária é D + A Reais para quem chegar
no dia 2; D + 2 × A Reais no dia 3; D + 3 × A Reais no dia 4 e assim por diante.
• A partir do dia 16 a diária não aumenta mais.
Note que quem chegar no dia 2 vai pagar um total de 30 × (D + A) reais; quem chegar no dia 3
vai pagar um total de 29 × (D + 2 × A) reais, e assim por diante.
Bruno gosta muito da professora Vilma, e para agradá-la quer ajudá-la a planejar suas férias, escre-
vendo um programa para calcular o total (em Reais) que a professora Vilma vai gastar, dependendo
do dia em que chegar no hotel.
"""

def solve(daily_cost: int, daily_increase: int, day_arrived: int):
    increase_by = (min(15, day_arrived) - 1) * daily_increase
    effective_daily_cost = daily_cost + increase_by

    days_paying = (31 + 1) - day_arrived

    return effective_daily_cost * days_paying


if __name__ == "__main__":
    daily_cost = int(input())
    daily_increase = int(input())
    day_arrived = int(input())

    print(solve(daily_cost, daily_increase, day_arrived))
