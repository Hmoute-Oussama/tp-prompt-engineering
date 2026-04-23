"""
Exercice 2.2 - Version 3 : Few-Shot Prompting (avec plusieurs exemples)
Prompt utilisé : "Crée une fonction Python format_product_code(product_id). Le product_id
doit être une chaîne de 10 caractères alphanumériques.
Exemples :
  - format_product_code('ABC123DEF4') ➞ 'ABC-123-DEF4'
  - format_product_code('XYZ987GHIJ') ➞ 'XYZ-987-GHIJ'
  - format_product_code('SHORT') ➞ lève ValueError
La fonction doit lever une ValueError si l'entrée est invalide (longueur ≠ 10 ou caractères
non alphanumériques). Inclue un docstring."

Résultat généré par l'IA :
"""


def format_product_code(product_id):
    """Formate un identifiant produit en insérant des tirets.

    Prend une chaîne de 10 caractères alphanumériques et insère des tirets
    après le 3ème et le 6ème caractère, produisant le format XXX-XXX-XXXX.

    Args:
        product_id (str): Identifiant produit de 10 caractères alphanumériques.

    Returns:
        str: L'identifiant formaté (ex : 'ABC-123-DEF4').

    Raises:
        ValueError: Si le product_id est invalide :
            - longueur différente de 10 caractères,
            - contient des caractères non alphanumériques.

    Examples:
        >>> format_product_code("ABC123DEF4")
        'ABC-123-DEF4'
        >>> format_product_code("XYZ987GHIJ")
        'XYZ-987-GHIJ'
        >>> format_product_code("SHORT")
        Traceback (most recent call last):
            ...
        ValueError: Le product_id doit contenir exactement 10 caractères. Reçu : 5.
    """
    # Validation du type d'entrée
    if not isinstance(product_id, str):
        raise ValueError(
            f"Le product_id doit être une chaîne de caractères. "
            f"Reçu : {type(product_id).__name__}."
        )

    # Validation de la longueur
    if len(product_id) != 10:
        raise ValueError(
            f"Le product_id doit contenir exactement 10 caractères. "
            f"Reçu : {len(product_id)}."
        )

    # Validation des caractères (uniquement alphanumériques)
    if not product_id.isalnum():
        raise ValueError(
            "Le product_id ne doit contenir que des caractères alphanumériques."
        )

    # Formatage : insertion des tirets aux positions 3 et 6
    part1 = product_id[:3]   # 3 premiers caractères
    part2 = product_id[3:6]  # 3 caractères suivants
    part3 = product_id[6:]   # 4 derniers caractères

    return f"{part1}-{part2}-{part3}"


if __name__ == "__main__":
    # Tests de démonstration
    print(format_product_code("ABC123DEF4"))  # ABC-123-DEF4
    print(format_product_code("XYZ987GHIJ"))  # XYZ-987-GHIJ

    # Test d'erreur
    try:
        print(format_product_code("SHORT"))
    except ValueError as e:
        print(f"Erreur attendue : {e}")
