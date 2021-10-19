class uneCarte:
    def __init__(self, pdv, pdatk, effet):
        self.carte=[pdv, pdatk, effet]
        pass

    def afficherCarte(self):
        return self.carte

carte1 = uneCarte(10, 4, "effet")
print(carte1.carte)
