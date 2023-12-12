def moyenne(l):
    """
    Calcule la moyenne des éléments d'une liste.
    
    Return:
        -La moyenne des nombres dan la liste. Retourne 0 si la liste est vide.
    """
    
    assert (type(l) == list) , "L n'est pas une liste (moyenne)"
    
    
    if len(l) == 0:
        return 0  
    somme = 0
    for nombre in l:
        somme += nombre
    moyenne = somme / len(l)
    return moyenne

def Minimum(L):
    """
    Trouve le minimum dans une liste de nombres.
    
    Return:
        - Le minimum des nombres dans la liste. Si la liste est vide, retourne None.
    """

    assert (type(L) == list) , "L n'est pas une liste (minimum)"
    
    if len(L) == 0:
        return None  
    minimum = L[0]  
    for nombre in L:
        if nombre < minimum:
            minimum = nombre
    return minimum


def rechercheSequentielle(L, date_recherchee):
    """
    Recherche une date dans une liste de dates. La liste est en str et représente les dates.
    
    Return:
        L'indice de la date recherchée dans la liste. Si la date n'est pas trouvée, retourne -1.
    """

    assert (type(L) == list) , "L n'est pas une liste (rechercheSequentielle)"
    assert (len(L) >= 1) , "L est une liste vide"
    assert (type(date_recherchee) == int) , "date_rechercher n'est pas un entier"


    
    for i in range(len(L)):
        if L[i] == date_recherchee:
            indice = i
            if indice != -1:
                print(f"La date a été trouvée à l'indice {indice}.")
            else:
                print(f"La date n'a pas été trouvée dans la liste.")
            return (indice)
    return (-1) 
