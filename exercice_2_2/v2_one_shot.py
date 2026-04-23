"""
Exercice 2.2 - Version 2 : One-Shot Prompting (avec un exemple)
Prompt utilisé : "Crée une fonction Python format_product_code(product_id). Le product_id
doit être une chaîne de 10 caractères alphanumériques. Voici un exemple d'entrée-sortie:
format_product_code('ABC123DEF4') devrait retourner 'ABC-123-DEF4'. La fonction doit lever
une ValueError si l'entrée est invalide. Inclue un docstring."

Résultat généré par l'IA :
"""


def format_product_code(product_id):
    """Formate un identifiant produit en insérant des tirets.

    Insère un tiret après le 3ème et le 6ème caractère, produisant le
    format XXX-XXX-XXXX.

    Args:
        product_id (str): Identifiant produit de 10 caractères alphanumériques.

    Returns:
        str: L'identifiant formaté (ex : 'ABC-123-DEF4').

    Raises:
        ValueError: Si le product_id n'a pas exactement 10 caractères
                    ou contient des caractères non alphanumériques.

    Examples:
        >>> format_product_code("ABC123DEF4")
        'ABC-123-DEF4'
    """
    # Vérification de la longueur
    if len(product_id) != 10:
        raise ValueError(
            f"Le product_id doit contenir exactement 10 caractères. "
            f"Reçu : {len(product_id)}."
        )

    # Vérification que la chaîne est alphanumérique
    if not product_id.isalnum():
        raise ValueError(
            "Le product_id ne doit contenir que des caractères alphanumériques."
        )

    # Découpage et insertion des tirets : XXX-XXX-XXXX
    return f"{product_id[:3]}-{product_id[3:6]}-{product_id[6:]}"


if __name__ == "__main__":
    print(format_product_code("ABC123DEF4"))  # ABC-123-DEF4
