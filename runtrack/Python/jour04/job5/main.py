#job5 insertion dans liste
def ma_list():
    #on créé la variable et init
    L=[0,1,2,3,4]
    #on lance la méthode de remplacement
    remplacement(L)
    impression(L)

def remplacement(L):
    #On effectue l'énnoncé
    L[3]=L[2]+L[4]

def impression(L):
        #on imprime (2x?)
        print("Impression de L[3]: ",L[3])
        #impression du dernier terme
        print("Impression dernier singleton de la liste: ",L[4])

#on appelle la méthode
ma_list()