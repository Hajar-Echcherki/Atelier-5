class Rectangle:
   #définir la classe Rectangle

    def _init_(self, longueur=16, largeur=17): #définir un constrecteur

        self.L = longueur   #initialisation avec valeurs par défaut
        self.l = largeur
        self.nom = "rectangle"

    def surface(self):
        return self.L * self.l  #Retourne la surface d'un rectangle

    def _str_(self):
        return ("\nLa surface du {0} de longueur{1} et de largeur{2} est {3}".format(self.nom, self.L, self.l, self.surface()))


class Carre(Rectangle):    #classe carre hérite de la classe rectangle
    def _init_(self, a=14):
        Rectangle._init_(self, a, a)   #définir un constrecteur sans parametre
        self.nom = "carre"
r = Rectangle(12, 8)
print(r)    #afficher la surface du rectangle
c = Carre()
print(c)    #afficher la surface du carre


