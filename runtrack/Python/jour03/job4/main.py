#job4

def fonction():
    #on déclare et initialise les variables
    donneesDEntrees = 0

    #on entre les données
    donneesDEntrees = range(101)

    for i in donneesDEntrees:
        #on recherche si i est multiple ( modulo )
        print("données d'entrée= ",(i))
        if i%3==0:
            print("Fizz")
        else:
            print(i)
    
fonction() 