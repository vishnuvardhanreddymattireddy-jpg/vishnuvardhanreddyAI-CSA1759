# Vacuum Cleaner Problem

def vacuum_cleaner(room, state):
    print("Initial State:", state)

    if state[room] == 1:
        state[room] = 0
        print(f"Cleaned Room {room}")

    other = 'B' if room == 'A' else 'A'
    if state[other] == 1:
        state[other] = 0
        print(f"Moved to Room {other} and Cleaned")

    print("Final State:", state)


# 1 = Dirty, 0 = Clean
state = {'A': 1, 'B': 1}
vacuum_cleaner('A', state)
