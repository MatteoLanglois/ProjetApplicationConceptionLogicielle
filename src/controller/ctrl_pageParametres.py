"""! @file ctrl_pageParametres
Contrôleur de la page des paramètres

Contient les fonctions permettant de gérer la page des paramètres

"""
import tkinter as tk
from src.view import view_pageParametres as view_pp

global tk_root


def ctrl_page_parameter_init(tk_win_root: tk.Tk):
    """! Initialise la page des paramètres

    **Variables :**
    * tk_root : Fenêtre principale

    **Préconditions :**
    * tk_root initialisé

    @param tk_win_root: Fenêtre principale
    """
    global tk_root
    # Enregistrement de manière globale de la fenêtre principale
    tk_root = tk_win_root
    # Initialisation de la page des paramètres
    view_pp.v_page_parameter_init(tk_root)
