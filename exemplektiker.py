mport tkinter as tk
from tkinter import messagebox
import random

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.position = 0
        self.correct_answers = 0

    def lancer_de(self):
        return random.randint(1, 6)

    def deplacer(self, valeur_de, direction):
        if direction == "avant":
            self.position += valeur_de
        elif direction == "arrière":
            self.position -= valeur_de
        self.position %= 42  # Boucle infinie de 42 cases

class manche:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtu IA Poursuit")
        self.joueurs = []
        self.tour = 0
        self.questions = [
            Question("What is the capital of France?", "Paris"),
            Question("What is 2 + 2?", "4"),
            Question("Who wrote 'harry potter?", "JKR"),
            Question("What is the largest planet in our solar system?", "Jupiter")
        ]
        self.create_widgets()

    def create_widgets(self):
        self.info_label = tk.Label(self.root, text="Bienvenue au Jeu de l'oie")
        self.info_label.pack(pady=10)

        self.question_label = tk.Label(self.root, text="", wraplength=400)
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.root)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.direction_label = tk.Label(self.root, text="Choisissez la direction :")
        self.direction_label.pack(pady=10)

        self.direction_var = tk.StringVar(value="avant")
        self.direction_avant = tk.Radiobutton(self.root, text="Avant", variable=self.direction_var, value="avant")
        self.direction_avant.pack(pady=5)
        self.direction_arriere = tk.Radiobutton(self.root, text="Arrière", variable=self.direction_var, value="arrière")
        self.direction_arriere.pack(pady=5)

        self.lancer_button = tk.Button(self.root, text="Lancer le dé", command=self.jouer_tour)
        self.lancer_button.pack(pady=10)

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def poser_question(self):
        question = random.choice(self.questions)
        self.question_label.config(text=question.question)
        self.current_question = question

    def check_answer(self):
        reponse = self.answer_entry.get()
        if reponse.lower() == self.current_question.answer.lower():
            joueur_actuel = self.joueurs[self.tour % len(self.joueurs)]
            joueur_actuel.correct_answers += 1
            messagebox.showinfo("Correct!", f"Bonne réponse ! {joueur_actuel.nom} a maintenant {joueur_actuel.correct_answers} bonnes réponses.")
            if joueur_actuel.correct_answers == 4:
                messagebox.showinfo("Gagné!", f"{joueur_actuel.nom} a gagné en répondant correctement à 4 questions !")
                self.root.quit()
            else:
                self.jouer_tour()
        else:
            messagebox.showinfo("Incorrect", "Mauvaise réponse.")
            self.tour += 1
            self.jouer_tour()

    def jouer_tour(self):
        joueur_actuel = self.joueurs[self.tour % len(self.joueurs)]
        valeur_de = joueur_actuel.lancer_de()
        direction = self.direction_var.get()
        joueur_actuel.deplacer(valeur_de, direction)
        self.info_label.config(text=f"{joueur_actuel.nom} a lancé un {valeur_de} et se déplace à la case {joueur_actuel.position}")
        self.poser_question()

