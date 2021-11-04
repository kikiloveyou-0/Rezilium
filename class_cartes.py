class uneCarte:
    def __init__(self, pdv, pdatk, effet, nom):
        self.vie = pdv
        self.atk = pdatk
        self.carte = [self.vie, self.atk, effet, nom]
        pass

    def afficher(self):
        return self.carte
   

    def perdVie(self, attaquant):
        self.vie = self.vie - attaquant.atk
        return self.vie
