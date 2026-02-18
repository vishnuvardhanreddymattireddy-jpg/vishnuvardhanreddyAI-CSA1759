% Facts
bird(sparrow).
bird(pigeon).
bird(ostrich).
bird(penguin).

% Birds that cannot fly
cannot_fly(ostrich).
cannot_fly(penguin).

% Rule
can_fly(X) :-
    bird(X),
    \+ cannot_fly(X).
