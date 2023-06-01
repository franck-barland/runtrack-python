class operateur:
    """Entrée de l'opérateur avec test d'exception"""

    def __init__(oper):
        def conditionsDEntrees():
            oper = input ("Opérateur?")
            if oper != ("*" or "-" or "+" or "/"):
                print("Prière de bien indiquer un opérateur entre '+' '-' '*' '/'!!!")
                # si l'entrée n'est pas un opérateur on recommence la méthode
                conditionsDEntrees()
            #sinon on retourne la valeur de l'opérateur
            return oper