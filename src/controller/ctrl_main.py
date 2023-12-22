"""! Contrôleur de la fenêtre globale
Ce module contient les fonctions permettant de gérer la fenêtre globale.
"""

import tkinter as tk
from src.controller import ctrl_pageAccueil as ctrl_pa
from src.controller import ctrl_pageJeu as ctrl_pj
from src.controller import ctrl_pageParametres as ctrl_pp
from src.view import view_main as view_m


def win_ctrl_init():
    """! Initialise la fenêtre de jeu

    **Variables :**
    * tk_root : Fenêtre principale

    \pre tk_root initialisé
    """
    # Initialisation de la fenêtre
    tk_root = view_m.win_init()
    # Initialisation de la page d'accueil
    ctrl_pa.ctrl_page_accueil_init(tk_root)
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


def win_ctrl_menu(tk_old_frame: tk.Frame, b_in_game: bool) -> tk.Menu:
    """! Crée le menu de la fenêtre

    @return Menu de la fenêtre
    """
    # Création du menu
    return view_m.win_menu(tk_old_frame, b_in_game)


def win_ctrl_page_play(tk_root: tk.Tk, tkf_old_frame: tk.Frame):
    """! Fonction permettant de passer à la fenêtre de jeu.

    @param tk_root: La fenêtre principale
    @param tkf_old_frame: Le cadre de la dernière fenêtre
    """
    # Efface le cadre
    tkf_old_frame.forget()
    # Supprime le cadre
    tkf_old_frame.destroy()
    # Initialise la page jeu
    ctrl_pj.ctrl_page_jeu_init(tk_root)


def win_ctrl_page_parameters(tk_root: tk.Tk, tkf_old_frame: tk.Frame):
    """! Fonction permettant de passer à la fenêtre de paramètres

    @param tk_root: La fenêtre principale
    @param tkf_old_frame: Le cadre de la dernière fenêtre
    """
    # Efface le cadre
    tkf_old_frame.forget()
    # Supprime le cadre
    tkf_old_frame.destroy()
    # Initialise la page de paramètres
    ctrl_pp.ctrl_page_parameter_init(tk_root)
