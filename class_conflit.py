from class_cartes import uneCarte

# la vie c'est à gauche

class conflit:
    def __init__(self, carte1, carte2):
        self.carte1 = list(carte1)
        self.carte2 = list(carte2)

    def perdVie(self, carteQuiDef, carteQuiAtk):
        carteQuiDef [0] = carteQuiDef [0] - carteQuiAtk [1]
        return carteQuiDef

    def calcul(self, carte1, carte2):
        '''' sachant que l'on modifie les listes self.carte venants de la classe uneCarte, on ne peux pas renommer ces listes avec par exemple self.carte1
        car on modifierait leurs noms respectifs, on doit donc les nommer avec de simples noms de variables pour qu'en sorti leurs noms respectifs n'aient pas                              changés'''

        print(carte1, carte2)
        self.carte1 = self.perdVie(carte1, carte2)
        self.carte2 = self.perdVie(carte2, carte1)
        return carte1, carte2


























petitTank = uneCarte(1, 2, "très petit", "Petit Tank")

moyenTank = uneCarte(2, 4, "moyennement moyen", "Moyen Tank")

grandTank = uneCarte(4, 8, "sacrément grand", "Grand Tank")

combat1 = conflit(petitTank.carte, moyenTank.carte)
print(combat1.calcul(petitTank.carte, moyenTank.carte))
print(petitTank.carte, moyenTank.carte)