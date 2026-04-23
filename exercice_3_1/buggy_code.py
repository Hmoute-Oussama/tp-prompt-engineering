"""
Exercice 3.1 : Débogage assisté
Code original fourni par le collègue avec une erreur TypeError.
"""

def calculate_average(numbers_list):
    # This function calculates the average of numbers in a list
    # It has some issues
    total = 0
    for num in numbers_list:
        total += num  # <-- Erreur ici car 'three' est une chaîne
    average = total / len(numbers_list)
    return average

if __name__ == "__main__":
    try:
        # Example of usage (causes errors)
        my_nums = [1, 2, 'three', 4]
        avg = calculate_average(my_nums)
        print(f"Average: {avg}")
    except TypeError as e:
        print(f"Erreur détectée : {e}")
