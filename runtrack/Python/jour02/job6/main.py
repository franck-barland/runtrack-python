#job6
def rechercheDeSigne():
    #On déclare et initialise les données d'entrée
    entree = 0
    signe = ""
    #on demande les données d'entrée à l'utilisateur
    entree = input("Veuillez entrer un nombre :")
    #On parse l'entrée en integer
    entree = int(entree)
    #on lance les conditions
    if entree < 0:
       signe = "négatif"
    if entree > 0:
       signe = "positif"
    else :
       signe = "nombre nul"
       #on imprime à l'écran
    print (signe)
#on exécute le programme
rechercheDeSigne()