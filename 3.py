from collections import deque

def water_jug_problem(jug1_cap, jug2_cap, target):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (a, b), path = queue.popleft()

        if a == target and b == 0:
            print("Steps to reach (2, 0):\n")
            for step in path:
                print(step)
            return

        moves = [
            (jug1_cap, b),                      # Fill jug1
            (a, jug2_cap),                      # Fill jug2
            (0, b),                             # Empty jug1
            (a, 0),                             # Empty jug2
            (a - min(a, jug2_cap - b),
             b + min(a, jug2_cap - b)),         # Pour jug1 → jug2
            (a + min(b, jug1_cap - a),
             b - min(b, jug1_cap - a))          # Pour jug2 → jug1
        ]

        for state in moves:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    print("No solution found")

# MAIN
water_jug_problem(4, 3, 2)
