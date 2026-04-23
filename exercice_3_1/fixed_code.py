"""
Exercice 3.1 : Correction proposée par l'IA
Cause identifiée : La liste contient un élément de type 'str' ('three'), ce qui provoque 
une TypeError lors de l'addition avec un entier (total).
Correction : Filtrer les éléments pour ne garder que les nombres ou convertir si possible.
"""

def calculate_average(numbers_list):
    """
    Calcule la moyenne des nombres dans une liste, en ignorant les valeurs non numériques.
    
    Args:
        numbers_list (list): Liste contenant des nombres (int, float) et potentiellement d'autres types.
        
    Returns:
        float: La moyenne des nombres valides. Retourne 0 si la liste est vide ou ne contient aucun nombre.
    """
    if not numbers_list:
        return 0
        
    # Filtrer uniquement les nombres (int ou float)
    valid_numbers = [n for n in numbers_list if isinstance(n, (int, float))]
    
    if not valid_numbers:
        return 0
        
    return sum(valid_numbers) / len(valid_numbers)

if __name__ == "__main__":
    my_nums = [1, 2, 'three', 4]
    avg = calculate_average(my_nums)
    print(f"Moyenne (éléments valides uniquement) : {avg}") # Devrait afficher (1+2+4)/3 = 2.33
