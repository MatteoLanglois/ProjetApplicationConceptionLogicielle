"""! @brief Un programme qui joue au jeu puissance 4++.

Ce programme est un jeu de puissance 4++ avec une grille de taille variable,
un nombre de pions à aligner variable, des bonus et un undo.

Ce programme utilise les modules externes suivants :
- tkinter
- numpy
- inspect

@package src.utils.widget_utils
@brief Ce module contient les fonctions relatives aux widgets.
@details Ce module contient les fonctions de gestion des widgets. Il permet de
gérer la taille de la fenêtre en fonction de la résolution de l'écran.
"""
import tkinter as tk


def wu_get_screen_size(tkf_frame: tk.Frame) -> (int, int):
    """! Récupère la taille de l'écran

    Cette fonction récupère la taille de l'écran et la renvoie sous la forme
    d'un tuple (largeur, hauteur).

    @param tkf_frame: Frame tkinter
    @pre Le cadre doit être initialisé
    @return Tuple (largeur, hauteur)
    """
    # Retourne la taille de l'écran
    return tkf_frame.winfo_screenwidth(), tkf_frame.winfo_screenheight()


def wu_get_grid_size(tkf_frame: tk.Frame) -> (int, int):
    """! Récupère la taille de la grille

    Cette fonction calcule la taille de la grille et la renvoie sous la forme
    d'un tuple (largeur, hauteur).

    @param tkf_frame: Frame tkinte
    @pre Le cadre doit être initialisé
    @return Tuple (largeur, hauteur)
    """
    # Récupère la taille de l'écran
    i_width_screen, i_height_screen = wu_get_screen_size(tkf_frame)

    # Si l'écran est en HD ou Full HD
    if i_width_screen <= 1920:
        # La largeur de la grille est de 500
        i_width_grid = 500
    # Si l'écran est en 2K
    elif i_width_screen <= 2560:
        # La largeur de la grille est de 700
        i_width_grid = 700
    # Si l'écran est en 4K
    elif i_width_screen <= 3840:
        # La largeur de la grille est de 900
        i_width_grid = 900
    # Sinon
    else:
        # La largeur de la grille est de 400
        i_width_grid = 400
    # On retourne la largeur et la hauteur de la grille, la hauteur de la
    # grille est de 6/7 de la largeur
    return i_width_grid, i_width_grid * 6/7


def wu_get_font_size(tkf_frame: tk.Frame, b_title: bool) -> int:
    """! Récupère la taille de la police

    Cette fonction calcule la taille de la police et la renvoie.

    @pre Le cadre doit être initialisé
    @param tkf_frame: Frame tkinter
    @param b_title: True si la police est pour un titre, False sinon
    @return Taille de la police
    """
    # Récupère la taille de l'écran
    i_width_screen, i_height_screen = wu_get_screen_size(tkf_frame)

    # Si l'écran est en HD ou Full HD
    if i_width_screen <= 1920:
        # La taille de la police est de 10
        i_font_size = 14
    # Si l'écran est en 2K
    elif i_width_screen <= 2560:
        # La taille de la police est de 15
        i_font_size = 16
    # Si l'écran est en 4K
    elif i_width_screen <= 3840:
        i_font_size = 20
    # Sinon
    else:
        # La taille de la police est de 10
        i_font_size = 14
    # Si la police est pour un titre
    if b_title:
        # On ajoute 10 à la taille de la police
        i_font_size += 5
    # On retourne la taille de la police
    return i_font_size
