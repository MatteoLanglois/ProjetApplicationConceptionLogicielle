"""! **Vue de la page de jeu**
Ce module représente la vue de la page de jeu.

Ce module contient les fonctions permettant de gérer la vue de la page de jeu.

@see src/controller/ctrl_pageJeu.py
"""

import tkinter as tk
from src.controller import ctrl_pageJeu as ctrl_pj

"""! Frame de la page de jeu
"""
global tkf_page_jeu

"""! Canvas de la page de jeu
Le canvas permet de dessiner la grille de jeu.
"""
global tkc_grid

"""! Largeur du canvas
"""
global i_canvas_width

"""! Hauteur du canvas
"""
global i_canvas_height


def v_page_jeu_init(tk_root: tk.Tk):
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
    """
    # On définit en global les variables tkf_page_jeu, tkc_grid,
    # i_canvas_width, i_canvas_height
    global tkf_page_jeu, tkc_grid, i_canvas_width, i_canvas_height
    # Création du cadre permettant l'affichage de la page du jeu
    tkf_page_jeu = tk.Frame(tk_root, height=500, width=430, padx=20, pady=20)
    # Affichage du cadre
    tkf_page_jeu.grid(row=0, column=0, sticky="nsew")

    # On définit la largeur du canvas qui va permettre d'afficher la grille
    i_canvas_width = 430
    # On définit la hauteur du canvas qui va permettre d'afficher la grille
    i_canvas_height = 500
    # On crée le canvas
    tkc_grid = tk.Canvas(tkf_page_jeu, bg="white",
                         width=i_canvas_width, height=i_canvas_height)
    # On affiche le canvas
    tkc_grid.grid(row=0, column=0, sticky="nsew", columnspan=4, rowspan=4)
    # Lorsque l'on clique sur le canvas, cela appellera la fonction
    # ctrl_pj.ctrl_page_jeu_play(event)
    tkc_grid.bind('<Button-1>', lambda event: ctrl_pj.ctrl_page_jeu_play(event))

    # Création d'un bouton pour annuler le dernier coup
    tkB_undo = tk.Button(tkf_page_jeu, text="Undo", font=("Helvetica", 20),
                         command=lambda: ctrl_pj.ctrl_page_jeu_undo())
    # Affichage du bouton
    tkB_undo.grid(row=4, column=0, sticky="nsew", pady=50, padx=50)

    # Création d'un bouton pour refaire le dernier coup
    tkB_redo = tk.Button(tkf_page_jeu, text="Redo", font=("Helvetica", 20),
                         command=lambda: ctrl_pj.ctrl_page_jeu_redo())
    # Affichage du bouton
    tkB_redo.grid(row=4, column=1, sticky="nsew", pady=50, padx=50)

    # Création d'un bouton pour jouer son bonus
    tkB_bonus = tk.Button(tkf_page_jeu, text="Bonus", font=("Helvetica", 20),
                          command=lambda: ctrl_pj.ctrl_page_jeu_bonus())
    # Affichage du bouton
    tkB_bonus.grid(row=4, column=2, sticky="nsew", pady=50, padx=50)

    # Création d'un bouton pour quitter le jeu
    tkB_quit = tk.Button(tkf_page_jeu, text="Quitter", font=("Helvetica", 20),
                         command=lambda: ctrl_pj.ctrl_page_jeu_quit())
    # Affichage du bouton
    tkB_quit.grid(row=4, column=3, sticky="nsew", pady=50, padx=50)


def v_page_jeu_destroy():
    """! Détruit la page de jeu

    **Variables :**
    * tkf_page_jeu : Frame de la page de jeu

    **Préconditions :**
    * tkf_page_jeu initialisé

    """
    # On définit de manière globale la variable tkf_page_jeu
    global tkf_page_jeu
    # On efface le cadre
    tkf_page_jeu.pack_forget()
    # On supprime le cadre
    tkf_page_jeu.destroy()


def v_page_jeu_draw_grid(rows: int, columns: int):
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
    # i_canvas_height
    global tkc_grid, i_canvas_width, i_canvas_height
    # On vide le canvas
    tkc_grid.delete("all")

    # On définit la largeur d'une cellule en fonction de la taille du canvas
    # et du nombre de colonnes dans la grille
    cell_width = i_canvas_width / columns
    # On définit la hauteur d'une cellule en fonction de la taille du canvas
    # et du nombre de lignes dans la grille
    cell_height = i_canvas_height / rows

    # Pour chaque ligne de la grille
    for i_rows in range(rows):
        # Pour chaque colonne de la ligne
        for i_cols in range(columns):
            # On calcule les coordonnées du point supérieur gauche de la cellule
            ti_upper_left = (i_rows * cell_width + 5, i_cols * cell_height + 5)
            # On calcule les coordonnées du point inférieur droit de la cellule
            ti_lower_right = (i_rows * cell_width + cell_width - 5,
                              i_cols * cell_height + cell_height - 5)
            # On dessine la cellule
            tkc_grid.create_oval((ti_upper_left, ti_lower_right))


def v_page_jeu_show_coin(row: int, column: int, color: str):
    """! Dessine un jeton dans une cellule

    @param row: Ligne de la cellule où l'on va dessiner le jeton
    @param column: Colonne de la cellule où l'on va dessiner le jeton
    @param color: Couleur du jeton
    @todo
    """


def v_page_jeu_get_grid_cell(i_x: int, i_y: int) -> (int, int):
    """! Récupère les coordonnées dans la grille de la cellule cliquée
    Récupère les coordonnées dans la grille de la cellule cliquée en fonction
    des coordonnées du clic dans le canvas.

    **Variables :**
    * i_canvas_width : Largeur du canvas
    * i_canvas_height : Hauteur du canvas

    @param i_x: Coordonnée x du clic dans le canvas
    @param i_y: Coordonnée y du clic dans le canvas

    @return: Coordonnées de la cellule cliquée dans la grille
    @todo
    """
    global i_canvas_width, i_canvas_height

    return 0, 0
