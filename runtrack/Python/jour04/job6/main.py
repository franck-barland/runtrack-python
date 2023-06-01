#job6


"""A faire:
    faire une boucle en entrée d'articles non définit -> gest. d'exception
    liste singleton !=0
    """

def liste():
    #on définit la liste
    L=[1,2,3,4]
    print ("liste de base",L)
    #on créé une mémoire tampon
    t=0
    #on effectue la permutation
    t=L[0]
    L[0]=L[3]
    L[3]=t
    print("liste permutée:",L)

liste()


