from plateau import Plateau
from joueur import Joueur
from utils import clear_console, clear_partial_ansi, dice_asci
import json
import random
import time


class Jeu:
    def __init__(self):
        self.joueurs = []
        self.tour_actuel = 0
        self.plateau = Plateau()

    def initialiser_joueurs(self):
        nb_joueurs = input('\n Veuillez saisir un nombre de joueur(max 6 joueurs)   ')

        animaux = [
            "🐱",  # Chat
            "🐶",  # Chien
            "🐻",  # Ours
            "🐸",  # Grenouille
            "🐯",  # Tigre
            "🐧"   # Pingouin
        ]


        for i in range(int(nb_joueurs)):

            nom_du_joueur = input(f'saisissez le nom du joueur {i + 1} : ')


            emoji_joueur = random.choice(animaux)
            animaux.remove(emoji_joueur)
            print(f"vous êtes l'emoji {emoji_joueur}")
            nouveau_joueur = Joueur(nom= nom_du_joueur)
            self.joueurs.append([nouveau_joueur, emoji_joueur])



    def lancer_manche(self):
        clear_console()
        """Exécute une manche du jeu."""
        joueur = self.joueurs[self.tour_actuel][0]
        element_joueurs = self.joueurs[self.tour_actuel]



        print(f"\nC'est au tour de {joueur.nom} !")

 

        self.plateau.creer_plateau(element_joueurs)

        # Lancer le dé

        print('')
        for i in range(11):
            print(dice_asci[i%5])
            time.sleep(0.2)
            clear_partial_ansi(6)
            clear_partial_ansi(1)




        print('===============================================')
        resultat = joueur.lancer_de()
        print(f"{joueur.nom} a lancé le dé et a obtenu : {resultat}   {dice_asci[resultat - 1]}")
        
        
        # Déplacer le joueur

        case = self.plateau.get_case(joueur.position)
        choix_mouvement = input('Si vous voulez aller en avant tapez av pour aller en arriere tapez ar ')
        if choix_mouvement != 'ar' and choix_mouvement != 'av':
            choix_mouvement = input('Si vous voulez aller en avant tapez av pour aller en arriere tapez ar ')
        else:
            if choix_mouvement == 'av':
                joueur.position += resultat
            else:
                choix_mouvement == 'ar'
                joueur.position -= resultat

        joueur.position = joueur.position % (len(self.plateau.cases))
        
        self.plateau.creer_plateau(element_joueurs)


            
        print(f"\n\n{joueur.nom} se trouve maintenant sur une case {self.plateau.cases[joueur.position].categorie}.")


        if self.poser(joueur.position):
            print("Bonne réponse ! 🎉")
            if  case.categorie not in joueur.camemberts and case.type == 'Camembert':
                print('===============================================')
                joueur.ajouter_camembert(case.categorie)

                # Vérifier si le joueur a gagné

                if joueur.a_tous_les_camemberts():
                    print(f"\nFélicitations {joueur.nom}, vous avez gagné le jeu ! 🎉")
                    return True

            # Si bonne réponse, rejouer
            print(f"{joueur.nom} rejoue !")
            time.sleep(1)
            clear_console()
            return False  # Le joueur continue de jouer

        else:
            print("Mauvaise réponse 😞.")
            time.sleep(1)
            clear_console()
            self.tour_actuel = (self.tour_actuel +1 ) % len(self.joueurs)
            return False

    def poser(self, case_joueur):
        """Pose la question au joueur et retourne s'il a répondu correctement."""
        with open('questions_trivial_pursuit.json', 'r') as files:
            question = json.load(files)

        case_actuelle = self.plateau.cases[case_joueur]
        cat_question = self.plateau.cases[case_joueur].categorie
        case_type = self.plateau.cases[case_joueur].type
        question_posee = random.choice(question[cat_question])

        print(f"\nQuestion ({cat_question}): {question_posee['question']}")
        for i, reponse in enumerate(question_posee['reponses'], 1):
            print(f"{i}. {reponse}")

        choix = input("Votre réponse (numéro) : ")
        while not choix.isdigit() or not (1 <= int(choix) <= 4):
            print("Entrée invalide. Réessayez.")
            choix = input("Votre réponse (numéro) : ")

        return int(choix) - 1 == question_posee['bonne_reponse']





    def lancer_jeu(self):
        """Lance le jeu complet."""
        print("Bienvenue dans le jeu !")
        self.initialiser_joueurs()
        
        while not self.lancer_manche():     
            pass



if __name__ == '__main__':
    plateau_du_jeu = Plateau()


    plateau_du_jeu.creation_cases()
    # plateau_du_jeu.creer_plateau()

    partie = Jeu()
    partie.lancer_jeu()
    partie.lancer_manche()