"""! @brief Un programme qui joue au jeu puissance 4++.

@mainpage Projet Puissance 4++

@section description_main Description
Ce programme est un jeu de puissance 4++ avec une grille de taille variable,
un nombre de pions à aligner variable, des bonus et un undo.

@section import_section Importations
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


def cpa_init(tk_root: tk.Tk):
    """! Initialise la page d'accueil

    @pre tk_root initialisé
    @param tk_root: Fenêtre principale
    """
    # Initialisation de la page d'accueil
    view_pa.vpa_init(tk_root)
