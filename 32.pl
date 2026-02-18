% 1. Check if two lists are exactly same
same_list([], []).
same_list([H|T1], [H|T2]) :-
    same_list(T1, T2).
