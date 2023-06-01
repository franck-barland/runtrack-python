class Personne:
    #variable de classe
    #age=int(14)
    
    def __init__(self):
        self.age=14
    
    def afficherAge(self):
        print("L'age est de :", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self):
        self.age = int(input ("Veuillez indiquer le nouvel age: "))
        return self.age
    
class Eleve(Personne):
    
    def allerEnCours(self):
        print("Je vais en cours",self.afficherAge() )

class Professeur():

    def __init__(self):
        self.__matiereEnseignee =""
        
    def enseigner():
        print("Le cours commencer!")

personne = Personne()
eleve = Eleve()
eleve.bonjour()
eleve.afficherAge()