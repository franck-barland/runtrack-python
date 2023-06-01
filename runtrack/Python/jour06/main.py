# Mot de passe
# Mot de passe aléatoire
# utilisation d'algorithme de hachage (SHA-256, bcrypt)

#Declar/typ/init
#Password
entry=str("")
pointerInPassword = int(0)


def motDePass():
    conditionEntry()

def conditionEntry():

    #pointer letter in password


    #input
    entry = (input("veuillez entrer un mot de passe svp: "))
    #print("Nombre caractères de l'entrée", len(entry))
    
    #condition 1: 8 carac. mini.
    if len(entry)<8:
        print ("svp d'entrer 8 carctères minimum...")
        conditionEntry()
    
    #cond. 2 : mini. 1 upper case letter (as local var)
    callMethod = lambda x: (x.isupper())
    errorMessage="Merci d'entrer au moins 1 lettre majuscule ..."  
    testCase234(entry,callMethod,errorMessage)

    #cond. 3 : 1 mini. letter lower case
    callMethod = lambda x: (x.islower())
    errorMessage="Merci d'entrer au moins 1 lettre minuscule ..."
    testCase234(entry,callMethod,errorMessage)

    #cond. 4 : 1 mini. digit
    calledMethod = lambda x: (x.isdigit())
    errorMessage="Merci d'entrer au moins 1 chiffre ..."
    testCase234(entry,callMethod,errorMessage)

    #cond. 5 : 1 mini. special character (!, @, #, $, %, ^, &, *).
    errorMessage="Merci d'entrer au moins 1 caractère special : ! @ # $ % ^ & *"
    testCase5(entry,errorMessage)


    print("Votre mot de passe est valide!")


    '''passwordLengh=range(len(entry))
    print ("range(len(entry))= ",passwordLengh)'''

def testCase234(entry,calledMethod,errorMessage):
 
    for pointerInPassword in range(len(entry)):
        
        #cond. 2.3.4 : mini. 1 upper case letter (as local var)
        if calledMethod(entry[pointerInPassword]):
            break
        elif pointerInPassword == len(entry)-1 :
            print (errorMessage)
            conditionEntry()

def testCase5(entry,errorMessage):
        #cond. 5 : 1 mini. special character (!, @, #, $, %, ^, &, *).
        for pointerInPassword in range(len(entry)):
            if entry[(pointerInPassword)]=="+" or entry[(pointerInPassword)]=="!" or entry[(pointerInPassword)]==("@") or entry[(pointerInPassword)]==("#") or entry[(pointerInPassword)]==("$") or entry[(pointerInPassword)]==("%") or entry[(pointerInPassword)]==("^") or entry[(pointerInPassword)]==("&") or entry[(pointerInPassword)]==("*"):
                '''print ("caractère spécial trouvé en ",pointerInPassword+1 ,'eme lettre')'''
                break
            elif pointerInPassword == len(entry)-1 :
                print ()
                conditionEntry()

motDePass()


'''# Mot de passe
# Mot de passe aléatoire
# utilisation d'algorithme de hachage (SHA-256, bcrypt)

def motDePass():
    #Declar/typ/init
    #Password
    entry=str("")

    conditionEntry()

def conditionEntry():

    #pointer letter in password
    pointerInPassword = int(0)

    #input
    entry = (input("veuillez entrer un mot de passe svp: "))
    print("Nombre caractères de l'entrée", len(entry))
    
    #condition 1: 8 carac. mini.
    if len(entry)<8:
        print ("svp d'entrer 8 carctères minimum...")
        conditionEntry()

    passwordLengh=range(len(entry))
    print ("range(len(entry))= ",passwordLengh)

    #cond. 2 : mini. 1 upper case letter (as local var) 
    for pointerInPassword in (passwordLengh):
        #print("Pointeur= ",pointerInPassword)
        if entry[pointerInPassword].isupper():
            #print ("Majuscule trouvée en ", pointerInPassword ,' lettre')
            break
        elif pointerInPassword == len(entry)-1 :
            print ("Merci d'entrer au moins 1 lettre majuscule ...")
            conditionEntry()

        #cond. 3 : 1 mini. letter lower case
        for pointerInPassword in range(len(entry)):

            if entry[(pointerInPassword)].islower():
                #print ("Minuscule trouvée à ",pointerInPassword+1,'eme lettre')
                break
            elif pointerInPassword == len(entry)-1 :
                print ("Merci d'entrer au moins 1 lettre minuscule ...")
                conditionEntry()

        #cond. 4 : 1 mini. digit
        for pointerInPassword in range(len(entry)):
            if entry[(pointerInPassword)].isdigit():
                #print ("digit trouvé en ",pointerInPassword+1 ,'eme lettre')
                break
            elif pointerInPassword == len(entry)-1 :
                print ("Merci d'entrer au moins 1 chiffre ...")
                conditionEntry()

        #cond. 5 : 1 mini. special character (!, @, #, $, %, ^, &, *).
        for pointerInPassword in range(len(entry)):
            if entry[(pointerInPassword)]=="+" or entry[(pointerInPassword)]=="!" or entry[(pointerInPassword)]==("@") or entry[(pointerInPassword)]==("#") or entry[(pointerInPassword)]==("$") or entry[(pointerInPassword)]==("%") or entry[(pointerInPassword)]==("^") or entry[(pointerInPassword)]==("&") or entry[(pointerInPassword)]==("*"):
                #print ("caractère spécial trouvé en ",pointerInPassword+1 ,'eme lettre')
                break
            elif pointerInPassword == len(entry)-1 :
                print ("Merci d'entrer au moins 1 caractère special : ! @ # $ % ^ & *")
                conditionEntry()
    
    print("Votre mot de passe est valide!")

motDePass()'''