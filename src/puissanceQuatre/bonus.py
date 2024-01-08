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

@package src.puissanceQuatre.bonus
@brief Ce module contient les fonctions relatives aux bonus.
@details Ce module contient les fonctions de bonus.
"""
import numpy as np
from src.puissanceQuatre import puissanceQuatre as ps4
from src.puissanceQuatre import grid as gr
from src.utils import bonus_utils as bu


def p4b_no_bonus(npa_grid: np.array) -> np.array:
    """! Bonus permettant de ne pas jouer de bonus

    @pre npa_grid initialisé
    @param npa_grid: Grille de jeu
    @return npa_grid : Grille retournée
    """
    # On retourne la grille
    return npa_grid


def p4b_invert_grid(npa_grid: np.array) -> np.array:
    """! Echange les pions des joueurs

    @pre npa_grid initialisé
    @param npa_grid: Grille
    @return npa_grid: Grille inversée

    **Variables :**
    * i_nb_rows : Nombre de lignes de la grille
    * i_nb_cols : Nombre de colonnes de la grille
    * i_row : Indice de ligne
    * i_col : Indice de colonne
    """
    # Récupération de la taille de la grille
    i_nb_rows, i_nb_cols = npa_grid.shape
    # Pour chaque ligne de la grille
    for i_row in range(i_nb_rows):
        # Pour chaque case de la ligne
        for i_col in range(i_nb_cols):
            # S'il y a un jeton du joueur
            if npa_grid[i_row, i_col] == 1:
                # Le transformer en jeton du bot
                npa_grid[i_row, i_col] = 2
            # S'il y a un jeton du bot
            elif npa_grid[i_row, i_col] == 2:
                # Le transformer en jeton du bot
                npa_grid[i_row, i_col] = 1
    # Retourner la grille
    return npa_grid


def p4b_remove_full_line(npa_grid: np.array) -> np.array:
    """! Supprime une ligne pleine

    @pre npa_grid initialisé
    @param npa_grid: Grille
    @return npa_grid: Grille avec une ligne pleine en moins

    **Variables :**
    * i_nb_rows : Nombre de lignes de la grille
    * i_nb_cols : Nombre de colonnes de la grille
    * i_row : Indice de ligne
    * i_col : Indice de colonne
    * b_full : Booléen indiquant si la ligne est pleine
    * i_row2 : Indice de ligne
    """
    # Récupérer la taille de la grille
    i_nb_rows, i_nb_cols = npa_grid.shape
    # Pour chaque ligne
    for i_row in range(i_nb_rows):
        # Initialisation d'un booléen à True indiquant si une ligne est pleine.
        b_full = True
        # Pour chaque case de cette ligne
        for i_col in range(i_nb_cols):
            # Si une des cases est vide
            if npa_grid[i_nb_rows, i_nb_cols] == 0:
                # La ligne ne peut pas être pleine
                b_full = False
        # Si la ligne peut être pleine
        if b_full:
            # Pour chaque colonne de cette ligne
            for i_col in range(i_nb_cols):
                # On vide la ligne
                npa_grid[i_row, i_col] = 0
            # Pour chaque ligne
            for i_row2 in range(i_row, i_nb_rows - 1):
                # Pour chaque colonne de la ligne
                for i_col in range(i_nb_cols):
                    # Redescendre les pions
                    npa_grid[i_row2, i_col] = npa_grid[i_row2 + 1, i_col]
    # Renvoyer la grille
    return npa_grid


'''
def p4b_block_column(npa_grid: np.array, i_col: int) -> np.array:
    """! Bloque une colonne

    @pre npa_grid initialisé
    @param npa_grid: Grille
    @param i_col: Colonne à bloquer
    @return npa_grid: Grille avec une colonne bloquée

    **Variables :**
    * i_nb_rows : Nombre de lignes de la grille
    * i_nb_cols : Nombre de colonnes de la grille
    * i_col : Indice de colonne
    @todo Trouver comment gérer la disparition du jeton ajouté par le bonus
    @todo Comment choisir la colonne à bloquer ?
    """
    # Récupération de la taille de la grille
    i_nb_rows, i_nb_cols = npa_grid.shape
    # Pour chaque ligne de la grille
    for i_row in range(i_nb_rows):
        # Mettre un jeton d'une valeur différente des deux joueurs
        npa_grid[i_row, i_col] = 3
    # Retourner la grille
    return npa_grid
'''


def p4b_use_min_max(npa_grid: np.array) -> np.array:
    """! Bonus permettant au joueur d'utiliser l'algorithme min max pour son
    prochain coup

    @pre npa_grid initialisé
    @param npa_grid: Grille de jeu
    @return npa_grid : Grille avec un coup de plus de joué

    **Variables :**
    * i_col : La colonne qui va être jouée avec l'algorithme min max
    """
    # On calcule la colonne où le joueur doit poser son jeton avec min-max
    i_col, _ = ps4.pq_minmax(1, np.copy(npa_grid), 4, 0, True, 0)
    # On pose le jeton
    ps4.pq_ajout_piece(npa_grid, i_col, 1)
    # On retourne la grille
    return npa_grid


def p4b_flip_grid(npa_grid: np.array) -> np.array:
    """! Bonus permettant de retourner la grille

    @pre npa_grid initialisé
    @param npa_grid: Grille de jeu
    @return npa_grid : Grille retournée
    """
    # On retourne la grille
    np.flip(npa_grid, 0)
    # On applique la gravité
    npa_grid = gr.pq_apply_gravity(npa_grid)
    # On retourne la grille
    return npa_grid


def p4b_random_placement(npa_grid: np.array) -> np.array:
    """! Bonus permettant de placer un jeton aléatoirement

    @pre npa_grid initialisé
    @param npa_grid: Grille de jeu
    @return npa_grid : Grille retournée
    """
    # On récupère le nombre de colonnes
    i_nb_columns = npa_grid.shape[1]
    # On récupère une colonne aléatoire
    i_col = np.random.randint(0, i_nb_columns)
    # On place le jeton
    ps4.pq_ajout_piece(npa_grid, i_col, 1)
    # On retourne la grille
    return npa_grid


def p4b_random_bonus(npa_grid: np.array) -> np.array:
    """! Bonus permettant de choisir un bonus aléatoirement

    @pre npa_grid initialisé
    @param npa_grid: Grille de jeu
    @return npa_grid : Grille retournée
    """
    # On récupère les bonus :
    ts_bonus = bu.bu_get_bonuses()
    # On récupère un bonus aléatoire
    s_bonus = ts_bonus[np.random.randint(0, len(ts_bonus))]
    # On récupère la fonction du bonus
    f_bonus = getattr(bu, s_bonus[1])
    # On applique le bonus
    npa_grid = f_bonus(npa_grid)
    # On retourne la grille
    return npa_grid
