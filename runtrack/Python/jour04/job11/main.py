

def typage():
    #initialisation des variables
    num1=float(input("num1= "))
    op=input("op= ")
    num2=float(input("num2= "))
    #on teste les exceptions d'entrées
    if op == "+":
        rslt= num1 + num2
    elif op == "-":
        rslt= num1 - num2
    elif op == "*":
        rslt= num1 * num2
    elif op == "/":
        rslt= num1 / num2
    else :
        rslt ="votre opérateur n'est pas reconnu..." 
    #impression
    print ("rslt= ",rslt)
#execution de la méthode
typage()