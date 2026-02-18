# Map Coloring using CSP (Backtracking)

# States of Australia
states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

# Neighbouring states (constraints)
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':  ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Function to check if assignment is valid
def is_valid(state, color, assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking function
def backtrack(assignment):
    if len(assignment) == len(states):
        return assignment
    
    for state in states:
        if state not in assignment:
            for color in colors:
                if is_valid(state, color, assignment):
                    assignment[state] = color
                    result = backtrack(assignment)
                    if result:
                        return result
                    del assignment[state]
            return None

# Solve the CSP
solution = backtrack({})

# Print solution
if solution:
    print("Solution Found:")
    for state in solution:
        print(state, "->", solution[state])
else:
    print("No Solution")
