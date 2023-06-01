def entree():
    #init variables
    entree=""
    #entrée données
    entree=input("Bonjour, quel est votre nom? ")
    '''#on gère les exceptions
    gestionException(entree)'''
    #imp
    print ("bonjour ",entree,"!" )

#essai
'''def gestionException(entree):
    try:
    entree = str(input("Entrez votre nom : "))
    print("Votrenom est", entree)
    except ValueError:
    print("Erreur : vous devez entrer un caractère alpha-numérique.")'''

entree()