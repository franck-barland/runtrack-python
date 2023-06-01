
#job3

def  tapis():


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
            #si nous sommes dans la première ligne ou la derniere ligne
            if i==0 or i == hauteur-1:
                #si la premiere colonne == 0 ou la derniere colonne == largeur-1, on met en mémoire "+" (encadrement de toutes les lignes par "+")
                if j==0 or j==largeur-1:
                    char += "+" 
                # sinon on met en mémoire "-"
                else: 
                    char += "-"
            # Si nous sommes strictement entre la première et dermière ligne
            else:
            #On encadre en mémoire la ligne par "|"
                if j==0 or j==largeur-1:
                    char += "|"
                # sinon 
                else:
                    #si lepointeur désigne la position du catactère en fonction de la ligne et de la colonne
                    if j==largeur-i-1:
                        char+=" "
                    #sinon on met en mémoire "#"
                    else:
                        char += "#"
    #...pour afficher le résultat..
        print (char)
    #et réinitialiser la mémoire de la variable pour la prochaine ligne
        char=""

'''def exceptions(X):
    ...'''

tapis()