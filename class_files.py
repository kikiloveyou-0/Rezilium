class File:
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        if self.contenu:
            return False
        else:
            return True

    def enfiler(self, valeur):
        self.contenu.insert(-(len(self.contenu)), valeur)

    def defiler(self):
        if self.est_vide() == False:
            self.contenu.pop()
        else:
            print("La liste est vide. Impossible de retirer une valeur.")

    def afficher(self):
        return(self.contenu)

    def taille(self):
        self.taille = len(self.contenu)
        return ("La pile a", self.taille, "valeurs.")

    def sommet(self):
        return ('La valeur au sommet de la pile est', self.contenu [len(self.contenu)-1], '.')



f=File()

f.enfiler(7)
f.enfiler(3)
f.enfiler(10)
print(f.contenu)

f.defiler()
f.enfiler(1)
print(f.est_vide())
print(f.contenu)
print(f.taille())
print(f.sommet())

f.defiler()
f.defiler()
f.defiler()
print(f.est_vide())