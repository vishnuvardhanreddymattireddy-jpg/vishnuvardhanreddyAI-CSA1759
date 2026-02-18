% State: state(MonkeyPosition, MonkeyStatus, BoxPosition, HasBanana)

% Monkey walks
move(state(X, on_floor, B, H),
     state(Y, on_floor, B, H)) :-
    X \= Y.

% Monkey pushes box
move(state(X, on_floor, X, H),
     state(Y, on_floor, Y, H)) :-
    X \= Y.

% Monkey climbs box
move(state(X, on_floor, X, H),
     state(X, on_box, X, H)).

% Monkey grabs banana
move(state(middle, on_box, middle, no),
     state(middle, on_box, middle, yes)).

% Goal state
goal(state(_, _, _, yes)).

% Main predicate
canget(State) :-
    dfs(State, []).

% DFS with visited list
dfs(State, _) :-
    goal(State),
    write('Monkey got the banana!'), nl.

dfs(State, Visited) :-
    move(State, Next),
    \+ member(Next, Visited),
    dfs(Next, [State|Visited]).
