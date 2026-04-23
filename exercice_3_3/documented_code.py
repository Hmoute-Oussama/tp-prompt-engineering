"""
Exercice 3.3 : Génération de Documentation
Fonction originale sans documentation claire.
"""

def get_user_permissions(user_id: int, system_context: dict) -> list:
    """
    Récupère les permissions d'un utilisateur en fonction du contexte système.

    Cette fonction vérifie si l'identifiant de l'utilisateur appartient aux groupes
    'admins' ou 'editors' définis dans le dictionnaire system_context et retourne
    une liste de permissions correspondante.

    Args:
        user_id (int): L'identifiant unique de l'utilisateur.
        system_context (dict): Un dictionnaire contenant les listes d'IDs pour 
                               'admins' et 'editors'.
                               Format attendu : 
                               {'admins': [id1, id2], 'editors': [id3, id4]}

    Returns:
        list: Une liste de chaînes de caractères représentant les permissions.
              - ['read', 'write', 'delete', 'admin'] pour les administrateurs.
              - ['read', 'write'] pour les éditeurs.
              - ['read'] pour les autres utilisateurs.

    Example:
        >>> context = {'admins': [1], 'editors': [2]}
        >>> get_user_permissions(1, context)
        ['read', 'write', 'delete', 'admin']
        >>> get_user_permissions(3, context)
        ['read']
    """
    if user_id in system_context.get('admins', []):
        return ['read', 'write', 'delete', 'admin']
    elif user_id in system_context.get('editors', []):
        return ['read', 'write']
    else:
        return ['read']

if __name__ == "__main__":
    context = {
        'admins': [101, 105],
        'editors': [202, 203]
    }
    print(f"Permissions Admin (101): {get_user_permissions(101, context)}")
    print(f"Permissions Guest (999): {get_user_permissions(999, context)}")
