"""! view_pageParametres
Vue de la page des paramètres

La vue de la page des paramètres permet de gérer l'affichage de la page des
paramètres et traiter les paramètres.
"""

import tkinter as tk
from tkinter.colorchooser import askcolor

from src.controller import ctrl_main as ctrl_m
from src.controller import ctrl_pageParametres as ctrl_pp

global tkf_page_parameter
global stv_rows
global stv_columns
global stv_nb_jetons
global tis_custom_color_joueur
global tis_custom_color_bot
global tis_custom_color_grid
global tkb_picker_joueur
global tkb_picker_bot
global tkb_picker_grid
global tks_scale


def v_page_parameter_init(tk_root: tk.Tk):
    """! Fonction initialisant la page des paramètres

    **Variables :**
    * tkf_page_parameter : Frame de la page des paramètres

    **Préconditions :**
    * tk_root initialisé

    @param tk_root: La fenêtre principale
    """
    global tkf_page_parameter
    # Création d'un cadre pour la page d'accueil
    tkf_page_parameter = tk.Frame(tk_root, height=500, width=500, padx=50,
                                  pady=50)
    # Affichage du cadre de la page d'accueil
    tkf_page_parameter.grid(row=0, column=1, sticky="nsew")

    # Affichage du menu sur la fenêtre
    tk_root.configure(menu=ctrl_m.win_ctrl_menu(tkf_page_parameter, False))

    v_page_parameter_init_settings()
    v_page_parameter_init_custom()


def v_page_parameter_init_custom():
    global tkf_page_parameter, tis_custom_color_joueur, tis_custom_color_bot, \
        tkb_picker_joueur, tkb_picker_bot, tkb_picker_grid
    # Création d'un label pour indiquer la seconde partie des paramètres
    tkl_perso = tk.Label(tkf_page_parameter, text="Personnalisation",
                         font="Helvetica 24")
    # Affichage du label
    tkl_perso.grid(row=6, column=1)

    # Création d'un label pour indiquer le choix de la couleur des jetons du
    # joueur
    tkl_color_joueur = tk.Label(tkf_page_parameter,
                                text="Couleur des jetons du joueur :",
                                font="Helvetica 16")
    # Affichage du label
    tkl_color_joueur.grid(row=7, column=0)

    # Création d'un bouton ouvrant un sélectionneur de couleur pour les jetons
    # du joueur
    tkb_picker_joueur = tk.Button(tkf_page_parameter,
                                  font="Helvetica 16",
                                  command=lambda:
                                  ctrl_pp.ctrl_page_parameter_askcolor("joueur")
                                  )
    # Affichage du bouton
    tkb_picker_joueur.grid(row=7, column=1)

    # Création d'un label pour indiquer le choix de la couleur des jetons du
    # bot
    tkl_color_bot = tk.Label(tkf_page_parameter,
                             text="Couleur des jetons du bot :",
                             font="Helvetica 16")
    # Affichage du Label
    tkl_color_bot.grid(row=8, column=0)

    # Création d'un bouton ouvrant un sélectionneur de couleur pour les jetons
    # du bot
    tkb_picker_bot = tk.Button(tkf_page_parameter,
                               font="Helvetica 16",
                               command=lambda:
                               ctrl_pp.ctrl_page_parameter_askcolor("bot")
                               )
    # Affichage du bouton
    tkb_picker_bot.grid(row=8, column=1)

    # Création d'un label pour indiquer le choix de la couleur de la grille
    tkl_color_grid = tk.Label(tkf_page_parameter,
                              text="Couleur de la grille :",
                              font="Helvetica 16")
    # Affichage du label
    tkl_color_grid.grid(row=9, column=0)

    # Création d'un bouton ouvrant un sélectionneur de couleur pour la grille
    tkb_picker_grid = tk.Button(tkf_page_parameter,
                                font="Helvetica 16",
                                command=lambda:
                                ctrl_pp.ctrl_page_parameter_askcolor("grille")
                                )
    # Affichage du bouton
    tkb_picker_grid.grid(row=9, column=1)

    tkb_save = tk.Button(tkf_page_parameter, text="Enregistrer",
                         font="Helvetica 16",
                         command=lambda:
                         ctrl_pp.ctrl_page_parameter_custom_save()
                         )
    tkb_save.grid(row=10, column=1)

    tkb_reset = tk.Button(tkf_page_parameter, text="Réinitialiser",
                          font="Helvetica 16",
                          command=lambda:
                          ctrl_pp.ctrl_page_parameter_custom_reset()
                          )
    tkb_reset.grid(row=10, column=2)


def v_page_parameter_init_settings():
    global tkf_page_parameter, stv_rows, stv_columns, stv_nb_jetons, tks_scale
    # Ajout d'un label pour "Paramètres"
    tkl_param = tk.Label(tkf_page_parameter, text="Paramètres",
                         font="Helvetica 24")
    # Affichage du label
    tkl_param.grid(row=1, column=1)

    # Création d'un label pour demander la taille de la grille
    tkl_size = tk.Label(tkf_page_parameter, text="Taille de la grille :",
                        font="Helvetica 16", justify="left")
    # Affichage du label
    tkl_size.grid(row=2, column=0)

    # Initialisation d'un stringVar pour récupérer la valeur du champ suivant
    stv_rows = tk.StringVar()
    # Création d'une spinbox pour le nombre de lignes
    tksb_nb_rows = tk.Spinbox(tkf_page_parameter, font="Helvetica 16", from_=4,
                              to=100, textvariable=stv_rows, width=5)
    # Affichage de l'entrée
    tksb_nb_rows.grid(row=2, column=1)

    tkl_lines = tk.Label(tkf_page_parameter, text="Lignes")
    tkl_lines.grid(row=2, column=2)

    # Initialisation d'un stringVar pour récupérer la valeur du champ suivant
    stv_columns = tk.StringVar()
    # Création d'une spinbox pour le nombre de colonnes
    tksb_nb_columns = tk.Spinbox(tkf_page_parameter, font="Helvetica 16",
                                 from_=5, to=110, textvariable=stv_columns)
    # Affichage de l'entrée
    tksb_nb_columns.grid(row=2, column=3)

    tkl_colonnes = tk.Label(tkf_page_parameter, text="Colonnes")
    tkl_colonnes.grid(row=2, column=4)

    # Création d'un label pour demander le nombre de jetons requis
    tkl_nb_jetons = tk.Label(tkf_page_parameter,
                             text="Nombre de jetons requis :",
                             font="Helvetica 16", justify="left")
    # Affichage du label
    tkl_nb_jetons.grid(row=3, column=0)

    # Initialisation d'un stringVar pour récupérer la valeur du champ suivant
    stv_nb_jetons = tk.StringVar()
    # Création d'une spinbox pour le nombre de jetons requis pour gagner
    tksb_nb_jetons = tk.Spinbox(tkf_page_parameter, font="Helvetica 16",
                                from_=1, to=100, textvariable=stv_nb_jetons)
    # Affichage de l'entrée
    tksb_nb_jetons.grid(row=3, column=1)

    # Création d'un label
    tkl_difficulty = tk.Label(tkf_page_parameter,
                              text="Difficulté",
                              font="Helvetica 16", justify="left")
    # Affichage du label
    tkl_difficulty.grid(row=4, column=0)

    # Création d'un slider pour la difficulté
    tks_scale = tk.Scale(tkf_page_parameter, from_=0, to=5, orient="horizontal")
    # Affichage du slider
    tks_scale.grid(row=4, column=1)

    tkb_save = tk.Button(tkf_page_parameter, text="Enregistrer",
                         font="Helvetica 16",
                         command=
                         lambda: ctrl_pp.ctrl_page_parameter_settings_save())
    tkb_save.grid(row=5, column=1)

    tkb_reset = tk.Button(tkf_page_parameter, text="Réinitialiser",
                          font="Helvetica 16",
                          command=
                          lambda: ctrl_pp.ctrl_page_parameter_settings_reset())
    tkb_reset.grid(row=5, column=2)


def v_page_parameter_get_nb_rows():
    global stv_rows
    return int(stv_rows.get())


def v_page_parameter_get_nb_columns():
    global stv_columns
    return int(stv_columns.get())


def v_page_parameter_get_nb_jetons():
    global stv_nb_jetons
    return int(stv_nb_jetons.get())


def v_page_parameter_get_difficulty():
    global tks_scale
    return int(tks_scale.get())


def v_page_parameter_set_nb_rows(i_rows: int):
    stv_rows.set(str(i_rows))


def v_page_parameter_set_nb_columns(i_columns: int):
    stv_columns.set(str(i_columns))


def v_page_parameter_set_nb_jetons(i_nb_jetons: int):
    stv_nb_jetons.set(str(i_nb_jetons))


def v_page_parameter_set_difficulty(i_difficulty):
    global tks_scale
    tks_scale.set(i_difficulty)


def v_page_parameter_reset_settings():
    v_page_parameter_set_nb_rows(6)
    v_page_parameter_set_nb_columns(7)
    v_page_parameter_set_nb_jetons(4)
    v_page_parameter_set_difficulty(0)


def v_page_parameter_get_joueur_color():
    global tis_custom_color_joueur
    return tis_custom_color_joueur


def v_page_parameter_get_bot_color():
    global tis_custom_color_bot
    return tis_custom_color_bot


def v_page_parameter_get_grid_color():
    global tis_custom_color_grid
    return tis_custom_color_grid


def v_page_parameter_set_joueur_color(s_color: str):
    global tis_custom_color_joueur, tkb_picker_joueur
    tis_custom_color_joueur = s_color
    tkb_picker_joueur.configure(bg=s_color)


def v_page_parameter_set_bot_color(s_color: str):
    global tis_custom_color_bot, tkb_picker_bot
    tis_custom_color_bot = s_color
    tkb_picker_bot.configure(bg=s_color)


def v_page_parameter_set_grid_color(s_color: str):
    global tis_custom_color_grid, tkb_picker_grid
    tis_custom_color_grid = s_color
    tkb_picker_grid.configure(bg=s_color)


def v_page_parameter_reset_customs():
    v_page_parameter_set_joueur_color("#ff0000")
    v_page_parameter_set_bot_color("#ffff00")
    v_page_parameter_set_grid_color("#5064F1")


def v_page_parameter_askcolor(s_element: str):
    """! Ouvre un sélecteur de couleur
    """
    s_colors = f"{askcolor(title=s_element)[1]}"
    if s_element == "joueur":
        v_page_parameter_set_joueur_color(s_colors)
    elif s_element == "bot":
        v_page_parameter_set_bot_color(s_colors)
    else:
        v_page_parameter_set_grid_color(s_colors)
