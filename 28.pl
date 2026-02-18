% Facts: Symptoms of diseases
symptom(fever).
symptom(cough).
symptom(headache).
symptom(sore_throat).
symptom(body_pain).

% Rules: Disease diagnosis
disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(body_pain).

disease(common_cold) :-
    symptom(cough),
    symptom(sore_throat).

disease(migraine) :-
    symptom(headache).
