from collections import deque

def missionaries_cannibals():
    start = (3, 3, 0)   # (Missionaries, Cannibals, Boat side 0=Left,1=Right)
    goal = (0, 0, 1)
    q = deque([(start, [])])
    visited = {start}

    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    while q:
        (m, c, b), path = q.popleft()

        if (m, c, b) == goal:
            for step in path + [(m, c, b)]:
                print(step)
            return

        for dm, dc in moves:
            if b == 0:
                nm, nc, nb = m-dm, c-dc, 1
            else:
                nm, nc, nb = m+dm, c+dc, 0

            if 0 <= nm <= 3 and 0 <= nc <= 3:
                if (nm == 0 or nm >= nc) and (3-nm == 0 or 3-nm >= 3-nc):
                    state = (nm, nc, nb)
                    if state not in visited:
                        visited.add(state)
                        q.append((state, path + [(m, c, b)]))

missionaries_cannibals()
from collections import deque

def missionaries_cannibals():
    start = (3, 3, 0)   # (Missionaries, Cannibals, Boat side 0=Left,1=Right)
    goal = (0, 0, 1)
    q = deque([(start, [])])
    visited = {start}

    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    while q:
        (m, c, b), path = q.popleft()

        if (m, c, b) == goal:
            for step in path + [(m, c, b)]:
                print(step)
            return

        for dm, dc in moves:
            if b == 0:
                nm, nc, nb = m-dm, c-dc, 1
            else:
                nm, nc, nb = m+dm, c+dc, 0

            if 0 <= nm <= 3 and 0 <= nc <= 3:
                if (nm == 0 or nm >= nc) and (3-nm == 0 or 3-nm >= 3-nc):
                    state = (nm, nc, nb)
                    if state not in visited:
                        visited.add(state)
                        q.append((state, path + [(m, c, b)]))

missionaries_cannibals()
