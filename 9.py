# Travelling Salesman Problem (Brute Force)

from itertools import permutations

def tsp(graph, start):
    cities = list(range(len(graph)))
    cities.remove(start)

    min_cost = float('inf')
    best_path = []

    for path in permutations(cities):
        cost = graph[start][path[0]]
        for i in range(len(path) - 1):
            cost += graph[path[i]][path[i+1]]
        cost += graph[path[-1]][start]

        if cost < min_cost:
            min_cost = cost
            best_path = [start] + list(path) + [start]

    print("Minimum Cost:", min_cost)
    print("Path:", best_path)


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp(graph, 0)
