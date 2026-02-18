% define some facts about teachers and their subject codes
teaches(john, math).
teaches(jane, english).
teaches(bob, science).
teaches(sue, history).
teaches(tom, art).

% define some facts about students and the subjects they are taking
takes(alice, math).
takes(alice, science).
takes(bob, english).
takes(bob, science).
takes(carol, history).
takes(carol, art).
takes(dave, math).
takes(dave, english).
takes(dave, art).

% define a predicate to look up the subject codes taught by a teacher
teaching_subjects(Teacher, Subject) :-
teaches(Teacher, Subject).

SAVEETHA SCHOOL OF ENGINEERING

SAVEETHA INSTITUTE OF MEDICAL AND TECHNICA% Facts: Teachers and the subjects they teach
teaches(john, math).
teaches(jane, english).
teaches(bob, science).
teaches(sue, history).
teaches(tom, art).

% Facts: Students and the subjects they take
takes(alice, math).
takes(alice, science).
takes(bob, english).
takes(bob, science).
takes(carol, history).
takes(carol, art).
takes(dave, math).
takes(dave, english).
takes(dave, art).

% Predicate to find subjects taught by a teacher
teaching_subjects(Teacher, Subject) :-
    teaches(Teacher, Subject).

% Predicate to find students taking a subject
taking_students(Subject, Student) :-
    takes(Student, Subject).
