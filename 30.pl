% Facts
parent(john, mary).
parent(mary, sam).

% Rule
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).
