"""! view_pageParametres
Vue de la page des paramètres

La vue de la page des paramètres permet de gérer l'affichage de la page des
paramètres et traiter les paramètres.
"""

import tkinter as tk
from tkinter.colorchooser import askcolor

from src.controller import ctrl_main as ctrl_m

global tkf_page_parameter


def v_page_parameter_init(tk_root: tk.Tk):
    """! Fonction initialisant la page des paramètres

    **Variables :**
    * tkf_page_parameter : Frame de la page des paramètres
    * tkl_param : Label "Paramètres"
    * tkl_size : Label "Taille de la grille :"
    * tke_nb_rows : Entrée pour le nombre de lignes
    * tke_nb_columns : Entrée pour le nombre de colonnes
    * tkl_nb_jetons : Label "Nombre de jetons requis :"
    * tke_nb_jetons : Entrée pour le nombre de jetons requis
    * tkl_difficulty : Label "Difficulté"
    * tks_scale : Slider pour la difficulté
    * tkl_perso : Label "Personnalisation"
    * tkl_color_joueur : Label "Couleur des jetons du joueur :"
    * tkb_picker_joueur : Bouton pour ouvrir un sélectionneur de couleur pour
    les jetons du joueur
    * tkl_color_bot : Label "Couleur des jetons du bot :"
    * tkb_picker_bot : Bouton pour ouvrir un sélectionneur de couleur pour les
    jetons du bot
    * tkl_color_grid : Label "Couleur de la grille :"
    * tkb_picker_grid : Bouton pour ouvrir un sélectionneur de couleur pour la
    grille

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

    # Ajout d'un label pour "Paramètres"
    tkl_param = tk.Label(tkf_page_parameter, text="Paramètres",
                         font="Helvetica 24")
    # Affichage du label
    tkl_param.grid(row=1, column=1)

    # Création d'un label pour demander la taille de la grille
    tkl_size = tk.Label(tkf_page_parameter, text="Taille de la grille :",
                        font="Helvetica 16")
    # Affichage du label
    tkl_size.grid(row=2, column=0)

    # Initialisation d'un stringVar pour récupérer la valeur du champ suivant
    stv_rows = tk.StringVar()
    # Création d'une entrée pour le nombre de lignes
    tke_nb_rows = tk.Entry(tkf_page_parameter, font="Helvetica 16",
                           justify="center", textvariable=stv_rows)
    # Affichage de l'entrée
    tke_nb_rows.grid(row=2, column=1)

    # Initialisation d'un stringVar pour récupérer la valeur du champ suivant
    stv_columns = tk.StringVar()
    # Création d'une entrée pour le nombre de colonnes
    tke_nb_columns = tk.Entry(tkf_page_parameter, font="Helvetica 16",
                              justify="center", textvariable=stv_columns)
    # Affichage de l'entrée
    tke_nb_columns.grid(row=2, column=2)

    # Création d'un label pour demander le nombre de jetons requis
    tkl_nb_jetons = tk.Label(tkf_page_parameter,
                             text="Nombre de jetons requis :",
                             font="Helvetica 16")
    # Affichage du label
    tkl_nb_jetons.grid(row=3, column=0)

    # Initialisation d'un stringVar pour récupérer la valeur du champ suivant
    stv_nb_jetons = tk.StringVar()
    # Création d'une entrée pour le nombre de jetons requis pour gagner
    tke_nb_jetons = tk.Entry(tkf_page_parameter, font="Helvetica 16",
                             justify="center", textvariable=stv_nb_jetons)
    # Affichage de l'entrée
    tke_nb_jetons.grid(row=3, column=1)

    # Création d'un label
    tkl_difficulty = tk.Label(tkf_page_parameter,
                              text="Difficulté",
                              font="Helvetica 16")
    # Affichage du label
    tkl_difficulty.grid(row=4, column=0)

    # Création d'un slider pour la difficulté
    tks_scale = tk.Scale(tkf_page_parameter, from_=0, to=5, orient="horizontal")
    # Affichage du slider
    tks_scale.grid(row=4, column=1)

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
                                  command=lambda: askcolor()
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
                               command=lambda: askcolor()
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
                                command=lambda: askcolor()
                                )
    # Affichage du bouton
    tkb_picker_grid.grid(row=9, column=1)
