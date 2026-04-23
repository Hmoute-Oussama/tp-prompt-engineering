"""
Exercice 2.1 - Version 3 : Prompt avec Persona
Prompt utilisé : "En tant que développeur Python, écris une fonction calculate(a, b, op) qui
prend deux entiers et une chaîne représentant une opération mathématique ('+', '-', '*', '/').
La fonction doit être robuste, bien documentée, gérer les erreurs (division par zéro, opérateur
invalide), arrondir les divisions à deux décimales, et respecter les conventions PEP8. Inclue
un docstring et des commentaires clairs."

Résultat généré par l'IA :
"""

from typing import Union

# Ensemble des opérateurs pris en charge par la fonction
VALID_OPERATORS = {'+', '-', '*', '/'}


def calculate(a: int, b: int, op: str) -> Union[int, float]:
    """Effectue une opération arithmétique entre deux entiers.

    Cette fonction prend deux entiers et un opérateur arithmétique sous
    forme de chaîne de caractères, puis retourne le résultat de l'opération
    correspondante. La division est arrondie à deux décimales.

    Args:
        a (int): Le premier opérande entier.
        b (int): Le second opérande entier.
        op (str): L'opérateur arithmétique. Valeurs acceptées : '+', '-', '*', '/'.

    Returns:
        Union[int, float]: Le résultat de l'opération.
            - int pour l'addition, la soustraction et la multiplication.
            - float arrondi à 2 décimales pour la division.

    Raises:
        TypeError: Si ``a`` ou ``b`` ne sont pas des entiers, ou si ``op``
            n'est pas une chaîne de caractères.
        ValueError: Si ``op`` n'est pas un opérateur valide.
        ZeroDivisionError: Si l'opération est une division et que ``b`` vaut 0.

    Examples:
        >>> calculate(5, 3, '+')
        8
        >>> calculate(5, 3, '-')
        2
        >>> calculate(5, 3, '*')
        15
        >>> calculate(5, 3, '/')
        1.67
    """
    # --- Validation des types des arguments ---
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(
            f"Les opérandes doivent être des entiers. "
            f"Reçu : a={type(a).__name__}, b={type(b).__name__}."
        )
    if not isinstance(op, str):
        raise TypeError(
            f"L'opérateur doit être une chaîne de caractères. "
            f"Reçu : {type(op).__name__}."
        )

    # --- Validation de l'opérateur ---
    if op not in VALID_OPERATORS:
        raise ValueError(
            f"Opérateur invalide : '{op}'. "
            f"Les opérateurs valides sont : {VALID_OPERATORS}."
        )

    # --- Exécution de l'opération ---
    if op == '+':
        return a + b

    if op == '-':
        return a - b

    if op == '*':
        return a * b

    # Division avec gestion de la division par zéro
    if b == 0:
        raise ZeroDivisionError(
            "Division par zéro impossible : le diviseur 'b' ne peut pas être 0."
        )
    return round(a / b, 2)


if __name__ == "__main__":
    # Démonstration des opérations de base
    print(f"calculate(5, 3, '+') = {calculate(5, 3, '+')}")   # 8
    print(f"calculate(5, 3, '-') = {calculate(5, 3, '-')}")   # 2
    print(f"calculate(5, 3, '*') = {calculate(5, 3, '*')}")   # 15
    print(f"calculate(5, 3, '/') = {calculate(5, 3, '/')}")   # 1.67
