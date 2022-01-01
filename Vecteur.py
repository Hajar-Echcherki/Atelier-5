class Point:
    """classe des points du plan."""

    def _init_(self, x=0.0, y=0.0):
        "Initialisation avec valeurs par defaut"
        self.px = float(x)
        self.py = float(y)


class Segment:
    """classe composite utilisant la classe Point."""

    def _init_(self, x1, y1, x2, y2):
        "L'initialisation utilise deux objets Point"
        self.orig = Point(x1, y1)
        self.extrem = Point(x2, y2)

    def _str_(self):
        """Representation d'un objet segment."""
        return ("Segment : [({0}, {1}), ({2}, {3})]"
                .format(self.orig.px, self.orig.py, self.extrem.px, self.extrem.py))


# Auto-test ---------------------------------------------------------
if _name_ == '_main_':
    s = Segment(1, 2, 3, 4)
    print(s)