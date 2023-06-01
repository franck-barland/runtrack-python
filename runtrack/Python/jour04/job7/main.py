#job7

#Variable de classe
R=0

def ma_liste():
    L=[8,24,48,2,16]
    rechercheMultipleDe3(L)

def rechercheMultipleDe3(L):
    #on créé une boucle correspondant au nombes de singletons dans L
    for i in range(len(L)):
        print(L[i])

ma_liste()