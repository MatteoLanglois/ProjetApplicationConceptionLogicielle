"""! @brief Un programme qui joue au jeu puissance 4++.

@mainpage Projet Puissance 4++

@section description_main Description
Ce programme est un jeu de puissance 4++ avec une grille de taille variable,
un nombre de pions à aligner variable, des bonus et un undo.

@section import_section Importations
Ce programme utilise les modules externes suivants :
- tkinter
- numpy

@package src.view.view_pageParametres
@brief Vue de la page des paramètres
@details La vue de la page des paramètres permet de gérer l'affichage de la page
des paramètres et traiter les paramètres.
"""

import tkinter as tk
from tkinter.colorchooser import askcolor

from src.controller import ctrl_main as ctrl_m
from src.controller import ctrl_pageParametres as ctrl_pp

global TKF_PAGE_PARAMETER
global STV_ROWS
global STV_COLUMNS
global STV_NB_JETONS
global TIS_CUSTOM_COLOR_JOUEUR
global TIS_CUSTOM_COLOR_BOT
global TIS_CUSTOM_COLOR_GRID
global TKB_PICKER_JOUEUR
global TKB_PICKER_BOT
global TKB_PICKER_GRID
global TKS_SCALE


def vpp_init(tk_root: tk.Tk):
    """! Fonction initialisant la page des paramètres

    **Variables :**
    * tkf_page_parameter : Frame de la page des paramètres

    **Préconditions :**
    * tk_root initialisé

    @param tk_root: La fenêtre principale
    """
    global TKF_PAGE_PARAMETER
    # Création d'un cadre pour la page d'accueil
    TKF_PAGE_PARAMETER = tk.Frame(tk_root, height=500, width=500, padx=50,
                                  pady=50)
    # Affichage du cadre de la page d'accueil
    TKF_PAGE_PARAMETER.grid(row=0, column=1, sticky="nsew")

    # Affichage du menu sur la fenêtre
    tk_root.configure(menu=ctrl_m.cm_menu(TKF_PAGE_PARAMETER, False))

    vpp_init_settings()
    vpp_init_custom()


def vpp_init_custom():
    global TKF_PAGE_PARAMETER, TIS_CUSTOM_COLOR_JOUEUR, TIS_CUSTOM_COLOR_BOT, \
        TKB_PICKER_JOUEUR, TKB_PICKER_BOT, TKB_PICKER_GRID
    # Création d'un label pour indiquer la seconde partie des paramètres
    tkl_perso = tk.Label(TKF_PAGE_PARAMETER, text="Personnalisation",
                         font="Helvetica 24")
    # Affichage du label
    tkl_perso.grid(row=6, column=1)

    # Création d'un label pour indiquer le choix de la couleur des jetons du
    # joueur
    tkl_color_joueur = tk.Label(TKF_PAGE_PARAMETER,
                                text="Couleur des jetons du joueur :",
                                font="Helvetica 16")
    # Affichage du label
    tkl_color_joueur.grid(row=7, column=0)

    # Création d'un bouton ouvrant un sélectionneur de couleur pour les jetons
    # du joueur
    TKB_PICKER_JOUEUR = tk.Button(TKF_PAGE_PARAMETER,
                                  font="Helvetica 16",
                                  command=lambda:
                                  ctrl_pp.ctrl_page_parameter_askcolor("joueur")
                                  )
    # Affichage du bouton
    TKB_PICKER_JOUEUR.grid(row=7, column=1)

    # Création d'un label pour indiquer le choix de la couleur des jetons du
    # bot
    tkl_color_bot = tk.Label(TKF_PAGE_PARAMETER,
                             text="Couleur des jetons du bot :",
                             font="Helvetica 16")
    # Affichage du Label
    tkl_color_bot.grid(row=8, column=0)

    # Création d'un bouton ouvrant un sélectionneur de couleur pour les jetons
    # du bot
    TKB_PICKER_BOT = tk.Button(TKF_PAGE_PARAMETER,
                               font="Helvetica 16",
                               command=lambda:
                               ctrl_pp.ctrl_page_parameter_askcolor("bot")
                               )
    # Affichage du bouton
    TKB_PICKER_BOT.grid(row=8, column=1)

    # Création d'un label pour indiquer le choix de la couleur de la grille
    tkl_color_grid = tk.Label(TKF_PAGE_PARAMETER,
                              text="Couleur de la grille :",
                              font="Helvetica 16")
    # Affichage du label
    tkl_color_grid.grid(row=9, column=0)

    # Création d'un bouton ouvrant un sélectionneur de couleur pour la grille
    TKB_PICKER_GRID = tk.Button(TKF_PAGE_PARAMETER,
                                font="Helvetica 16",
                                command=lambda:
                                ctrl_pp.ctrl_page_parameter_askcolor("grille")
                                )
    # Affichage du bouton
    TKB_PICKER_GRID.grid(row=9, column=1)

    tkb_save = tk.Button(TKF_PAGE_PARAMETER, text="Enregistrer",
                         font="Helvetica 16",
                         command=lambda:
                         ctrl_pp.ctrl_page_parameter_custom_save()
                         )
    tkb_save.grid(row=10, column=1)

    tkb_reset = tk.Button(TKF_PAGE_PARAMETER, text="Réinitialiser",
                          font="Helvetica 16",
                          command=lambda:
                          ctrl_pp.ctrl_page_parameter_custom_reset()
                          )
    tkb_reset.grid(row=10, column=2)


def vpp_init_settings():
    global TKF_PAGE_PARAMETER, STV_ROWS, STV_COLUMNS, STV_NB_JETONS, TKS_SCALE
    # Ajout d'un label pour "Paramètres"
    tkl_param = tk.Label(TKF_PAGE_PARAMETER, text="Paramètres",
                         font="Helvetica 24")
    # Affichage du label
    tkl_param.grid(row=1, column=1)

    # Création d'un label pour demander la taille de la grille
    tkl_size = tk.Label(TKF_PAGE_PARAMETER, text="Taille de la grille :",
                        font="Helvetica 16", justify="left")
    # Affichage du label
    tkl_size.grid(row=2, column=0)

    # Initialisation d'un stringVar pour récupérer la valeur du champ suivant
    STV_ROWS = tk.StringVar()
    # Création d'une spinbox pour le nombre de lignes
    tksb_nb_rows = tk.Spinbox(TKF_PAGE_PARAMETER, font="Helvetica 16", from_=4,
                              to=100, textvariable=STV_ROWS, width=5)
    # Affichage de l'entrée
    tksb_nb_rows.grid(row=2, column=1)

    tkl_lines = tk.Label(TKF_PAGE_PARAMETER, text="Lignes")
    tkl_lines.grid(row=2, column=2)

    # Initialisation d'un stringVar pour récupérer la valeur du champ suivant
    STV_COLUMNS = tk.StringVar()
    # Création d'une spinbox pour le nombre de colonnes
    tksb_nb_columns = tk.Spinbox(TKF_PAGE_PARAMETER, font="Helvetica 16",
                                 from_=5, to=110, textvariable=STV_COLUMNS)
    # Affichage de l'entrée
    tksb_nb_columns.grid(row=2, column=3)

    tkl_colonnes = tk.Label(TKF_PAGE_PARAMETER, text="Colonnes")
    tkl_colonnes.grid(row=2, column=4)

    # Création d'un label pour demander le nombre de jetons requis
    tkl_nb_jetons = tk.Label(TKF_PAGE_PARAMETER,
                             text="Nombre de jetons requis :",
                             font="Helvetica 16", justify="left")
    # Affichage du label
    tkl_nb_jetons.grid(row=3, column=0)

    # Initialisation d'un stringVar pour récupérer la valeur du champ suivant
    STV_NB_JETONS = tk.StringVar()
    # Création d'une spinbox pour le nombre de jetons requis pour gagner
    tksb_nb_jetons = tk.Spinbox(TKF_PAGE_PARAMETER, font="Helvetica 16",
                                from_=1, to=100, textvariable=STV_NB_JETONS)
    # Affichage de l'entrée
    tksb_nb_jetons.grid(row=3, column=1)

    # Création d'un label
    tkl_difficulty = tk.Label(TKF_PAGE_PARAMETER,
                              text="Difficulté",
                              font="Helvetica 16", justify="left")
    # Affichage du label
    tkl_difficulty.grid(row=4, column=0)

    # Création d'un slider pour la difficulté
    TKS_SCALE = tk.Scale(TKF_PAGE_PARAMETER, from_=0, to=5, orient="horizontal")
    # Affichage du slider
    TKS_SCALE.grid(row=4, column=1)

    tkb_save = tk.Button(TKF_PAGE_PARAMETER, text="Enregistrer",
                         font="Helvetica 16",
                         command=
                         lambda: ctrl_pp.ctrl_page_parameter_settings_save())
    tkb_save.grid(row=5, column=1)

    tkb_reset = tk.Button(TKF_PAGE_PARAMETER, text="Réinitialiser",
                          font="Helvetica 16",
                          command=
                          lambda: ctrl_pp.ctrl_page_parameter_settings_reset())
    tkb_reset.grid(row=5, column=2)


def vpp_get_nb_rows():
    global STV_ROWS
    return int(STV_ROWS.get())


def vpp_get_nb_columns():
    global STV_COLUMNS
    return int(STV_COLUMNS.get())


def vpp_get_nb_jetons():
    global STV_NB_JETONS
    return int(STV_NB_JETONS.get())


def vpp_get_difficulty():
    global TKS_SCALE
    return int(TKS_SCALE.get())


def vpp_set_nb_rows(i_rows: int):
    STV_ROWS.set(str(i_rows))


def vpp_set_nb_columns(i_columns: int):
    STV_COLUMNS.set(str(i_columns))


def vpp_set_nb_jetons(i_nb_jetons: int):
    STV_NB_JETONS.set(str(i_nb_jetons))


def vpp_set_difficulty(i_difficulty):
    global TKS_SCALE
    TKS_SCALE.set(i_difficulty)


def v_page_parameter_reset_settings():
    vpp_set_nb_rows(6)
    vpp_set_nb_columns(7)
    vpp_set_nb_jetons(4)
    vpp_set_difficulty(0)


def vpp_get_joueur_color():
    global TIS_CUSTOM_COLOR_JOUEUR
    return TIS_CUSTOM_COLOR_JOUEUR


def vpp_get_bot_color():
    global TIS_CUSTOM_COLOR_BOT
    return TIS_CUSTOM_COLOR_BOT


def vpp_get_grid_color():
    global TIS_CUSTOM_COLOR_GRID
    return TIS_CUSTOM_COLOR_GRID


def vpp_set_joueur_color(s_color: str):
    global TIS_CUSTOM_COLOR_JOUEUR, TKB_PICKER_JOUEUR
    TIS_CUSTOM_COLOR_JOUEUR = s_color
    TKB_PICKER_JOUEUR.configure(bg=s_color)


def vpp_set_bot_color(s_color: str):
    global TIS_CUSTOM_COLOR_BOT, TKB_PICKER_BOT
    TIS_CUSTOM_COLOR_BOT = s_color
    TKB_PICKER_BOT.configure(bg=s_color)


def vpp_set_grid_color(s_color: str):
    global TIS_CUSTOM_COLOR_GRID, TKB_PICKER_GRID
    TIS_CUSTOM_COLOR_GRID = s_color
    TKB_PICKER_GRID.configure(bg=s_color)


def vpp_reset_customs():
    vpp_set_joueur_color("#ff0000")
    vpp_set_bot_color("#ffff00")
    vpp_set_grid_color("#5064F1")


def vpp_askcolor(s_element: str):
    """! Ouvre un sélecteur de couleur
    """
    s_colors = f"{askcolor(title=s_element)[1]}"
    if s_element == "joueur":
        vpp_set_joueur_color(s_colors)
    elif s_element == "bot":
        vpp_set_bot_color(s_colors)
    else:
        vpp_set_grid_color(s_colors)
