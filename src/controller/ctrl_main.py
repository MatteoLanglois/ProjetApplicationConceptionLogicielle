"""! Contrôleur de la fenêtre globale
Ce module contient les fonctions permettant de gérer la fenêtre globale.
"""

import tkinter as tk
from src.controller import ctrl_pageAccueil as ctrl_pa
from src.view import view_main as view_m


def win_ctrl_init():
    """! Initialise la fenêtre de jeu

    **Variables :**
    * tk_root : Fenêtre principale

    **Préconditions :**
    * tk_root initialisé
    """
    # Initialisation de la fenêtre
    tk_root = view_m.win_init()
    # Initialisation de la page d'accueil
    ctrl_pa.ctrl_page_accueil_init(tk_root)
    # Affichage du menu sur toutes les fenêtres
    tk_root.configure(menu=win_ctrl_menu())
    # Boucle principale
    tk.mainloop()


def win_ctrl_quit(tk_root: tk.Tk):
    """! Ferme la fenêtre de jeu

    **Préconditions :**
    * tk_root initialisé

    @param tk_root: Fenêtre principale
    """
    # Fermeture de la fenêtre
    view_m.win_quit(tk_root)


def win_ctrl_menu() -> tk.Menu:
    """! Crée le menu de la fenêtre

    @return Menu de la fenêtre
    """
    # Création du menu
    return view_m.win_menu()
