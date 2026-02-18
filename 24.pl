% Facts
diet(diabetes, low_sugar).
diet(bp, low_salt).
diet(obesity, low_fat).
diet(anemia, iron_rich_food).

% Rule
suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).
