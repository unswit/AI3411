/*
    This is the first assignment of COMP3411 T1,
    mainly prolog questions.

    Yiheng Quan Z5098268
*/

% --- Q1 ---

% Handle nothing or one element
sumsq_even([], 0).
% Loop through the list and sum the square of even numbers
sumsq_even([H|T], EvenSum) :-
    sumsq_even(T, Sum),
    0 is H mod 2,
    EvenSum is H * H + Sum.
sumsq_even([H|T], Sum) :-
    sumsq_even(T, Sum),
    1 is H mod 2.

% --- Q2 ---

% P1 is an ancestor of P2
ancestor(P1, P2) :-
    parent(P1, P2).
ancestor(P1, P2) :-
    parent(P1, Child),
    ancestor(Child, P2).

% Same person same name
same_name(P, P).
% Same male ancestor
same_name(P1, P2) :-
    ancestor(A, P1),
    ancestor(A, P2),
    male(A).
% Ancestor of C
same_name(P, C) :-
    ancestor(P, C),
    male(P).
same_name(C, P) :-
    ancestor(P, C),
    male(P).

% --- Q3 ---

% Empty list
sqrt_list([], []).
% One or more elements
sqrt_list([H | T], [[H, S] | R]) :-
    % negative sqrt is not valid
    H >= 0, S is sqrt(H),
    sqrt_list(T, R).

% --- Q4 ---
% my own append function (I cannot think of another method)
my_append([], N, [N]).
my_append([H | T], N, [H | R]) :- 
    my_append(T, N, R).

% get the last element from a list
last_list([], []).
last_list([L], L).
last_list([_ | T], R) :-
    last_list(T, R).

% check if same sign (all positive or all negative)
same_sign(X, Y) :- X >= 0, Y >= 0.
same_sign(X, Y) :- X < 0, Y < 0.

% Empty list
sign_runs([], []).
sign_runs([X], [X]).
sign_runs(L, R) :- sign_runs_temp(L, R, []).
sign_runs_temp([F, S | T], C, [F | R]) :-
    F >= 0, S >= 0,
    sign_runs_temp([S | T], C, R).
sign_runs_temp([F, S | T], C, [F | R]) :-
    F < 0, S < 0,
    sign_runs_temp([S | T], C, R).
% When to split and when to merge
sign_runs_temp([F, S | T], [R | L], R) :-
    F >= 0, S < 0,
    sign_runs_temp([S | T], L, []).
sign_runs_temp([F, S | T], [R | L], R) :-
    F < 0, S >= 0,
    sign_runs_temp([S | T], L, []).

test([], [], []).
test([X], [], [X]).
test([F, S | T], A, [F | R]) :-
    F >= 0,
    test([S | T], A, R).
test([F, S | T], [F | R], A) :-
    F < 0,
    test([S | T], R, A).

% --- Q5 ---

% Binary Tree
empty().
tree(L, Num, R).