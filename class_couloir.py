from class_cartes import uneCarte

class creationCouloir:
    def __init__(self):
        self.couloir = []

    def est_vide(self):
        if self.couloir:
            return False
        else:
            return True

    def enfiler(self, carteCliquée):
        self.couloir.insert(-(len(self.couloir)), carteCliquée)

    def defiler(self):
        if self.est_vide() == False:
            self.couloir.pop()
        else:
            print("La liste est vide. Impossible de retirer une valeur.")

    def afficher(self):
        return(self.couloir)

    def taille(self):
        self.taille = len(self.couloir)
        return ("Le couloir de ce joueur a", self.taille, "unités.")

    def sommet(self):
        return ("L'unité", self.couloir [len(self.couloir)-1] [3], "est à l'avant du couloir.")


petit_tank = uneCarte(1, 2, "petit", "petit_tank")
petit_tank = petit_tank.afficherr()

moyen_tank = uneCarte(4, 6, "incroyablement moyen", "moyen_tank")
moyen_tank = moyen_tank.afficherr()


J1=creationCouloir()
J1.enfiler(petit_tank)
J1.enfiler(moyen_tank)
print(J1.afficher())
