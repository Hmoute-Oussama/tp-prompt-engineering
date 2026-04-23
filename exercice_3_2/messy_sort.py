"""
Exercice 3.2 : Refactoring avec l'IA
Code de départ : Un tri à bulles (bubble sort) non structuré.
"""

# code de départ
a = [5, 3, 8, 6, 7, 2]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
print(a)
