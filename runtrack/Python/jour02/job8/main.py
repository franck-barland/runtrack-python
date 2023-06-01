#job8

#On construit la méthode
def fruitLegumeSaison():

# on initialise les variables utilisées
    type=""
    saison=""





# On demande les entrées des données du problème
    type=input ("Veuillez entrer 'fruit' ou 'legume'...")
    saison=input ("Veuillez entrer 'été' ou 'hiver'..")

    # On teste si les entrées sont des valeurs attendues et si elles ne correspondent pas, 
    # on relance le programme.. 
    if (type != 'fruit' or 'legume' ) or ( saison != 'été' or 'hiver'):
        print ("veuillez entrer les valeurs attendues svp...")
        fruitLegumeSaison()

    #On exécute les instructions 
    if type == "fruits" and saison =="hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison =="été":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison=="hiver":
        print("artichaut, aubergine,navet")

    #On prévoie le reste des possibilités, et si elles ne correspondent pas, 
    # on relance le programme.. 
    else:
        print("Désolé, ce cas de figure n'est pas prévu par l'algorithme..")
        fruitLegumeSaison()

    #Nous arrivons dans le cas où toutes les possibilités attendues
    #sont remplies
    print ("Votre demande a donc bien été enregistrée!")

#On exécute le programme
fruitLegumeSaison()