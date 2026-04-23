"""
Exercice 3.2 : Version refactorisée par l'IA
Contraintes : PEP8, docstrings, fonctions modulaires, noms explicites, bloc __main__.
"""

from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
    """
    Trie une liste d'entiers en utilisant l'algorithme de tri à bulles.
    
    L'algorithme parcourt la liste et échange les éléments adjacents s'ils sont 
    dans le mauvais ordre. Ce processus est répété jusqu'à ce que la liste soit triée.

    Args:
        numbers (List[int]): La liste d'entiers à trier.

    Returns:
        List[int]: Une nouvelle liste triée par ordre croissant.
    """
    # Création d'une copie pour ne pas modifier l'original (bonne pratique)
    sorted_list = numbers.copy()
    n = len(sorted_list)
    
    for i in range(n):
        # Les i derniers éléments sont déjà en place
        for j in range(0, n - i - 1):
            # Parcourir la liste de 0 à n-i-1
            # Échanger si l'élément trouvé est plus grand que le suivant
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                
    return sorted_list

def display_results(original: List[int], sorted_list: List[int]) -> None:
    """Affiche les listes originale et triée de manière lisible."""
    print(f"Liste originale : {original}")
    print(f"Liste triée     : {sorted_list}")

if __name__ == "__main__":
    # Données d'exemple
    data_to_sort = [5, 3, 8, 6, 7, 2]
    
    # Exécution du tri
    result = bubble_sort(data_to_sort)
    
    # Affichage
    display_results(data_to_sort, result)
