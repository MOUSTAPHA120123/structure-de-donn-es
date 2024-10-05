# Question1
my_liste = [2, 3, 6]

a = 1  # Initialisation
for i in my_liste:
    a = i * a
    print(a)

#Question2

"""Écrivez un programme Python pour obtenir une liste, triée par

ordre croissant par le dernier élément de chaque tuple, à partir

d'une liste donnée de tuples non vides.

Liste d'échantillons : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

Résultat attendu : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

Astuce : vous pouvez utiliser la fonction de tri."""

def return_last_element(tuple_item):
    return tuple_item [-1]

list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(list[::-1])

# Question3
"""Écrivez un programme Python qui combine deux dictionnaires en ajoutant des valeurs pour les clés communes.

d1 = {'a': 100, 'b': 200, 'c': 300}

d2 = {'a' : 300, 'b' : 200, 'd' : 400}

Résultat attendu : {'a' : 400, 'b' : 400, 'd' : 400, 'c' : 300}  """

#Les deux dictionnaires donnés
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Créer un nouveau dictionnaire combiné
d_combined = d1.copy()

# Parcourir les éléments du deuxième dictionnaire
for key, value in d2.items():
    if key in d_combined:
        # Si la clé est déjà présente dans d_combined, additionner les valeurs
        d_combined[key] += value
    else:
        # Si la clé n'existe pas, l'ajouter avec sa valeur
        d_combined[key] = value

# Afficher le dictionnaire combiné
print(d_combined)

# Question4
"""
Avec un nombre entier n donné, écrivez un programme pour 
générer un dictionnaire qui contient (i, i*i) de sorte que 
soit un nombre entier compris entre 1 et n (les deux inclus).
Le programme doit ensuite imprimer le dictionnaire. Supposons 
que l'entrée suivante soit fournie au programme : 8. La sortie 
doit alors être : {1 : 1, 2 : 4, 3 : 9, 
4 : 16, 5 : 25, 6 : 36, 7 : 49, 8 : 64}
"""

n = int(input("Entrez un nombre entier : "))

# Créer un dictionnaire vide

dictionnaire = {}

# Remplir le dictionnaire avec (i, i*i) pour i de 1 à n
for i in range(1, n + 1):
    dictionnaire[i] = i * i

# Imprimer le dictionnaire

print(dictionnaire)


# question5

""" Écrivez un programme pour trier un tuple par son élément float.

Par exemple : liste = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

Résultat attendu : [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]"""

def return_last_element(tuple_item):
    return tuple_item [-1]

list=[[('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]]
print(list[::-1])


# question6
"""Écrivez un programme Python pour créer un ensemble.
Exemples : {0, 1, 2, 3, 4}
Écrivez un programme Python pour effectuer une itération sur des ensembles.
Écrivez un programme Python pour ajouter des membres à un ensemble et pour
supprimer des éléments d'un ensemble donné."""

mon_ensemble = {0, 1, 2, 3, 4}
print(mon_ensemble)

for i in mon_ensemble:
    print(mon_ensemble)

# Ajout de nombres

mon_ensemble.add(5)
mon_ensemble.add(6)
mon_ensemble.add(7)
print('mon_ensemble aprés ajout', mon_ensemble)

# Suppréssion de nombres
mon_ensemble.remove(6)
mon_ensemble.remove(7)
print('suppréssion de 6 et 7', mon_ensemble)
