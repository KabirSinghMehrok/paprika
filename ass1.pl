% list of suggested coureses to take up for pursuing career in a given field
courses(aiml, [dsa, ip, ada, dm, m3, ai, ml, nlp]).
courses(biol, [ip, dsa, dm, m3, nb, mlba, chi, biop]).
courses(cysc, [dsa, ip, dm, m3, cn, cldc, fcs, ac]).
courses(data, [ip, dsa, dm, m3, dmg, dpm]).
courses(desi, [df, iag, tdaf, davp, efd, vdc]).
courses(econ, [dm, m3, ra, ff, gt]).
courses(math, [dm, m3, tnt, cmpa, sc, ra2, spa, ita]).
courses(sdev, [ip, dsa, ada, dm, cn, cldc, mad]).

% prereq(A, B) -> A is a prerequisite of B
prereq(dsa, nb).
prereq(gmb, nb).
prereq(ml, chi).
prereq(ap, chi).
prereq(os, cn).
prereq(ada, cn).
prereq(cn, cldc).
prereq(cn, fcs).
prereq(la, nlp).
prereq(ada, nlp).
prereq(dbms, dmg).
prereq(dm, ac).
prereq(dis, df).
prereq(nt, tnt).
prereq(ra1, cmpa).
prereq(m1, sc).
prereq(ra1, ra2).
prereq(pns, spa).
prereq(m4, ita).

% finds whether course A is prerequisite of course B
is_prereq(A, B) :- prereq(A, B).
is_prereq(A, B) :- is_prereq(A, X), prereq(X, B).

% assert(branch(csd)).
% assert(year(7)).
% assert(career(desi)).
% assert(field(hiedu)).
% assert(cgpa(8)).
% assert(done([ai, ml, m3, dm, ip, dc, dsa, ada, dmg, ])).

find_electives :- 
  % find L = list of courses corresponding to the given career
  done(D), career(C), courses(C, L),
  % subtract to find a new list T = courses to be done for the given field
  subtract(L, D, T),
  courses_to_do(T, List_duplicates),
  sort(List_duplicates, List_sorted),
  subtract(List_sorted, D, Final),
  % write("working"), nl,
  write(Final), 
  assert(final(Final)),
  nl.

find_prereqs(C, L) :- 
  % find list of prereqs of course C
  findall(X, prereq(X, C), L).

all_prereqs([], []).
all_prereqs([H|T], List) :-
  find_prereqs(H, List_H),
  all_prereqs(T, Tail_list),
  append(List_H, Tail_list, List).

courses_to_do(T, List) :-
  all_prereqs(T, List_prereq),
  append(T, List_prereq, List).

analyse_cgpa(C) :- C < 8.
analyse_cgpa(C) :- C > 8.

analyse :- 
  find_electives,
  cgpa(C), analyse_cgpa(C), nl.