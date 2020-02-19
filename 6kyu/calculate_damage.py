# Pokemon Damage Calculator
# https://www.codewars.com/kata/536e9a7973130a06eb000e9f

# My code
def calculate_damage(your_type, opponent_type, attack, defense):
    effectiveness = type_check(your_type, opponent_type)
    return (50 * (attack / defense) * effectiveness)
def type_check(your_type, opponent_type):
    if your_type == opponent_type:
        return 0.5
    elif your_type == "water":
        if opponent_type == "fire":
            return 2
        else:
            return 0.5
    elif your_type == "fire":
        if opponent_type == "water":
            return 0.5
        elif opponent_type == "grass":
            return 2
        elif opponent_type == "electric":
            return 1
    elif your_type == "grass":
        if opponent_type == "water":
            return 2
        elif opponent_type == "fire":
            return 0.5
        elif opponent_type == "electric":
            return 1
    elif your_type == "electric":
        if opponent_type == "water":
            return 2
        else:
            return 1

# best code
# from math import ceil
# D = {"fire": "grass", "water": "fire", "grass": "water", "electric": "water"}
# def calculate_damage(a, b, n, m):
#     return ceil(50 * (n / m) * (2 if D[a] == b else 0.5 if D[b] == a or a == b else 1))
