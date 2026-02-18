% Check vowel
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

% Count vowels
count_vowels([], 0).
count_vowels([H|T], N) :-
    vowel(H),
    count_vowels(T, N1),
    N is N1 + 1.

count_vowels([H|T], N) :-
    \+ vowel(H),
    count_vowels(T, N).
