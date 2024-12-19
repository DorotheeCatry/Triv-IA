from jeu import Jeu
import os
from plateau import Plateau

clear = os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    plateau_du_jeu = Plateau()


    plateau_du_jeu.creation_cases()
    # plateau_du_jeu.creer_plateau()

    partie = Jeu()
    partie.lancer_jeu()
    partie.lancer_manche()
