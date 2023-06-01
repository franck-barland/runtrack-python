class Rectangle:
    def __init__(self, __longueur, __largeur):
        self.__longueur=0
        self.__largeur=0

    def perimetre(self):
        perimetre=self.__longueur+self.__largeur
        return perimetre
    
    def surface(self):
        surface=self.__longueur+self.__largeur
        return surface
    
    def setLongueur(self):
        self.__longueur = input ("Veuillez entrer la longueur")
        
    def getLongueur(self):
        return self.__largeur

    def setLargeur(self):
        self.__largeur = input ("Veuillez entrer la largeur")

    def getLargeur(self):
        return self.__longueur

class Parallelepipede(Rectangle):

    def __init__(self):
        super().__init__()

    def setHauteur(__largeur):
        __largeur = input ("Veuillez entrer la largeur")

    def getLongueur(self):
        return self.__longueur

    def perimetre(self):
        perimetre=(self.__longueur+self.__largeur)*2
        return perimetre
    
    def surface(self):
        surface=self.__longueur+self.__largeur
        return surface

Parallelepipede().setHauteur()
