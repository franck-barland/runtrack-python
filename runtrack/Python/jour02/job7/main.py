#job7
def langage():
    langue = ""
    resultat = ""

    langue = input ("veuillez entrer votre langage: ")
    
    if langue == "javascript":
        resultat = "tu es un developpeur web"
    elif langue =="python":
        resultat = "tu es un developpeur IA"
    elif langue =="java":
        resultat ="tu es un developpeur logiciel"
    elif langue == "reactjs":
        resultat ="tu es un developpeur mobile"
    else :
        resultat ="un jour, je serai le meilleur developpeur…"
    print (resultat)

langage()


