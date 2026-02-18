% Tower of Hanoi Program

% Base case: If there is only one disk
hanoi(1, Source, Destination, _) :-
    write('Move disk 1 from '),
    write(Source),
    write(' to '),
    write(Destination), nl.

% Recursive case
hanoi(N, Source, Destination, Auxiliary) :-
    N > 1,
    M is N - 1,
    
    % Step 1: Move N-1 disks from Source to Auxiliary
    hanoi(M, Source, Auxiliary, Destination),
    
    % Step 2: Move largest disk to Destination
    write('Move disk '),
    write(N),
    write(' from '),
    write(Source),
    write(' to '),
    write(Destination), nl,
    
    % Step 3: Move N-1 disks from Auxiliary to Destination
    hanoi(M, Auxiliary, Destination, Source).
