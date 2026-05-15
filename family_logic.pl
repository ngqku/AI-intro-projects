% ---FACTS---
% parent(parent, child).
parent(albert, francis).
parent(albert, patrick).
parent(albert, jacinta).
parent(albert, martha).
parent(mary, francis).
parent(mary, patrick).
parent(mary, jacinta).
parent(mary, martha).
parent(francis,sam).
parent(francis, fridah).
parent(patrick,precious).
parent(patrick, immaculate).
parent(jacinta, charlene).
parent(martha, rachel).


% gender(person)
male(albert).
male(patrick).
male(francis).
male(sam).
female(fridah).
female(precious).
female(immaculate).
female(charlene).
female(rachel).
female(mary).
female(jacinta).
female(martha).

% ----RULES----
grandfather(X,Z) :-parent(X,Y) ,parent(Y,Z), male(X).
grandmother(X,Z) :- parent(X,Y), parent(Y,Z), female(X).
grandparent(GP, GC) :- grandfather(GP, GC).
grandparent(GP, GC) :- grandmother(GP, GC).

husband(X,Y):- parent(X,Z), parent(Y,Z) , male(X).
wife(X,Y):- parent(X,Z), parent(Y,Z) , female(X).

sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
brother(X,Y) :- sibling(X,Y), male(X).
sister(X,Y):- sibling(X,Y) ,female(X).

father(X,Z):- parent(X,Z), male(X).
mother(X,Z):- parent(X,Z), female(X).

child(Child,Parent):- parent(Parent,Child).

uncle(U,Person) :-parent(P, Person), 
    sibling(U, P), 
    male(U).

aunt(A, Person) :-parent(P, Person),
    sibling(A,P),
    female(A).

cousin(C, Person) :- parent(X,C), parent(Y,Person),sibling(X,Y).

granchildren(X, Grand) :- parent(Grand,Y), parent(Y,X).



















