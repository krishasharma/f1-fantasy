'''
f1 fantasy team 
-------------------------------------------------------------
choose the best f1 fantsy team based on the knapsack optimixation problem.
The knapsack problem is a problem in combinatorial optimization 
Given a set of items, each with a weight and a value, determine the number of 
each item to include in a collection so that the total weight is less than or 
equal to a given limit and the total value is as large as possible.
'''

class Driver:
    def __init__(self, name, cost, points):
        self.name = name
        self.cost = cost
        self.points = points

def knapsack_problem(drivers, budget):
    n = len(drivers)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if drivers[i - 1].cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - drivers[i - 1].cost] + drivers[i - 1].points)
            else:
                dp[i][j] = dp[i - 1][j]

    selected_drivers = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_drivers.append(drivers[i - 1])
            j -= drivers[i - 1].cost

    return selected_drivers

def main():
    # Gather data
    drivers = [
        Driver("Driver1", 10, 50),
        Driver("Driver2", 20, 70),
        # Add more drivers with their costs and points
    ]
    budget = 30

    # Solve knapsack problem
    selected_team = knapsack_problem(drivers, budget)

    # Output selected team
    total_points = sum(driver.points for driver in selected_team)
    total_cost = sum(driver.cost for driver in selected_team)
    print("Selected Team:")
    for driver in selected_team:
        print(f"{driver.name}: Cost - {driver.cost}, Points - {driver.points}")
    print(f"Total Cost: {total_cost}, Total Points: {total_points}")

if __name__ == "__main__":
    main()