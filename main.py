'''
Ce module contient :
    - une fonction de lecture des données contenues dans le fichier listes.csv
    - diverses fonctions manipulant des listes numériques
'''

#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """
    Retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename,'r',encoding='utf8') as f :
        l = f.readlines()
    l = [ligne.strip() for ligne in l]
    l = [ligne.split(";") for ligne in l]
    l = [[int(val) for val in ligne] for ligne in l]
    return l


def get_list_k(data, k):
    '''
    Retourne la k-ième liste

    Args:
        data (list) : liste de listes retournée par read_data()
        k : nombre entier
    Return :
        l : liste
    '''
    l = data[k]
    return l

def get_first(l):
    '''
    Retourne le premier élément d'une liste
    '''
    return l[0]

def get_last(l):
    '''
    Retourne le dernier élément d'une liste
    '''
    return l[-1]

def get_max(l):
    '''
    Retoune le maximum d'une liste
    '''
    maxi = l[0]
    for elt in l :
        maxi = max(maxi,elt)
    return maxi

def get_min(l):
    '''
    Retourne le minimum d'une liste
    '''
    mini = l[0]
    for elt in l :
        mini = min(mini,elt)
    return mini

def get_sum(l):
    '''
    Retourne la somme d'une liste
    '''
    s = 0
    for elt in l :
        s += elt
    return s


#### Fonction principale


def main():
    '''
    Permet de vérifier le bon fonctionnement des fonctions précédentes
    '''
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
