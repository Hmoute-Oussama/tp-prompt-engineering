# Rapport de TP : Ingénierie de Prompt appliquée au Développement

**Étudiant :** Oussama Hmoute 
**Cours :** Prof. Imane Allaouzi  
**Sujet :** Ingénierie de prompt appliquée à la génération de code avec l’IA

---

## Partie 1 : Choix de la Solution d'IA Générative

1.  **Solution choisie :** Gemini 2.0 Flash (via Google AI)
2.  **Définition brève :** Gemini est une famille de modèles d'IA multimodaux développés par Google DeepMind, capable de comprendre et de générer du texte, du code et d'autres médias avec une grande fenêtre de contexte.
3.  **Avantages perçus :**
    *   **Vitesse d'exécution :** Génération quasi instantanée de blocs de code complexes.
    *   **Intégration de l'écosystème :** Excellente connaissance des bibliothèques standards et frameworks modernes.
    *   **Fenêtre de contexte large :** Capacité à analyser de gros volumes de code existant pour proposer des solutions cohérentes.
4.  **Inconvénients ou limites perçues :**
    *   **Hallucinations :** Risque de suggérer des bibliothèques ou des paramètres qui n'existent pas dans des versions spécifiques.
    *   **Sécurité :** Peut parfois suggérer des fonctions obsolètes ou non sécurisées (comme `eval()`) si le prompt n'est pas restrictif.
    *   **Vérification nécessaire :** Le code généré nécessite toujours une revue humaine et des tests unitaires pour garantir la validité logique.
5.  **Cas d'utilisation typiques :** Génération de boilerplate (code répétitif), refactorisation de fonctions isolées, écriture de tests unitaires et documentation automatique.


Questions du Prompt Vague :
Q1. La fonction est-elle nommée ?
Non, le prompt vague ne précise pas de nom. L'IA peut nommer la fonction n'importe comment (calc, operation, compute...) selon son choix.
Q2. Quelles opérations sont prises en charge ?
Non précisé. L'IA décide elle-même quelles opérations inclure, peut-être seulement + et -, ou toutes les quatre.
Q3. Y a-t-il une gestion des erreurs ?
Probablement non ou minimale, car le prompt n'en parle pas.
Q4. Des commentaires ?
Probablement non, rien n'est demandé à ce sujet.

## Partie 2 – Génération de code avec IA

### Exercice 2.1 : Fonction `calculate`
| Version | Différences observées |
| :--- | :--- |
| **Vague** | Code minimaliste, ne gère pas les erreurs, affiche au lieu de retourner, noms génériques. |
| **Spécifique** | Respecte le nom de fonction imposé, gère la division par zéro, docstring présent, arrondit à 2 décimales. |
| **Persona** | Code très professionnel, utilise des "type hints", constantes pour les opérateurs, validation stricte des entrées. |

**Analyse Critique :**
1.  **Impact du Prompt Engineering :** La **spécificité** a eu le plus grand impact sur la fonctionnalité, tandis que le **persona** a amélioré la structure et la maintenabilité.
2.  **Comportements inattendus :** Dans la version vague, l'IA n'a pas inclus de mécanisme pour arrêter une opération invalide (elle ne faisait rien).
3.  **Coût vs Qualité :** Un prompt vague demande 2 à 3 itérations manuelles pour corriger le code (plus coûteux), alors qu'un prompt spécifique produit un code prêt pour la production dès le premier essai.

   

### Exercice 2.2 : `format_product_code`
*   **Zero-Shot :** L'IA a parfois confondu l'indice d'insertion (split à 3/7 au lieu de 3/6 pour obtenir le format de l'exemple).
*   **One-Shot :** L'exemple a immédiatement corrigé la logique de découpage de la chaîne.
*   **Few-Shot :** L'ajout de l'exemple d'erreur a poussé l'IA à ajouter des validations de longueur plus explicites et des blocs de gestion d'exception.

**Analyse Critique :**
*   Le **Few-Shot Prompting** est crucial pour les formats de données propriétaires ou les règles métier complexes qui ne sont pas des standards publics.

---

## Partie 3 – Débogage et Amélioration

### Exercice 3.3 : Documentation de `get_user_permissions`

#### Section README : Utilisation de la fonction
```markdown
### Fonction : `get_user_permissions`
Cette fonction permet de déterminer les droits d'accès d'un utilisateur au sein du système.

**Prérequis :**
Le paramètre `system_context` doit être un dictionnaire contenant les clés `'admins'` et `'editors'`, chacune associée à une liste d'identifiants (entiers).

**Exemple d'appel :**
```python
context = {'admins': [1, 5], 'editors': [10]}
permissions = get_user_permissions(5, context)
# Retourne : ['read', 'write', 'delete', 'admin']
```
```

---

## Conclusion
Le TP démontre que l'IA est un outil puissant mais dépendant de la qualité de la directive. Passer d'un mode "utilisateur" à un mode "ingénieur de prompt" permet de réduire drastiquement le temps de débogage et d'élever la qualité du logiciel produit.
