"""! Vue principale du jeu
Ce module contient les fonctions de base utile à la vue du jeu.

Ce module permet de facilement avoir le menu sur toutes les fenêtres. De quitter
le jeu, de recommencer une partie, etc.

@see src/controller/ctrl_main.py
"""

import tkinter as tk

from src.controller import ctrl_main as ctrl_m

global tk_root


def win_init() -> tk.Tk:
    """! Initialise la fenêtre de jeu

    **Variables :**
    * tk_root : Fenêtre principale

    @return Fenêtre principale
    """
    global tk_root
    # Création de la fenêtre principale
    tk_root = tk.Tk()
    # Changement du titre de la fenêtre principale
    tk_root.title("Puissance 4")
    # Renvoie de la fenêtre créée
    return tk_root


def win_quit(tk_win_root: tk.Tk):
    """! Ferme la fenêtre de jeu

    **Préconditions :**
    * tk_root initialisé

    @param tk_win_root: Fenêtre principale
    """
    # Suppression de la fenêtre principale
    tk_win_root.quit()


def win_menu(tk_old_frame: tk.Frame) -> tk.Menu:
    """! Initialise le menu de la fenêtre de jeu

    **Variables :**
    * tkm_menu_bar : Menu de la fenêtre de jeu
    * tkm_menu_partie : sous-menu permettant de gérer la partie
    * tkm_menu_param : sous-menu permettant d'accéder aux paramètres
    * tkm_menu_a_propos : sous-menu permettant d'accéder à la page "À propos"

    @return Menu de la fenêtre de jeu
    """
    global tk_root
    # Création du menu
    tkm_menu_bar = tk.Menu()

    # Création du sous menu pour la partie
    tkm_menu_partie = tk.Menu(tkm_menu_bar, tearoff=False)
    # Ajout dans la barre de menu du sous menu.
    tkm_menu_bar.add_cascade(label="Partie",
                             menu=tkm_menu_partie)
    # Ajout d'une commande permettant de lancer une partie
    tkm_menu_partie.add_command(label="Nouvelle partie",
                                command=lambda:
                                ctrl_m.win_ctrl_page_play(tk_root,
                                                          tk_old_frame))
    # Ajout d'une commande permettant de relancer une partie
    tkm_menu_partie.add_command(label="Recommencer",
                                command=lambda:
                                ctrl_m.win_ctrl_page_play(tk_root,
                                                          tk_old_frame))
    # Ajout d'une commande permettant de quitter le jeu
    tkm_menu_partie.add_command(label="Quitter",
                                command=lambda: win_quit)

    # Ajout d'un bouton dans le menu pour accéder aux paramètres
    tkm_menu_bar.add_command(label="Paramètres",
                             command=lambda:
                             ctrl_m.win_ctrl_page_parameters(tk_root,
                                                             tk_old_frame))
    # Ajout d'un bouton dans le menu pour accéder à la page à propos
    tkm_menu_bar.add_command(label="A propos",
                             command=lambda: print("A propos"))
    # Renvoie du menu
    return tkm_menu_bar
