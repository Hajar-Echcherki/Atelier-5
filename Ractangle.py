class Vecteur2D:
    """Les Vecteurs plans."""

    def _init_(self, x0=0, y0=0):
        """Constructeur avec parametres par defaut."""
        self.x = x0  # initialisation de x et y, attributs d'instance
        self.y = y0
        self.nom = "coucou"

    def affiche(self):
        print(self.nom)

    def _str_(self):
        """ Utilisation du print """
        return "x = %d, y = %d" % (self.x, self.y)


# Auto-test ---------------------------------------------------------
if _name_ == '_main_':
    print(" une instance par defaut ".center(50, '-'))
    print(Vecteur2D())
    # --
    print(" une instance initialisee ".center(50, '-'))
    print(Vecteur2D(-5.2, 4.1))
    Vecteur2D().affiche()