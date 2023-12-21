"""! Controller de la page d'accueil
Ce module contient les fonctions permettant de gérer la page d'accueil.
"""
import tkinter as tk
from src.view import view_PageAccueil as view_pa


def ctrl_page_accueil_init(tk_root: tk.Tk):
    """! Initialise la page d'accueil

    **Préconditions :**
    * tk_root initialisé

    @param tk_root: Fenêtre principale
    """
    # Initialisation de la page d'accueil
    view_pa.v_page_accueil_init(tk_root)
