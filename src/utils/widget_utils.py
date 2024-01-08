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

@package src.utils.widget_utils
@brief Ce module contient les fonctions utiles pour créer les widgets tkinter
@details Ce module contient les fonctions utilitaires relatives aux widgets
tkinter. Il permet d'assurer une uniformité et une meilleure mise à l'échelle
des widgets.
"""
import tkinter as tk


def wu_i_get_font() -> str:
    """! Fonction qui retourne la police de caractères utilisée pour les widgets

    @return: La taille de la police en fonction de la taille de l'interface.
    """
    return "Helvetica 16"


def wu_tkb_init_button(tkf_frame: tk.Frame, s_text: str) -> tk.Button:
    """! Fonction qui initialise un bouton.

    @pre tkf_frame initialisé
    @param tkf_frame: Le cadre dans lequel le bouton sera affiché.
    @param s_text: Le texte du bouton.
    @return: Le bouton initialisé.
    @post Afficher le bouton.
    """
    s_font = wu_i_get_font()
    tkb_button = tk.Button(master=tkf_frame, text=s_text, font=s_font,
                           width=50)
    return tkb_button


def wu_tkl_init_label(tkf_frame: tk.Frame, s_text: str) -> tk.Label:
    s_font = wu_i_get_font()
    tkl_label = tk.Label(master=tkf_frame, text=s_text, font=s_font)
    return tkl_label


def wu_tksb_init_spinbox(tkf_frame: tk.Frame, i_from: int, i_to: int) \
        -> tk.Spinbox:
    s_font = wu_i_get_font()
    tksb_spinbox = tk.Spinbox(master=tkf_frame, from_=i_from, to=i_to,
                              font=s_font)
    return tksb_spinbox


def wu_tks_init_scale(tkf_frame: tk.Frame, i_from: int, i_to: int,
                      s_orient: str) -> tk.Scale:
    s_font = wu_i_get_font()
    tks_scale = tk.Scale(master=tkf_frame, from_=i_from, to=i_to,
                         font=s_font, orient=s_orient)
    return tks_scale
