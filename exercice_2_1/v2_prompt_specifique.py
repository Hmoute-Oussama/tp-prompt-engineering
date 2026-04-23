"""
Exercice 2.1 - Version 2 : Prompt Spécifique
Prompt utilisé : "Écris une fonction Python appelée calculate(a, b, op) qui prend deux entiers
a et b, et une chaîne op indiquant '+', '-', '*', ou '/'. La fonction doit retourner le résultat de
l'opération, gérer les erreurs (division par zéro, opération invalide) et arrondir le résultat de
la division à deux décimales. Ajoute un docstring détaillé et des commentaires."

Résultat généré par l'IA :
"""


def calculate(a, b, op):
    """
    Effectue une opération mathématique entre deux entiers.

    Args:
        a (int): Le premier opérande.
        b (int): Le second opérande.
        op (str): L'opérateur mathématique ('+', '-', '*', '/').

    Returns:
        int ou float: Le résultat de l'opération. Les divisions sont arrondies
                      à deux décimales.

    Raises:
        ZeroDivisionError: Si op est '/' et b vaut 0.
        ValueError: Si op n'est pas un opérateur valide.
    """
    # Vérifier que l'opérateur est valide
    if op == '+':
        return a + b  # Addition
    elif op == '-':
        return a - b  # Soustraction
    elif op == '*':
        return a * b  # Multiplication
    elif op == '/':
        # Gestion de la division par zéro
        if b == 0:
            raise ZeroDivisionError("La division par zéro est impossible.")
        # Arrondir le résultat à deux décimales
        return round(a / b, 2)
    else:
        # Opérateur non reconnu
        raise ValueError(f"Opérateur invalide : '{op}'. Utilisez '+', '-', '*' ou '/'.")


# Exemples d'utilisation
if __name__ == "__main__":
    print(calculate(5, 3, '+'))   # 8
    print(calculate(5, 3, '-'))   # 2
    print(calculate(5, 3, '*'))   # 15
    print(calculate(5, 3, '/'))   # 1.67
