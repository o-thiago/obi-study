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
