"""
Exercice 2.2 - Version 1 : Zero-Shot Prompting (basé sur la règle)
Prompt utilisé : "Crée une fonction Python format_product_code(product_id). Le product_id
doit être une chaîne de 10 caractères alphanumériques. La fonction doit insérer un tiret après
le 3ème et le 7ème caractère. Si la chaîne n'a pas 10 caractères ou contient des caractères
non alphanumériques, elle doit lever une ValueError. Inclue un docstring."

Résultat généré par l'IA :
"""


def format_product_code(product_id):
    """Formate un identifiant produit en insérant des tirets.

    Le product_id doit être une chaîne de 10 caractères alphanumériques.
    Un tiret est inséré après le 3ème et le 7ème caractère.

    Args:
        product_id (str): Identifiant produit de 10 caractères alphanumériques.

    Returns:
        str: L'identifiant formaté avec des tirets (format : XXX-XXXX-XXX).

    Raises:
        ValueError: Si la longueur n'est pas de 10 ou si des caractères
                    non alphanumériques sont présents.
    """
    if len(product_id) != 10:
        raise ValueError(
            f"Le product_id doit contenir exactement 10 caractères. "
            f"Reçu : {len(product_id)}."
        )
    if not product_id.isalnum():
        raise ValueError(
            "Le product_id ne doit contenir que des caractères alphanumériques."
        )

    # Insertion des tirets après le 3ème et le 7ème caractère
    return f"{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}"


if __name__ == "__main__":
    print(format_product_code("ABC123DEF4"))  # ABC-123D-EF4  ← format XXX-XXXX-XXX
