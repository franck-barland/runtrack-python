#job8


def sommeDUneListe():
    #déclaration + init. variable de méthode
    ma_liste=[8,24,27,48,2,16,9,7,84,91]
    nbreSingleton =0
    somme=0
    #recherche du nombre de singletond
    nbreSingleton=len(ma_liste)
    #addition
    for i in range(nbreSingleton):
        somme=somme+ma_liste[i]
    #imp
    print("somme de ma_liste: ", somme)

sommeDUneListe()