#job10

def sommeDUneListe():
    #déclaration + init. variable de méthode
    ma_liste=[8,24,27,48,2,16,9,7,84,91]
    produit=0
    test=[]
    #filtrage pour toute valeur 25<x>90
    '''for i in range(len(ma_liste)):
        if ma_liste[i]>25 and ma_liste[i]<90:
            produit=produit*ma_liste[i]'''
    #essai
    for i in range(len(ma_liste)):
        if ma_liste[i]>25 and ma_liste[i]<90:
            test.append(ma_liste[i])
            produit=produit*ma_liste[i]

    #impression
    print("produit de ma_liste: ", produit)

#exécution
sommeDUneListe()