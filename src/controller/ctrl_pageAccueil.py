"""! Controller de la page d'accueil
Ce module contient les fonctions permettant de gérer la page d'accueil.
"""
import tkinter as tk
from src.controller import ctrl_pageJeu as ctrl_pj
from src.view import view_PageAccueil as view_pa


def ctrl_page_accueil_init(tk_root: tk.Tk):
    """! Initialise la page d'accueil

    **Préconditions :**
    * tk_root initialisé

    @param tk_root: Fenêtre principale
    """
    # Initialisation de la page d'accueil
    view_pa.v_page_accueil_init(tk_root)


def ctrl_page_accueil_play(tk_root: tk.Tk):
    """! Permet de lancer une partie

    @param tk_root: La fenêtre principale
    """
    # Destruction de la page d'accueil
    view_pa.v_page_accueil_destroy()
    # Initialisation de la page de jeu
    ctrl_pj.ctrl_page_jeu_init(tk_root)
