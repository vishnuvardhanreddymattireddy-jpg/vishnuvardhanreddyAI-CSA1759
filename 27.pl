% Graph edges with cost (heuristic value)

edge(a, b, 4).
edge(a, c, 2).
edge(b, d, 5).
edge(c, d, 1).

% Best First Search
best_first(Start, Goal) :-
    edge(Start, Goal, _),
    write('Reached Goal'), nl.

best_first(Start, Goal) :-
    edge(Start, Next, _),
    best_first(Next, Goal).
