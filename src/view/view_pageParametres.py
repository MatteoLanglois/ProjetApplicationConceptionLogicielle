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

@package src.view.view_pageParametres
@brief Vue de la page des paramètres
@details La vue de la page des paramètres permet de gérer l'affichage de la page
des paramètres et traiter les paramètres.
"""

# Importation de tkinter
import tkinter as tk
# Importation de la fonction askcolor pour le choix de la couleur
from tkinter.colorchooser import askcolor
# Importation du contrôleur principale pour le menu
from src.controller import ctrl_main as ctrl_m
# Importation du contrôleur de la page des paramètres
from src.controller import ctrl_pageParametres as ctrl_pp

# Variables globales ##########################
# Frame de la page des paramètres
global TKF_PAGE_PARAMETER
# StringVar pour le nombre de lignes
global STV_ROWS
# StringVar pour le nombre de colonnes
global STV_COLUMNS
# StringVar pour le nombre de jetons requis
global STV_NB_JETONS
# Tableau d'entier pour la couleur des jetons du joueur
global TIS_CUSTOM_COLOR_JOUEUR
# Tableau d'entier pour la couleur des jetons du bot
global TIS_CUSTOM_COLOR_BOT
# Tableau d'entier pour la couleur de la grille
global TIS_CUSTOM_COLOR_GRID
# Bouton pour ouvrir le sélecteur de couleur des jetons du joueur
global TKB_PICKER_JOUEUR
# Bouton pour ouvrir le sélecteur de couleur des jetons du bot
global TKB_PICKER_BOT
# Bouton pour ouvrir le sélecteur de couleur de la grille
global TKB_PICKER_GRID
# Slider pour la difficulté
global TKS_SCALE


def vpp_init(tk_root: tk.Tk):
    """! Fonction initialisant la page des paramètres

    Cette fonction initialise la page des paramètres. Elle crée un cadre et
    affiche le menu sur la fenêtre. Elle initialise aussi les paramètres de jeu
    et de personnalisation.

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
    # Initialisation des paramètres de jeu
    vpp_init_settings()
    # Initialisation des paramètres de personnalisation
    vpp_init_custom()


def vpp_init_custom():
    """! Fonction initialisant la partie personnalisation des paramètres

    Cette fonction initialise la partie personnalisation des paramètres. Elle
    crée des labels pour indiquer les choix de couleurs et des boutons pour
    ouvrir un sélecteur de couleur. Elle initialise aussi les couleurs par
    défaut.

    @pre TKF_PAGE_PARAMETER initialisé
    @post La partie personnalisation des paramètres est initialisée
    @post TKB_PICKER_JOUEUR, TKB_PICKER_BOT et TKB_PICKER_GRID sont initialisés

    **Variables :**
    * tkl_perso : Label pour indiquer la seconde partie des paramètres
    * tkl_color_joueur : Label pour indiquer le choix de la couleur des jetons
    du joueur
    * TKB_PICKER_JOUEUR : Bouton pour ouvrir un sélectionneur de couleur pour
    les jetons du joueur
    * tkl_color_bot : Label pour indiquer le choix de la couleur des jetons du
    bot
    * TKB_PICKER_BOT : Bouton pour ouvrir un sélectionneur de couleur pour les
    jetons du bot
    * tkl_color_grid : Label pour indiquer le choix de la couleur de la grille
    * TKB_PICKER_GRID : Bouton pour ouvrir un sélectionneur de couleur pour la
    grille
    * tkb_save : Bouton pour enregistrer les paramètres
    * tkb_reset : Bouton pour réinitialiser les paramètres
    """
    global TKF_PAGE_PARAMETER, TKB_PICKER_JOUEUR, TKB_PICKER_BOT, \
        TKB_PICKER_GRID
    # Création d'un label pour indiquer la seconde partie des paramètres
    tkl_perso = tk.Label(TKF_PAGE_PARAMETER, text="Personnalisation",
                         font="Helvetica 24")
    # Affichage du label
    tkl_perso.grid(row=6, column=1, pady=20)

    # Création d'un label pour indiquer le choix de la couleur des jetons du
    # joueur
    tkl_color_joueur = tk.Label(TKF_PAGE_PARAMETER,
                                text="Couleur des jetons du joueur :",
                                font="Helvetica 16")
    # Affichage du label
    tkl_color_joueur.grid(row=7, column=0, pady=10)

    # Création d'un bouton ouvrant un sélectionneur de couleur pour les jetons
    # du joueur
    TKB_PICKER_JOUEUR = tk.Button(TKF_PAGE_PARAMETER, width=3,
                                  font="Helvetica 16",
                                  command=lambda:
                                  ctrl_pp.cpp_askcolor("joueur")
                                  )
    # Affichage du bouton
    TKB_PICKER_JOUEUR.grid(row=7, column=1)

    # Création d'un label pour indiquer le choix de la couleur des jetons du
    # bot
    tkl_color_bot = tk.Label(TKF_PAGE_PARAMETER,
                             text="Couleur des jetons du bot :",
                             font="Helvetica 16")
    # Affichage du Label
    tkl_color_bot.grid(row=8, column=0, pady=10)

    # Création d'un bouton ouvrant un sélectionneur de couleur pour les jetons
    # du bot
    TKB_PICKER_BOT = tk.Button(TKF_PAGE_PARAMETER, width=3,
                               font="Helvetica 16",
                               command=lambda:
                               ctrl_pp.cpp_askcolor("bot")
                               )
    # Affichage du bouton
    TKB_PICKER_BOT.grid(row=8, column=1)

    # Création d'un label pour indiquer le choix de la couleur de la grille
    tkl_color_grid = tk.Label(TKF_PAGE_PARAMETER,
                              text="Couleur de la grille :",
                              font="Helvetica 16")
    # Affichage du label
    tkl_color_grid.grid(row=9, column=0, pady=10)

    # Création d'un bouton ouvrant un sélectionneur de couleur pour la grille
    TKB_PICKER_GRID = tk.Button(TKF_PAGE_PARAMETER, width=3,
                                font="Helvetica 16",
                                command=lambda:
                                ctrl_pp.cpp_askcolor("grille")
                                )
    # Affichage du bouton
    TKB_PICKER_GRID.grid(row=9, column=1)
    # Initialisation d'un bouton pour enregistrer les paramètres
    tkb_save = tk.Button(TKF_PAGE_PARAMETER, text="Enregistrer",
                         font="Helvetica 16",
                         command=lambda:
                         ctrl_pp.cpp_custom_save()
                         )
    # Affichage du bouton
    tkb_save.grid(row=10, column=1, pady=20)
    # Initialisation d'un bouton pour réinitialiser les paramètres
    tkb_reset = tk.Button(TKF_PAGE_PARAMETER, text="Réinitialiser",
                          font="Helvetica 16",
                          command=lambda:
                          ctrl_pp.cpp_custom_reset()
                          )
    # Affichage du bouton
    tkb_reset.grid(row=10, column=2)


def vpp_init_settings():
    """! Fonction initialisant la partie paramètres du jeu

    Cette fonction initialise la partie paramètres du jeu. Elle crée des labels
    pour indiquer les choix de paramètres et des spinbox pour choisir les
    paramètres. Elle initialise aussi les paramètres par défaut.

    @pre TKF_PAGE_PARAMETER initialisé
    @post La partie paramètres du jeu est initialisée

    **Variables :**
    * tkl_param : Label pour indiquer la première partie des paramètres
    * tkl_size : Label pour indiquer le choix de la taille de la grille
    * STV_ROWS : StringVar pour récupérer la valeur du nombre de lignes
    * tksb_nb_rows : Spinbox pour le nombre de lignes
    * tkl_lines : Label pour indiquer le nombre de lignes
    * STV_COLUMNS : StringVar pour récupérer la valeur du nombre de colonnes
    * tksb_nb_columns : Spinbox pour le nombre de colonnes
    * tkl_colonnes : Label pour indiquer le nombre de colonnes
    * tkl_nb_jetons : Label pour indiquer le choix du nombre de jetons requis
    * STV_NB_JETONS : StringVar pour récupérer la valeur du nombre de jetons
    requis
    * tksb_nb_jetons : Spinbox pour le nombre de jetons requis
    * tkl_difficulty : Label pour indiquer le choix de la difficulté
    * TKS_SCALE : Slider pour la difficulté
    * tkb_save : Bouton pour enregistrer les paramètres
    * tkb_reset : Bouton pour réinitialiser les paramètres
    """
    global TKF_PAGE_PARAMETER, STV_ROWS, STV_COLUMNS, STV_NB_JETONS, TKS_SCALE
    # Ajout d'un label pour "Paramètres"
    tkl_param = tk.Label(TKF_PAGE_PARAMETER, text="Paramètres",
                         font="Helvetica 24")
    # Affichage du label
    tkl_param.grid(row=1, column=1, pady=20)

    # Création d'un label pour demander la taille de la grille
    tkl_size = tk.Label(TKF_PAGE_PARAMETER, text="Taille de la grille :",
                        font="Helvetica 16", justify="left")
    # Affichage du label
    tkl_size.grid(row=2, column=0, pady=10)

    # Initialisation d'un stringVar pour récupérer la valeur du champ suivant
    STV_ROWS = tk.StringVar()
    # Création d'une spinbox pour le nombre de lignes
    tksb_nb_rows = tk.Spinbox(TKF_PAGE_PARAMETER, font="Helvetica 16", from_=4,
                              to=100, textvariable=STV_ROWS, width=5)
    # Affichage de l'entrée
    tksb_nb_rows.grid(row=2, column=1, padx=10, sticky="e")

    tkl_lines = tk.Label(TKF_PAGE_PARAMETER, text="Lignes,",
                         font="Helvetica 14")
    tkl_lines.grid(row=2, column=2, sticky="w")

    # Initialisation d'un stringVar pour récupérer la valeur du champ suivant
    STV_COLUMNS = tk.StringVar()
    # Création d'une spinbox pour le nombre de colonnes
    tksb_nb_columns = tk.Spinbox(TKF_PAGE_PARAMETER, font="Helvetica 16",
                                 from_=5, to=110, textvariable=STV_COLUMNS,
                                 width=5)
    # Affichage de l'entrée
    tksb_nb_columns.grid(row=2, column=3, padx=10, sticky="e")

    tkl_colonnes = tk.Label(TKF_PAGE_PARAMETER, text="Colonnes",
                            font="Helvetica 14")
    tkl_colonnes.grid(row=2, column=4, sticky="w")

    # Création d'un label pour demander le nombre de jetons requis
    tkl_nb_jetons = tk.Label(TKF_PAGE_PARAMETER,
                             text="Nombre de jetons requis :",
                             font="Helvetica 16", justify="left")
    # Affichage du label
    tkl_nb_jetons.grid(row=3, column=0, pady=10)

    # Initialisation d'un stringVar pour récupérer la valeur du champ suivant
    STV_NB_JETONS = tk.StringVar()
    # Création d'une spinbox pour le nombre de jetons requis pour gagner
    tksb_nb_jetons = tk.Spinbox(TKF_PAGE_PARAMETER, font="Helvetica 16",
                                from_=1, to=100, textvariable=STV_NB_JETONS,
                                width=5)
    # Affichage de l'entrée
    tksb_nb_jetons.grid(row=3, column=1, padx=10, sticky="w")

    # Création d'un label
    tkl_difficulty = tk.Label(TKF_PAGE_PARAMETER,
                              text="Difficulté",
                              font="Helvetica 16", justify="left")
    # Affichage du label
    tkl_difficulty.grid(row=4, column=0, pady=10)

    # Création d'un slider pour la difficulté
    TKS_SCALE = tk.Scale(TKF_PAGE_PARAMETER, from_=0, to=5, orient="horizontal")
    # Affichage du slider
    TKS_SCALE.grid(row=4, column=1)
    # Initialisation d'un bouton pour enregistrer les paramètres
    tkb_save = tk.Button(TKF_PAGE_PARAMETER, text="Enregistrer",
                         font="Helvetica 16",
                         command=
                         lambda: ctrl_pp.cpp_settings_save())
    # Affichage du bouton
    tkb_save.grid(row=5, column=1, pady=20)
    # Initialisation d'un bouton pour réinitialiser les paramètres
    tkb_reset = tk.Button(TKF_PAGE_PARAMETER, text="Réinitialiser",
                          font="Helvetica 16",
                          command=
                          lambda: ctrl_pp.cpp_settings_reset())
    # Affichage du bouton
    tkb_reset.grid(row=5, column=2)


def vpp_get_nb_rows():
    """! Accesseur retournant le nombre de lignes sélectionné

    Cette fonction retourne le nombre de lignes sélectionné par l'utilisateur.
    Elle est appelée lorsque l'utilisateur clique sur le bouton "Enregistrer"

    @pre STV_ROWS initialisé
    @return Le nombre de lignes sélectionné

    **Variables :**
    * STV_ROWS : StringVar pour récupérer la valeur du nombre de lignes
    """
    global STV_ROWS
    # Retourne le nombre de lignes sélectionné
    return int(STV_ROWS.get())


def vpp_get_nb_columns():
    """! Accesseur retournant le nombre de colonnes sélectionné

    Cette fonction retourne le nombre de colonnes sélectionné par l'utilisateur.
    Elle est appelée lorsque l'utilisateur clique sur le bouton "Enregistrer"

    @pre STV_COLUMNS initialisé
    @return Le nombre de colonnes sélectionné

    **Variables :**
    * STV_COLUMNS : StringVar pour récupérer la valeur du nombre de colonnes
    """
    global STV_COLUMNS
    # Retourne le nombre de colonnes sélectionné
    return int(STV_COLUMNS.get())


def vpp_get_nb_jetons():
    """! Accesseur retournant le nombre de jetons requis sélectionné

    Cette fonction retourne le nombre de jetons requis sélectionné par
    l'utilisateur. Elle est appelée lorsque l'utilisateur clique sur le bouton
    "Enregistrer".

    @pre STV_NB_JETONS initialisé
    @return Le nombre de jetons requis sélectionné

    **Variables :**
    * STV_NB_JETONS : StringVar pour récupérer la valeur du nombre de jetons
    requis
    """
    global STV_NB_JETONS
    # Retourne le nombre de jetons requis sélectionné
    return int(STV_NB_JETONS.get())


def vpp_get_difficulty():
    """! Accesseur retournant la difficulté sélectionnée

    Cette fonction retourne la difficulté sélectionnée par l'utilisateur. Elle
    est appelée lorsque l'utilisateur clique sur le bouton "Enregistrer".

    @pre TKS_SCALE initialisé
    @return La difficulté sélectionnée

    **Variables :**
    * TKS_SCALE : Slider pour la difficulté
    """
    global TKS_SCALE
    # Retourne la difficulté sélectionnée
    return int(TKS_SCALE.get())


def vpp_set_nb_rows(i_rows: int):
    """! Mutateur pour le nombre de lignes

    Cette fonction modifie le nombre de lignes sélectionné par l'utilisateur.
    Elle est appelée lorsque l'utilisateur clique sur le bouton "Réinitialiser".

    @pre STV_ROWS initialisé
    @param i_rows: Le nouveau nombre de lignes
    @post STV_ROWS est modifié

    **Variables :**
    * STV_ROWS : StringVar pour récupérer la valeur du nombre de lignes
    * i_rows : Le nombre de lignes à modifier
    """
    # Modifie le nombre de lignes dans l'interface
    STV_ROWS.set(str(i_rows))


def vpp_set_nb_columns(i_columns: int):
    """! Mutateur pour le nombre de colonnes

    Cette fonction modifie le nombre de colonnes sélectionné par l'utilisateur.
    Elle est appelée lorsque l'utilisateur clique sur le bouton "Réinitialiser".

    @pre STV_COLUMNS initialisé*
    @param i_columns: Le nouveau nombre de colonnes
    @post STV_COLUMNS est modifié

    **Variables :**
    * STV_COLUMNS : StringVar pour récupérer la valeur du nombre de colonnes
    * i_columns : Le nombre de colonnes à modifier
    """
    STV_COLUMNS.set(str(i_columns))


def vpp_set_nb_jetons(i_nb_jetons: int):
    """! Mutateur pour le nombre de jetons requis

    Cette fonction modifie le nombre de jetons requis sélectionné par
    l'utilisateur. Elle est appelée lorsque l'utilisateur clique sur le bouton
    "Réinitialiser".

    @pre STV_NB_JETONS initialisé
    @param i_nb_jetons: Le nouveau nombre de jetons requis
    @post STV_NB_JETONS est modifié

    **Variables :**
    * STV_NB_JETONS : StringVar pour récupérer la valeur du nombre de jetons
    requis
    * i_nb_jetons : Le nombre de jetons requis à modifier
    """
    # Modifie le nombre de jetons requis dans l'interface
    STV_NB_JETONS.set(str(i_nb_jetons))


def vpp_set_difficulty(i_difficulty):
    """! Mutateur pour la difficulté

    Cette fonction modifie la difficulté sélectionnée par l'utilisateur. Elle
    est appelée lorsque l'utilisateur clique sur le bouton "Réinitialiser".

    @pre TKS_SCALE initialisé
    @param i_difficulty: La nouvelle difficulté
    @post TKS_SCALE est modifié

    **Variables :**
    * TKS_SCALE : Slider pour la difficulté
    * i_difficulty : La difficulté à modifier
    """
    global TKS_SCALE
    # Modifie la difficulté dans l'interface
    TKS_SCALE.set(i_difficulty)


def vpp_reset_settings():
    """! Réinitialise les paramètres du jeu

    Cette fonction réinitialise les paramètres du jeu. Elle est appelée lorsque
    l'utilisateur clique sur le bouton "Réinitialiser".
    """
    # Définit le nombre de lignes de la grille à 6.
    vpp_set_nb_rows(6)
    # Définit le nombre de colonnes de la grille à 7.
    vpp_set_nb_columns(7)
    # Définit le nombre de jetons requis pour gagner à 4.
    vpp_set_nb_jetons(4)
    # Définit la difficulté à 0.
    vpp_set_difficulty(0)


def vpp_get_joueur_color():
    """! Accesseur retournant la couleur des jetons du joueur

    Cette fonction retourne la couleur des jetons du joueur. Elle est appelée
    lorsque l'utilisateur clique sur le bouton "Enregistrer".

    @pre TIS_CUSTOM_COLOR_JOUEUR initialisé
    @return La couleur des jetons du joueur

    **Variables :**
    * TIS_CUSTOM_COLOR_JOUEUR : Tableau d'entier pour la couleur des jetons du
    joueur
    """
    global TIS_CUSTOM_COLOR_JOUEUR
    # Retourne la couleur des jetons du joueur
    return TIS_CUSTOM_COLOR_JOUEUR


def vpp_get_bot_color():
    """! Accesseur retournant la couleur des jetons du bot

    Cette fonction retourne la couleur des jetons du bot. Elle est appelée
    lorsque l'utilisateur clique sur le bouton "Enregistrer".

    @pre TIS_CUSTOM_COLOR_BOT initialisé
    @return La couleur des jetons du bot

    **Variables :**
    * TIS_CUSTOM_COLOR_BOT : Tableau d'entier pour la couleur des jetons du bot
    """
    global TIS_CUSTOM_COLOR_BOT
    # Retourne la couleur des jetons du bot
    return TIS_CUSTOM_COLOR_BOT


def vpp_get_grid_color():
    """! Accesseur retournant la couleur de la grille

    Cette fonction retourne la couleur de la grille. Elle est appelée lorsque
    l'utilisateur clique sur le bouton "Enregistrer".

    @pre TIS_CUSTOM_COLOR_GRID initialisé
    @return La couleur de la grille

    **Variables :**
    * TIS_CUSTOM_COLOR_GRID : Tableau d'entier pour la couleur de la grille
    """
    global TIS_CUSTOM_COLOR_GRID
    # Retourne la couleur de la grille
    return TIS_CUSTOM_COLOR_GRID


def vpp_set_joueur_color(s_color: str):
    """! Mutateur pour la couleur des jetons du joueur

    Cette fonction modifie la couleur des jetons du joueur. Elle est appelée
    lorsque l'utilisateur clique sur le bouton "Réinitialiser".

    @pre TIS_CUSTOM_COLOR_JOUEUR initialisé
    @param s_color: La nouvelle couleur des jetons du joueur
    @post TIS_CUSTOM_COLOR_JOUEUR est modifié

    **Variables :**
    * TIS_CUSTOM_COLOR_JOUEUR : Tableau d'entier pour la couleur des jetons du
    joueur
    * s_color : La couleur des jetons du joueur à modifier
    * TKB_PICKER_JOUEUR : Bouton pour ouvrir le sélecteur de couleur
    """
    global TIS_CUSTOM_COLOR_JOUEUR, TKB_PICKER_JOUEUR
    # Enregistre la nouvelle couleur des jetons du joueur
    TIS_CUSTOM_COLOR_JOUEUR = s_color
    # Modifie la couleur du bouton pour ouvrir le sélecteur de couleur
    TKB_PICKER_JOUEUR.configure(bg=s_color)


def vpp_set_bot_color(s_color: str):
    """! Mutateur pour la couleur des jetons du bot

    Cette fonction modifie la couleur des jetons du bot. Elle est appelée
    lorsque l'utilisateur clique sur le bouton "Réinitialiser".

    @pre TIS_CUSTOM_COLOR_BOT initialisé
    @param s_color: La nouvelle couleur des jetons du bot
    @post TIS_CUSTOM_COLOR_BOT est modifié

    **Variables :**
    * TIS_CUSTOM_COLOR_BOT : Tableau d'entier pour la couleur des jetons du bot
    * s_color : La couleur des jetons du bot à modifier
    * TKB_PICKER_BOT : Bouton pour ouvrir le sélecteur de couleur
    """
    global TIS_CUSTOM_COLOR_BOT, TKB_PICKER_BOT
    # Enregistre la nouvelle couleur des jetons du bot
    TIS_CUSTOM_COLOR_BOT = s_color
    # Modifie la couleur du bouton pour ouvrir le sélecteur de couleur
    TKB_PICKER_BOT.configure(bg=s_color)


def vpp_set_grid_color(s_color: str):
    """! Mutateur pour la couleur de la grille

    Cette fonction modifie la couleur de la grille. Elle est appelée lorsque
    l'utilisateur clique sur le bouton "Réinitialiser".

    @pre TIS_CUSTOM_COLOR_GRID initialisé
    @param s_color: La nouvelle couleur de la grille
    @post TIS_CUSTOM_COLOR_GRID est modifié

    **Variables :**
    * TIS_CUSTOM_COLOR_GRID : Tableau d'entier pour la couleur de la grille
    * s_color : La couleur de la grille à modifier
    * TKB_PICKER_GRID : Bouton pour ouvrir le sélecteur de couleur
    """
    global TIS_CUSTOM_COLOR_GRID, TKB_PICKER_GRID
    # Enregistre la nouvelle couleur de la grille
    TIS_CUSTOM_COLOR_GRID = s_color
    # Modifie la couleur du bouton pour ouvrir le sélecteur de couleur
    TKB_PICKER_GRID.configure(bg=s_color)


def vpp_reset_customs():
    """! Réinitialise les paramètres de personnalisation

    Cette fonction réinitialise les paramètres de personnalisation. Elle est
    appelée lorsque l'utilisateur clique sur le bouton "Réinitialiser".

    """
    # Définit la couleur des jetons du joueur à rouge
    vpp_set_joueur_color("#ff0000")
    # Définit la couleur des jetons du bot à jaune
    vpp_set_bot_color("#ffff00")
    # Définit la couleur de la grille à bleu
    vpp_set_grid_color("#5064F1")


def vpp_askcolor(s_element: str):
    """! Ouvre un sélecteur de couleur

    Cette fonction ouvre un sélecteur de couleur. Elle est appelée lorsque
    l'utilisateur clique sur le bouton pour choisir la couleur.

    @pre s_element est soit "joueur", "bot" ou "grille"
    @param s_element: L'élément dont on veut changer la couleur
    @post La couleur de l'élément est modifiée
    """
    # Demande la couleur de l'élément
    s_colors = f"{askcolor(title=s_element)[1]}"
    # Si la couleur demandée est pour l'utilisateur
    if s_element == "joueur":
        # Modifie la couleur des jetons du joueur
        vpp_set_joueur_color(s_colors)
    # Si la couleur demandée est pour le bot
    elif s_element == "bot":
        # Modifie la couleur des jetons du bot
        vpp_set_bot_color(s_colors)
    # Si la couleur demandée est pour la grille
    else:
        # Modifie la couleur de la grille
        vpp_set_grid_color(s_colors)
