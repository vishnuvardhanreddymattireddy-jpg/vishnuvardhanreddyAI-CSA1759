% Initial Facts
fact(raining).
fact(cloudy).

% Rules
fact(wet_ground) :-
    fact(raining).

fact(carry_umbrella) :-
    fact(raining).

fact(stay_home) :-
    fact(wet_ground),
    fact(cloudy).
