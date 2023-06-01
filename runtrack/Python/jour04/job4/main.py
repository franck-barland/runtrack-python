#job4 insertion dans liste
def ma_list():
    #on créé la variable et init
    liste = ["pomme","cerise","orange",]
    #on ajoute un élément
    liste.append(("melon"))
    # on insert à la place voulue
    liste.insert(1,'mangue')
    #on imprime
    print(liste)
#on appelle la méthode
ma_list()