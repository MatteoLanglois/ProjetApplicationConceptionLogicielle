"""! @brief Un programme qui joue au jeu puissance 4++.

@mainpage Projet Puissance 4++

@section description_main Description
Ce programme est un jeu de puissance 4++ avec une grille de taille variable,
un nombre de pions à aligner variable, des bonus et un undo.

@section import_section Importations
Ce programme utilise les modules externes suivants :
- tkinter
- numpy

@package src.puissanceQuatre.bonus
@brief Ce module contient les fonctions relatives aux bonus.
@details Ce module contient les fonctions de bonus.
"""
import numpy as np


def p4b_init():
    pass


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
    i_nb_rows, i_nb_cols = npa_grid.shape
    for i_row in range(i_nb_rows):
        for i_col in range(i_nb_cols):
            if npa_grid[i_row, i_col] == 1:
                npa_grid[i_row, i_col] = 2
            elif npa_grid[i_row, i_col] == 2:
                npa_grid[i_row, i_col] = 1
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
    i_nb_rows, i_nb_cols = npa_grid.shape
    for i_row in range(i_nb_rows):
        b_full = True
        for i_col in range(i_nb_rows):
            if npa_grid[i_nb_rows, i_nb_cols] == 0:
                b_full = False
        if b_full:
            for i_col in range(i_nb_cols):
                npa_grid[i_row, i_col] = 0
            # Redescendre les pions
            for i_row2 in range(i_row, i_nb_rows-1):
                for i_col in range(i_nb_cols):
                    npa_grid[i_row2, i_col] = npa_grid[i_row2+1, i_col]
    return npa_grid


