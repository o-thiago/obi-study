
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
