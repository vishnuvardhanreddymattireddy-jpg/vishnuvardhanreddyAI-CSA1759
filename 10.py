def a_star(graph, start, goal, h):
    open_list = {start}
    closed_list = set()
    g = {start: 0}
    parent = {start: None}

    while open_list:
        n = min(open_list, key=lambda x: g[x] + h[x])

        if n == goal:
            path = []
            while n:
                path.append(n)
                n = parent[n]
            print("Path:", path[::-1])
            return

        open_list.remove(n)
        closed_list.add(n)

        for m, cost in graph[n]:
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parent[m] = n
                g[m] = g[n] + cost

    print("Path not found")

# Graph and heuristic
graph = {
    'A': [('B',1), ('C',3)],
    'B': [('D',1)],
    'C': [('D',1)],
    'D': []
}

h = {'A':3, 'B':2, 'C':1, 'D':0}

a_star(graph, 'A', 'D', h)
