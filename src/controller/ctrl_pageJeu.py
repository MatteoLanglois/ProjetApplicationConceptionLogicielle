"""! Contient le contrôleur de la page de jeu
Ce module contient les fonctions permettant de gérer la page de jeu.

@see src/view/view_pageJeu.py
"""
import tkinter as tk
from src.view import view_pageJeu as view_pj
from src.controller import ctrl_main as ctrl_m
from src.puissanceQuatre import puissanceQuatre as ps4
from src.puissanceQuatre import grid as gr

"""! Grille de jeu
@see src/puissanceQuatre/grid.py
"""
global npa_grid

"""! Fenêtre principale du jeu
@see src/controller/ctrl_main.py
"""
global tk_root


def ctrl_page_jeu_init(tk_win_root: tk.Tk):
    """! Initialise la page d'accueil

    **Variables :**
    * npa_grid : Grille de jeu

    **Préconditions :**
    * tk_root initialisé

    @param tk_win_root: Fenêtre principale
    """
    # Récupération de manière globale de la grille de jeu
    global npa_grid
    # Enregistrement de manière globale de la fenêtre principale
    global tk_root

    tk_root = tk_win_root
    # Initialisation de la page de jeu
    view_pj.v_page_jeu_init(tk_root)
    # Dessin de la grille de jeu
    ctrl_page_jeu_draw_grid()
    # Initialisation de la grille de jeu pour le puissance 4
    npa_grid = gr.pq_init_grille(6, 7)


def ctrl_page_jeu_draw_grid():
    """! Dessine la grille de jeu
    """
    # Dessin de la grille de jeu
    view_pj.v_page_jeu_draw_grid(6, 7)


def ctrl_page_jeu_put_coin():
    """! Place un jeton dans la grille de jeu
    @todo
    """


def ctrl_page_jeu_undo():
    """! Annule le dernier coup
    @todo
    """


def ctrl_page_jeu_redo():
    """! Refait le dernier coup
    @todo
    """


def ctrl_page_jeu_quit():
    """! Quitte la partie
    @todo
    """
    # Destruction de la page de jeu
    view_pj.v_page_jeu_destroy()
    # Fermeture de la fenêtre principale
    ctrl_m.win_ctrl_quit(tk_root)


def ctrl_page_jeu_play(event: tk.Event):
    """! Joue un coup dans la grille de jeu

    @param event: Evenement de la souris sur la grille de jeu
    @todo
    """
    # Affichage des coordonnées de la cellule sur laquelle on a cliquée
    print(view_pj.v_page_jeu_get_grid_cell(event.x, event.y))


def ctrl_page_jeu_bonus():
    """! Utilise un bonus
    @todo
    """