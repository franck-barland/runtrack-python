#job5 Retourdu login de l'os de l'utilisateur

import os

def alphabet():
    #Décl/typ/init
    alpha=str(("zyxwvutsrqponmlkjihgfedcba, tu as vu "+  os.getlogin() + "!, je connais même mon alaphabet à l'envers! :p"))
    #imp
    print("L'alphabet est: ",alpha)

alphabet()