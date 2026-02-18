% Facts
male(john).
male(paul).
female(mary).
female(linda).

parent(john, paul).
parent(mary, paul).
parent(paul, linda).

% Rules
father(X,Y) :- male(X), parent(X,Y).
mother(X,Y) :- female(X), parent(X,Y).

grandparent(X,Y) :-
    parent(X,Z),
    parent(Z,Y).
