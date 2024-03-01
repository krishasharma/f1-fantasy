class Driver:
    def __init__(self, name, team, cost, points):
        self.name = name
        self.team = team
        self.cost = cost
        self.points = points

def knapsack_problem(drivers, budget):
    n = len(drivers)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if drivers[i - 1].cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - int(drivers[i - 1].cost)] + drivers[i - 1].points)
    selected_drivers = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_drivers.append(drivers[i - 1])
            j -= int(drivers[i - 1].cost)
    return selected_drivers

def main():
    team_costs = {
        "Red Bull": 27.9,
        "McLaren": 23.2,
        "Mercedes": 20.1,
        "Ferrari": 19.3,
        "Aston Martin": 13.6,
        "RB": 8.5,
        "Alpine": 8.4,
        "Sauber": 6.6,
        "Williams": 6.3,
        "Haas": 6.3
    }

    drivers_data = [
        ["Max Verstappen", "Red Bull", 30.0, 575],
        ["Sergio Perez", "Red Bull", 20.8, 285],
        ["Lewis Hamilton", "Mercedes", 19.3, 234],
        ["Fernando Alonso", "Aston Martin", 15.8, 206],
        ["Charles Leclerc", "Ferrari", 19.1, 206],
        ["Lando Norris", "McLaren", 23.0, 205],
        ["Carlos Sainz Jr.", "Ferrari", 18.5, 200],
        ["George Russell", "Mercedes", 18.8, 175],
        ["Oscar Piastri", "McLaren", 19.0, 97],
        ["Lance Stroll", "Aston Martin", 10.7, 74],
        ["Daniel Ricciardo", "RB", 9.0, 6],
        ["Yuki Tsunoda", "RB", 8.0, 17],
        ["Pierre Gasly", "Alpine", 7.8, 62],
        ["Esteban Ocon", "Alpine", 7.8, 58],
        ["Alexander Albon", "Williams", 7.0, 27],
        ["Zhou Guanyu", "Sauber", 6.6, 6],
        ["Valtteri Bottas", "Sauber", 6.4, 10],
        ["Nico Hulkenberg", "Haas", 6.4, 9],
        ["Kevin Magnussen", "Haas", 6.2, 3],
        ["Logan Sargeant", "Williams", 5.5, 1]
    ]

    drivers = [Driver(*data) for data in drivers_data]

    total_budget = 100.0
    driver_budget = total_budget * 0.6

    selected_drivers = knapsack_problem(drivers, int(driver_budget))

    print("Selected Drivers:")
    for driver in selected_drivers:
        print(f"{driver.name} ({driver.team}): Cost - {driver.cost}, Points - {driver.points}")

if __name__ == "__main__":
    main()