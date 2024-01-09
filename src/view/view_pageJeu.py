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

@package src.view.view_pageJeu
@brief Ce module représente la vue de la page de jeu.
@details Ce module contient les fonctions permettant de gérer la vue de la page 
de jeu.
"""
# Importation de tkinter
import tkinter as tk
# Importation du contrôleur de la page de jeu
from src.controller import ctrl_pageJeu as ctrl_pj
# Importation du contrôleur principal pour avoir le menu
from src.controller import ctrl_main as ctrl_m

# Variables globales ##########################
# Frame de la page de jeu
global TKF_PAGE_JEU
# Canvas de la page de jeu
global TKC_GRID
# Largeur du canvas
global I_CANVAS_WIDTH
# Hauteur du canvas
global I_CANVAS_HEIGHT
# Nombre de lignes de la grille
global I_NB_ROWS
# Nombre de colonnes de la grille
global I_NB_COLUMNS
# Bouton pour utiliser un bonus
global TKB_BONUS
# Label pour afficher des informations
global TKL_INFO


def vpj_init_page_jeu(tk_root: tk.Tk, st_color_grid: str):
    """! Initialise la page de jeu

    **Variables :**
    * tkf_page_jeu : Frame de la page de jeu
    * tkc_grid : Canvas de la page de jeu
    * i_canvas_width : Largeur du canvas
    * i_canvas_height : Hauteur du canvas
    * tkB_undo : Bouton pour annuler le dernier coup
    * tkB_redo : Bouton pour refaire le dernier coup
    * tkB_bonus : Bouton pour utiliser un bonus
    * tkB_quit : Bouton pour quitter la partie

    **Préconditions :**
    * tk_root initialisé

    @param tk_root: Fenêtre principale
    @param st_color_grid: Couleur de la grille au format hexadécimal
    """
    # On définit en global les variables tkf_page_jeu, tkc_grid,
    # i_canvas_width, i_canvas_height
    global TKF_PAGE_JEU, TKC_GRID, I_CANVAS_WIDTH, I_CANVAS_HEIGHT, TKB_BONUS
    global TKL_INFO

    # Création du cadre permettant l'affichage de la page du jeu
    TKF_PAGE_JEU = tk.Frame(tk_root, height=500, width=430, padx=20, pady=20)
    # Affichage du cadre
    TKF_PAGE_JEU.grid(row=0, column=0, sticky="nsew")

    # Affichage du menu sur la fenêtre
    tk_root.configure(menu=ctrl_m.cm_menu(TKF_PAGE_JEU, True))

    TKL_INFO = tk.Label(TKF_PAGE_JEU, text="", font=("Helvetica", 20))
    TKL_INFO.grid(row=0, column=0, columnspan=4, sticky="nsew")

    # On définit la largeur du canvas qui va permettre d'afficher la grille
    I_CANVAS_WIDTH = 500
    # On définit la hauteur du canvas qui va permettre d'afficher la grille
    I_CANVAS_HEIGHT = 430
    # On crée le canvas
    TKC_GRID = tk.Canvas(TKF_PAGE_JEU, bg=st_color_grid,
                         width=I_CANVAS_WIDTH, height=I_CANVAS_HEIGHT)
    # On affiche le canvas
    TKC_GRID.grid(row=1, column=0, sticky="nsew", columnspan=4, rowspan=4)
    # Lorsque l'on clique sur le canvas, cela appellera la fonction
    # ctrl_pj.ctrl_page_jeu_play(event)
    TKC_GRID.bind('<Button-1>',
                  lambda event: ctrl_pj.cpj_play(event, TKF_PAGE_JEU))

    # Création d'un bouton pour annuler le dernier coup
    tkB_undo = tk.Button(TKF_PAGE_JEU, text="Undo", font=("Helvetica", 16),
                         command=lambda: ctrl_pj.cpj_undo())
    # Affichage du bouton
    tkB_undo.grid(row=5, column=0, sticky="nsew", pady=50, padx=10)

    # Création d'un bouton pour refaire le dernier coup
    tkB_redo = tk.Button(TKF_PAGE_JEU, text="Redo", font=("Helvetica", 16),
                         command=lambda: ctrl_pj.cpj_redo())
    # Affichage du bouton
    tkB_redo.grid(row=5, column=1, sticky="nsew", pady=50, padx=10)

    # Création d'un bouton pour jouer son bonus
    TKB_BONUS = tk.Button(TKF_PAGE_JEU, text="Bonus", font=("Helvetica", 16),
                          command=lambda: ctrl_pj.cpj_use_bonus(TKF_PAGE_JEU))
    # Affichage du bouton
    TKB_BONUS.grid(row=5, column=2, sticky="nsew", pady=50, padx=10)

    # Création d'un bouton pour quitter le jeu
    tkB_quit = tk.Button(TKF_PAGE_JEU, text="Quitter", font=("Helvetica", 16),
                         command=lambda: ctrl_pj.cpj_quit())
    # Affichage du bouton
    tkB_quit.grid(row=5, column=3, sticky="nsew", pady=50, padx=10)


def vpj_destroy():
    """! Détruit la page de jeu

    **Variables :**
    * tkf_page_jeu : Frame de la page de jeu

    @pre tkf_page_jeu initialisé

    """
    # On définit de manière globale la variable tkf_page_jeu
    global TKF_PAGE_JEU
    # On efface le cadre
    TKF_PAGE_JEU.pack_forget()
    # On supprime le cadre
    TKF_PAGE_JEU.destroy()


def vpj_draw_grid(rows: int, columns: int):
    """! Dessine la grille de jeu

    **Variables :**
    * tkc_grid : Canvas de la page de jeu
    * i_canvas_width : Largeur du canvas
    * i_canvas_height : Hauteur du canvas
    * cell_width : Largeur d'une cellule
    * cell_height : Hauteur d'une cellule
    * ti_upper_left : Coordonnées du coin supérieur gauche d'une cellule
    * ti_lower_right : Coordonnées du coin inférieur droit d'une cellule

    @param rows: Nombre de lignes de la grille
    @param columns: Nombre de colonnes de la grille
    """
    # On définit de manière globale les variables tkc_grid, i_canvas_width,
    # i_canvas_height, i_nb_rows, i_nb_columns
    global TKC_GRID, I_CANVAS_WIDTH, I_CANVAS_HEIGHT, I_NB_ROWS, I_NB_COLUMNS
    # On définit la variable globale i_nb_rows
    I_NB_ROWS = rows
    # On définit la variable globale i_nb_columns
    I_NB_COLUMNS = columns

    # On vide le canvas
    TKC_GRID.delete("all")

    # On définit la largeur d'une cellule en fonction de la taille du canvas
    # et du nombre de colonnes dans la grille
    cell_width = I_CANVAS_WIDTH / columns
    # On définit la hauteur d'une cellule en fonction de la taille du canvas
    # et du nombre de lignes dans la grille
    cell_height = I_CANVAS_HEIGHT / rows

    # Pour chaque colonne de la grille
    for i_rows in range(columns):
        # Pour chaque ligne de la colonne
        TKC_GRID.create_line((i_rows * cell_width, 0),
                             (i_rows * cell_width, I_CANVAS_HEIGHT))
        for i_cols in range(rows):
            # On calcule les coordonnées du point supérieur gauche de la cellule
            ti_upper_left = (i_rows * cell_width + 5, i_cols * cell_height + 5)
            # On calcule les coordonnées du point inférieur droit de la cellule
            ti_lower_right = (i_rows * cell_width + cell_width - 5,
                              i_cols * cell_height + cell_height - 5)
            # On dessine la cellule
            TKC_GRID.create_oval((ti_upper_left, ti_lower_right), fill="white")


def vpj_show_coin(row: int, column: int, color: str):
    """! Dessine un jeton dans une cellule

    @param row: Ligne de la cellule où l'on va dessiner le jeton
    @param column: Colonne de la cellule où l'on va dessiner le jeton
    @param color: Couleur du jeton
    """
    global I_CANVAS_WIDTH, I_CANVAS_HEIGHT, I_NB_ROWS, I_NB_COLUMNS

    # On définit la largeur d'une cellule en fonction de la taille du canvas
    # et du nombre de colonnes dans la grille
    cell_width = I_CANVAS_WIDTH / I_NB_COLUMNS
    # On définit la hauteur d'une cellule en fonction de la taille du canvas
    # et du nombre de lignes dans la grille
    cell_height = I_CANVAS_HEIGHT / I_NB_ROWS

    # On calcule les coordonnées du point supérieur gauche de la cellule
    ti_upper_left = (column * cell_width + 5, row * cell_height + 5)
    # On calcule les coordonnées du point inférieur droit de la cellule
    ti_lower_right = (column * cell_width + cell_width - 5,
                      row * cell_height + cell_height - 5)

    # On dessine le jeton
    TKC_GRID.create_oval((ti_upper_left, ti_lower_right), fill=color)


def vpj_get_grid_cell(i_x: int, i_y: int) -> (int, int):
    """! Récupère les coordonnées dans la grille de la cellule cliquée
    Récupère les coordonnées dans la grille de la cellule cliquée en fonction
    des coordonnées du clic dans le canvas.

    **Variables :**
    * i_canvas_width : Largeur du canvas
    * i_canvas_height : Hauteur du canvas

    @param i_x: Coordonnée x du clic dans le canvas
    @param i_y: Coordonnée y du clic dans le canvas

    @return: Coordonnées de la cellule cliquée dans la grille
    """
    global I_CANVAS_WIDTH, I_CANVAS_HEIGHT, I_NB_ROWS, I_NB_COLUMNS

    # On définit la largeur d'une cellule en fonction de la taille du canvas
    # et du nombre de colonnes dans la grille
    cell_width = I_CANVAS_WIDTH / I_NB_COLUMNS
    # On définit la hauteur d'une cellule en fonction de la taille du canvas
    # et du nombre de lignes dans la grille
    cell_height = I_CANVAS_HEIGHT / I_NB_ROWS

    # On retourne les coordonnées de la cellule cliquée
    return int(i_x / cell_width), int(i_y / cell_height)


def vpj_disable_bonus():
    """! Désactive le bouton bonus

    @pre TKS_BONUS initialisé
    """
    global TKB_BONUS
    # On désactive le bouton bonus
    TKB_BONUS.config(state="disabled")
    # On change le relief du bouton bonus
    TKB_BONUS.config(relief="sunken")


def vpj_get_frame() -> tk.Frame:
    """! Accesseur de la frame de la page de jeu

    @pre TKF_PAGE_JEU initialisé
    @return: Frame de la page de jeu

    **Variables :**
    * TKF_PAGE_JEU : Frame de la page de jeu
    """
    global TKF_PAGE_JEU
    # On retourne la frame de la page de jeu
    return TKF_PAGE_JEU


def vpj_set_info(st_info: str):
    """! Modifie le texte du label d'information

    @param st_info: Texte à afficher dans le label d'information
    """
    global TKL_INFO
    TKL_INFO.config(text=st_info)
