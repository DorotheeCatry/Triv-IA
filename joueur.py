import random

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.camemberts = []  # Ensemble pour stocker les couleurs de camemberts gagnés
        self.position = 0  # Position actuelle du joueur sur le plateau

    def ajouter_camembert(self, categorie):
        """Ajoute un camembert de categorie spécifique au joueur."""
        self.camemberts.append(categorie)
        print("\n", "🧀"*25)
        print(f"\n\n{self.nom} a gagné un camembert de categorie {categorie} !")
        print("\n\n","🧀"*25)

    def a_tous_les_camemberts(self):
        """Vérifie si le joueur a collecté les 6 camemberts."""
        if len(self.camemberts) == 1:
            return True

    def lancer_de(self):
        """Simule le lancer du dé."""
        return random.randint(1, 6)
