#job3

def addition():
    #declar/typ/init
    a=int()
    b=int()
    questionForA=("Veuillez entrer le premier terme: \n")
    questionForB=("Veuillez entrer le deuxième terme: \n")

    #except. manag.
    a=exception(a,questionForA)
    b=exception(b,questionForB)

    #exec
    Add(a,b)
    print ("L'addition demandée est: ", Add(a,b))

def exception(x,questionFor):
    while True:
        try:
            x=int(input(questionFor))
            break
        except ValueError:
            print("Attention, il faut entrer une valeur"+ 
            "numérique, SVP!!! Essayez encore: ")
    return x

def Add(nombre1,nombre2):
    return (nombre1 + nombre2)

addition()