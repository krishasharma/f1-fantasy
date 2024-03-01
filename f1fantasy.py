class Driver:
    def __init__(self, name, team, cost, points):
        self.name = name
        self.team = team
        self.cost = cost
        self.points = points

def knapsack_problem(drivers, budget):
    n = len(drivers)
    budget = int(budget)  # Convert budget to an integer
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if drivers[i - 1].cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - drivers[i - 1].cost] + drivers[i - 1].points)

    selected_drivers = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_drivers.append(drivers[i - 1])
            j -= int(drivers[i - 1].cost)

    return selected_drivers

def main():
    # Gather data
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
        {"name": "Max Verstappen", "team": "Red Bull", "cost": 30.0, "points": 575},
        {"name": "Sergio Perez", "team": "Red Bull", "cost": 20.8, "points": 285},
        {"name": "Lewis Hamilton", "team": "Mercedes", "cost": 19.3, "points": 234},
        {"name": "Fernando Alonso", "team": "Aston Martin", "cost": 15.8, "points": 206},
        {"name": "Charles Leclerc", "team": "Ferrari", "cost": 19.1, "points": 206},
        {"name": "Lando Norris", "team": "McLaren", "cost": 23.0, "points": 205},
        {"name": "Carlos Sainz Jr.", "team": "Ferrari", "cost": 18.5, "points": 200},
        {"name": "George Russell", "team": "Mercedes", "cost": 18.8, "points": 175},
        {"name": "Oscar Piastri", "team": "McLaren", "cost": 19.0, "points": 97},
        {"name": "Lance Stroll", "team": "Aston Martin", "cost": 10.7, "points": 74},
        {"name": "Daniel Ricciardo", "team": "RB", "cost": 9.0, "points": 6},
        {"name": "Yuki Tsunoda", "team": "RB", "cost": 8.0, "points": 17},
        {"name": "Pierre Gasly", "team": "Alpine", "cost": 7.8, "points": 62},
        {"name": "Esteban Ocon", "team": "Alpine", "cost": 7.8, "points": 58},
        {"name": "Alexander Albon", "team": "Williams", "cost": 7.0, "points": 27},
        {"name": "Zhou Guanyu", "team": "Sauber", "cost": 6.6, "points": 6},
        {"name": "Valtteri Bottas", "team": "Sauber", "cost": 6.4, "points": 10},
        {"name": "Nico Hulkenberg", "team": "Haas", "cost": 6.4, "points": 9},
        {"name": "Kevin Magnussen", "team": "Haas", "cost": 6.2, "points": 3},
        {"name": "Logan Sargeant", "team": "Williams", "cost": 5.5, "points": 1}
    ]

    # Adjust the driver costs based on team costs
    for driver in drivers_data:
        team_cost = team_costs.get(driver["team"], 0)
        driver["cost"] += team_cost

    # Define the budget for drivers and constructors
    total_budget = 100.0
    driver_budget = total_budget * 0.6
    constructor_budget = total_budget * 0.4

    # Calculate remaining budget for constructor teams
    remaining_constructor_budget = constructor_budget - sum(team_costs.values())
    remaining_constructor_budget_per_team = remaining_constructor_budget / 2

    # Create Driver objects
    drivers = [Driver(driver["name"], driver["team"], int(driver["cost"]), driver["points"]) for driver in drivers_data]

    # Solve knapsack problem for selecting drivers
    selected_drivers = knapsack_problem(drivers, int(driver_budget))  # Convert driver_budget to an integer

    # Output selected drivers
    print("Selected Drivers:")
    driver_counter = 0
    for driver in selected_drivers:
        if driver_counter >= 5:  # Check if the maximum number of drivers has been reached
            break
        print(f"{driver.name} ({driver.team}): Cost - {driver.cost}, Points - {driver.points}")
        driver_counter += 1

    # Allocate remaining budget to constructor teams
    print("\nSelected Constructor Teams:")
    team_counter = 0
    for team, cost in team_costs.items():
        if team_counter >= 2:  # Check if the maximum number of teams has been reached
            break
        if cost <= remaining_constructor_budget_per_team:
            print(f"{team}: Cost - {cost}")
            remaining_constructor_budget_per_team -= cost
            team_counter += 1

    print("\nTotal drivers selected:", min(driver_counter, 5))  # Ensure the driver count does not exceed 5
    print("Total teams selected:", min(team_counter, 2))  # Ensure the team count does not exceed 2

if __name__ == "__main__":
    main()