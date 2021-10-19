class uneCarte:
    def __init__(self, pdv, pdatk, effet, nom):
        self.vie = pdv
        self.atk = pdatk
        self.carte = [self.vie, self.atk, effet, nom]
        pass

    def afficherr(self):
        return self.carte

    def perdVie(self, carte1, carte2):
        carte1 [0] = carte1 [0] - carte2 [1]
        return carte1


    def perdvie(self,x):




