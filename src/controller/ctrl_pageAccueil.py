"""! @brief Un programme qui joue au jeu puissance 4++.

Ce programme est un jeu de puissance 4++ avec une grille de taille variable,
un nombre de pions à aligner variable, des bonus et un undo.

Ce programme utilise les modules externes suivants :
- tkinter
- numpy
- inspect

@package src.controller.ctrl_pageAccueil
@brief Un module qui gère la page d'accueil du jeu
@details Ce module gère la page d'accueil du jeu
"""
# Importations de tkinter
import tkinter as tk
# Importation de la vue de la page d'accueil
from src.view import view_pageAccueil as view_pa
# Importation du controller de la page principale afin de lancer une partie
from src.controller import ctrl_main as ctrl_m


def cpa_init(tk_root: tk.Tk):
    """! Initialise la page d'accueil

    Cette fonction initialise la page d'accueil du jeu.

    @pre tk_root initialisé
    @param tk_root: Fenêtre principale
    """
    # Initialisation de la page d'accueil
    view_pa.vpa_init(tk_root)


def cpa_play(tk_root: tk.Tk, tkf_frame: tk.Frame):
    """! Lance une partie

    Cette fonction lance une partie de puissance 4++. Elle est appelée lorsque
    l'utilisateur clique sur le bouton "Jouer".

    @pre tk_root initialisé
    @pre tkf_frame initialisé
    @param tk_root: Fenêtre principale
    @param tkf_frame: Frame de la page d'accueil
    @post Fenêtre de choix du bonus ouverte
    """
    ctrl_m.cm_page_bonus(tk_root, tkf_frame)
