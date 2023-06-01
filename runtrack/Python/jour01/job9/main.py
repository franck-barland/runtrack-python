#job9 pourAllerPlusLoin

def rechercheCaractereDanscChaineStr():
    #declar/typ/init var
    letterToLookFor=str("")
    userInput=str("")

    #entrees
    userInput=input("veuillez entrer votre chaine de caractère: \n")
    letterToLookFor=input("veuillez entrer le caractère à chercher, par défaut, ce sera 'e' : ")
    #Condition d'entrée par défaut
    if letterToLookFor=="":
        letterToLookFor="e"
    #recherche
    if letterToLookFor in userInput:
        print("le caractère '", letterToLookFor,"' a été trouvé!")
    else:
        print("le caractère '", letterToLookFor,"' n'a PAS été trouvé!")    

rechercheCaractereDanscChaineStr()