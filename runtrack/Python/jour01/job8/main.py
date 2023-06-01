#job8

def multiplication():
    
    #declar/typ/init
    entree=""
    num1=int()
    num2=int()
    rslt=int()

    #entrees

        # importance de parser l'input!!
    num1=int(input ("Donnez la première valeur svp, sinon la valeur par défaut sera '3'"))
    print("Typage de num1 avant condition: ",type(num1))
    if entree==str(num1) :
        (num1)=(3)

    print ("la première valeur est donc: ",num1)

        # importance de parser l'input en int()!!
    num2=int(input ("Donnez la deuxième valeur svp, sinon la valeur par défaut sera '14'"))
    if entree==str(num2) :
        num2=(14)
    print ("la deuxième valeur est donc: ",num2) 

    # Calcul du produit
    rslt=num1*num2
    
    #imp
    print ("Le résultat du produit de", num1, " * ", num2," est donc: ", rslt )

multiplication() 
