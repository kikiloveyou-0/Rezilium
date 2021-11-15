class File:
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
        return ("La pile a", self.taille, "valeurs.")

    def sommet(self):
        return ('La valeur au sommet de la pile est', self.couloir [len(self.couloir)-1], '.')



'''f=File()

f.enfiler(7)
f.enfiler(3)
f.enfiler(10)
print(f.couloir)

f.defiler()
print(f.couloir)
f.enfiler(1)
print(f.est_vide())
print(f.couloir)
print(f.taille())
print(f.sommet())

f.defiler()
f.defiler()
f.defiler()
print(f.est_vide())'''