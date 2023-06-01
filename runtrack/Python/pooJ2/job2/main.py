class Personne:
    #variable de classe
    #age=int(14)
    
    def __init__(self):
        self.age=15
    
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

    def affichageAge(self):
        print ("l'age de l'élève est de", self.age)

    def setAgeEleve(self):
         self.age=15

    def getAgeEleve(self):
        return self.age
       

class Professeur(Personne):

    def __init__(self):
        self.__matiereEnseignee =""

    def setAgeProfesseur(self,newage):
        self.age=newage

    def getAgeProfesseur(self):
        return self.age

    def enseigner(self):
        print("Le cours commencer!")

personne = Personne()
eleve=Eleve()
eleve.bonjour()
eleve.allerEnCours()
eleve.setAgeEleve()

professeur = Professeur()
professeur.setAgeProfesseur(40)
print("l'age du professeur est de :",professeur.getAgeProfesseur())
professeur.enseigner()

