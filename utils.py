import os



def clear_console():
    if os.name == 'nt':  # Si le système est Windows
        os.system('cls')
    else:  # Si le système est Linux ou macOS
        os.system('clear')


def clear_partial_ansi(lines_to_clear=1):
    # Déplace le curseur vers le haut (efface la ligne en cours)
    print(f"\033[{lines_to_clear}A", end="")  # Le curseur remonte de `lines_to_clear` lignes
    for _ in range(lines_to_clear):
        print("\033[K", end="")  # Efface la ligne à la position actuelle


dice_asci = [
    """
+-----+
|     |
|  *  |
|     |
+-----+
""",
    """
+-----+
| *   |
|     |
|   * |
+-----+
""",
    """
+-----+
| *   |
|  *  |
|   * |
+-----+
""",
    """
+-----+
| * * |
|     |
| * * |
+-----+
""",
    """
+-----+
| * * |
|  *  |
| * * |
+-----+
""",
    """
+-----+
| * * |
| * * |
| * * |
+-----+
"""
]

code_couleur = [[
            ["🟦",  'Base de données'],
            ["🟩",  'Python'],
            ["🟥",  'Unix'],
            ["🟨",  'Actua Ia'],
            ["🟧",  'Devops'],
            ["🟪",  "Personnalités de l'IA"]
        ]]