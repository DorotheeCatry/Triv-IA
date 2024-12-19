
from case import Case
from utils import code_couleur
import random


class Plateau:
    

    def __init__(self, cases=[]):

        self.cases = cases


    def creation_cases(self):
        types_possibles = ['Camembert', 'Normale']
        categories = ['Base de données', 'Python', 'Unix', 'Actu IA', 'Devops',"Personnalité de l'IA"]


        cat_cam = categories.copy()
        for i in range(36):
            if i == 0 or i % 6 == 0:
                cat_case = random.choice(cat_cam)
                cat_cam.remove(cat_case)
                new_case = Case(categorie= cat_case,position = i, type = types_possibles[0])
                self.cases.append(new_case)
                cat = categories.copy()
                cat.remove(cat_case)


            else:
                cat_case_normale = random.choice(cat)
                cat.remove(cat_case_normale)
                new_case = Case(categorie= cat_case_normale,position = i, type = types_possibles[1])
                self.cases.append(new_case)

    def creer_plateau(self, joueur):

        types_possibles = ['Camembert', 'Normale']
        categories = ['Base de données', 'Python', 'Unix', 'Actu IA', 'Devops',"Personnalité de l'IA"]

        code_couleur = [
                    ["🟦",  'Base de données'],
                    ["🟩",  'Python'],
                    ["🟥",  'Unix'],
                    ["🟨",  'Actua Ia'],
                    ["🟧",  'Devops'],
                    ["🟪",  "Personnalités de l'IA"]
                ]
        
        emojis = [
            "🟦",  # Carré bleu
            "🟩",  # Carré vert
            "🟥",  # Carré rouge
            "🟨",  # Carré jaune
            "🟧",  # Carré orange
            "🟪",  # Carré violet
        ]

        emojis_ronds = [
            "🔵",  # Cercle bleu
            "🟢",  # Cercle vert
            "🔴",  # Cercle rouge
            "🟡",  # Cercle jaune
            "🟠",  # Cercle orange
            "🟣",  # Cercle violet
        ]

        for i in range(12):
            
            if i == joueur[0].position:
                print(joueur[1], end = '    ')

            
            else:
                if self.cases[i].categorie == categories[0]:
                    if self.cases[i].type == types_possibles[0]:
                        print(emojis_ronds[0], end = '    ')
                    else:
                        print(emojis[0], end = '   ')

                elif self.cases[i].categorie == categories[1]:
                    if self.cases[i].type == types_possibles[0]:
                        print(emojis_ronds[1], end = '    ')
                    else:
                        print(emojis[1], end = '   ')

                elif self.cases[i].categorie == categories[2]:
                    if self.cases[i].type == types_possibles[0]:
                        print(emojis_ronds[2], end = '    ')
                    else:
                        print(emojis[2], end = '   ')

                elif self.cases[i].categorie == categories[3]:
                    if self.cases[i].type == types_possibles[0]:
                        print(emojis_ronds[3], end = '    ')
                    else:
                        print(emojis[3], end = '   ')

                elif self.cases[i].categorie == categories[4]:
                    if self.cases[i].type == types_possibles[0]:
                        print(emojis_ronds[4], end = '    ')
                    else:
                        print(emojis[4], end = '  ')

                elif self.cases[i].categorie == categories[5]:
                    if self.cases[i].type == types_possibles[0]:
                        print(emojis_ronds[5], end = '    ')
                    else:
                        print(emojis[5], end = '   ')
                    



        c = 35
        c1 = 12
        while c >= 30:
            if c == joueur[0].position :
                print(joueur[1], end = '    ') 

            else:


                if self.cases[c-1].categorie == categories[0]:
                    if self.cases[c-1].type == types_possibles[0]:
                        print(emojis_ronds[0], end = '    ')
                    else:
                        print(emojis[0], end = '   ')

                elif self.cases[c-1].categorie == categories[1]:
                    if self.cases[c-1].type == types_possibles[0]:
                        print(emojis_ronds[1], end = '    ')
                    else:
                        print(emojis[1], end = '   ')

                elif self.cases[c-1].categorie == categories[2]:
                    if self.cases[c-1].type == types_possibles[0]:
                        print(emojis_ronds[2], end = '    ')
                    else:
                        print(emojis[2], end = '   ')

                elif self.cases[c-1].categorie == categories[3]:
                    if self.cases[c-1].type == types_possibles[0]:
                        print(emojis_ronds[3], end = '    ')
                    else:
                        print(emojis[3], end = '   ')

                elif self.cases[c-1].categorie == categories[4]:
                    if self.cases[c-1].type == types_possibles[0]:
                        print(emojis_ronds[4], end = '   ')
                    else:
                        print(emojis[4], end = '   ')

                elif self.cases[c-1].categorie == categories[5]:
                    if self.cases[c-1].type == types_possibles[0]:
                        print(emojis_ronds[5], end = '    ')
                    else:
                        print(emojis[5], end = '   ')
                    
            print(' '* 49, end = '   ')
        
            if c1 == joueur[0].position:
                print(joueur[1], end = '    ')
            
            else:

                if self.cases[c1-1].categorie == categories[0]:
                    if self.cases[c1-1].type == types_possibles[0]:       
                        print(emojis_ronds[0], end='\n\n')
                    else:
                        print(emojis[0], end='\n\n')

                elif self.cases[c1-1].categorie == categories[1]:
                    if self.cases[c1-1].type == types_possibles[0]:       
                        print(emojis_ronds[1], end='\n\n')
                    else:
                        print(emojis[1], end='\n\n')

                elif self.cases[c1-1].categorie == categories[2]:
                    if self.cases[c1-1].type == types_possibles[0]:       
                        print(emojis_ronds[2], end='\n\n')
                    else:
                        print(emojis[2], end='\n\n')

                elif self.cases[c1-1].categorie == categories[3]:
                    if self.cases[c1-1].type == types_possibles[0]:       
                        print(emojis_ronds[3], end='\n\n')
                    else:
                        print(emojis[3], end='\n\n')

                elif self.cases[c1-1].categorie == categories[4]:
                    if self.cases[c1-1].type == types_possibles[0]:       
                        print(emojis_ronds[4], end='\n\n')
                    else:
                        print(emojis[4], end='\n\n')

                elif self.cases[c1-1].categorie == categories[5]:
                    if self.cases[c1-1].type == types_possibles[0]:       
                        print(emojis_ronds[5], end='\n\n')
                    else:
                        print(emojis[5], end='\n\n')

            c -= 1
            c1 +=1


        for i in range(29, 17, -1):
                
            if i == joueur[0].position:
                print(joueur[1], end = '    ')

            else:

                if self.cases[i].categorie == categories[0]:
                    if self.cases[i].type == types_possibles[0]:
                        print(emojis_ronds[0], end = '    ')
                    else:
                        print(emojis[0], end = '   ')

                elif self.cases[i].categorie == categories[1]:
                    if self.cases[i].type == types_possibles[0]:
                        print(emojis_ronds[1], end = '    ')
                    else:
                        print(emojis[1], end = '   ')

                elif self.cases[i].categorie == categories[2]:
                    if self.cases[i].type == types_possibles[0]:
                        print(emojis_ronds[2], end = '    ')
                    else:
                        print(emojis[2], end = '   ')

                elif self.cases[i].categorie == categories[3]:
                    if self.cases[i].type == types_possibles[0]:
                        print(emojis_ronds[3], end = '    ')
                    else:
                        print(emojis[3], end = '   ')

                elif self.cases[i].categorie == categories[4]:
                    if self.cases[i].type == types_possibles[0]:
                        print(emojis_ronds[4], end = '    ')
                    else:
                        print(emojis[4], end = '   ')

                elif self.cases[i].categorie == categories[5]:
                    if self.cases[i].type == types_possibles[0]:
                        print(emojis_ronds[5], end = '    ')
                    else:
                        print(emojis[5], end = '   ')
        print('\n\n\n==========================================\n\n')
        print( 
            f'{code_couleur[0][0]} = {code_couleur[0][1]}, '
            f'{code_couleur[1][0]} = {code_couleur[1][1]}, '
            f'{code_couleur[2][0]} = {code_couleur[2][1]}, '
            f'{code_couleur[3][0]} = {code_couleur[3][1]}, '
            f'{code_couleur[4][0]} = {code_couleur[4][1]}, '
            f'{code_couleur[5][0]} = {code_couleur[5][1]}')



    def get_case(self, i):
        return self.cases[i]


if __name__ == '__main__':
    partie = Plateau()

    partie.creation_cases()
    partie.creer_plateau()
    partie.creation_joueur()
    print(partie.joueurs)


    