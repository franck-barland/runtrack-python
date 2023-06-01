def rectangle():

    #init + typage + entrées des variables
    char=""
    hauteur=int(input("entrez la hauteur svp: "))
    largeur=int(input("entrez la largeur svp: "))

    #gestion exceptions hauteur & largeur doivent être des entiers
    '''
    exceptions(hauteur)
    exceptions(largeur)'''

    #Dessin
    #gestion ligne
    for i in range(hauteur):
        #gestion colonne
        for j in range(largeur):
            #si la premiere colonne == 0 ou la derniere colonne ==-1, on met en mémoire "|" (encadrement de toute les lignes par "|")
            if j==0 or j==largeur-1:
                char += "|" 
                # sinon on met en mémoire "-"
            else: 
                char += "-"   
        #...pour afficher le résultat..
        print (char)
        #et réinitialiser la mémoire pour la prochaine ligne
        char=""


'''essai
def exceptions(X):'''

rectangle()