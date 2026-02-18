# Alpha-Beta Pruning Example

import math

# Alpha-Beta function
def alphabeta(depth, node, maximizing, values, alpha, beta):

    # Leaf node condition
    if depth == 3:
        return values[node]

    if maximizing:
        best = -math.inf
        for i in range(2):
            val = alphabeta(depth+1, node*2+i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:   # Beta cut-off
                break
        return best

    else:
        best = math.inf
        for i in range(2):
            val = alphabeta(depth+1, node*2+i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:   # Alpha cut-off
                break
        return best


# Leaf node values (8 leaf nodes)
values = [3, 5, 6, 9, 1, 2, 0, -1]

result = alphabeta(0, 0, True, values, -math.inf, math.inf)

print("Optimal Value:", result)
