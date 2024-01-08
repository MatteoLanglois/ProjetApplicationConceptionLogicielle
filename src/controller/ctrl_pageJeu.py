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

@package src.controller.ctrl_pageJeu
@brief Un module qui gère la page de jeu
@details Ce module contient les fonctions permettant de gérer la page de jeu.
"""
# Importation de tkinter
import tkinter as tk
# Importation de numpy
import numpy as np
# Importation du controller de la page d'accueil afin d'initialiser la fenêtre
from src.view import view_pageJeu as view_pj
# Importation du controller de la page de paramètres afin d'initialiser la
# fenêtre
from src.controller import ctrl_main as ctrl_m
# Importation du controller de la page de paramètres afin d'initialiser la
# fenêtre
from src.controller import ctrl_pageParametres as ctrl_pp
# Importation du controller de la page de bonus afin de récupérer le bonus
# sélectionné
from src.controller import ctrl_PageBonus as ctrl_pb
# Importation du modèle du jeu puissance 4
from src.puissanceQuatre import puissanceQuatre as ps4
# Importation du modèle de la grille de jeu
from src.puissanceQuatre import grid as gr
# Importation du modèle des bonus
from src.utils import bonus_utils as bu

# Variables globales ##########################
# Grille de jeu
global NPA_GRID
# Fenêtre principale
global TK_ROOT
# Nombre de jetons à aligner pour gagner
global I_NB_JETONS
# Couleur des jetons du joueur
global ST_COLOR_JOUEUR
# Couleur des jetons du bot
global ST_COLOR_BOT
# Difficulté du bot
global I_DIFFICULTY
# Liste des coups joués
global T_UNDO_REDO
# Liste des coups annulés
global T_REDO
# Nombre de lignes de la grille de jeu
global I_NB_ROWS
# Nombre de colonnes de la grille de jeu
global I_NB_COLS
# Bonus sélectionné
global S_BONUS
# Bonus utilisé
global B_BONUS_USED


def cpj_init(tk_win_root: tk.Tk):
    """! Affiche la page de jeu

    @pre tk_root initialisé
    @post page de jeu affichée

    **Variables :**
    * TK_ROOT : Fenêtre principale
    * ST_COLOR_JOUEUR : Couleur des jetons du joueur
    * ST_COLOR_BOT : Couleur des jetons du bot
    * I_NB_ROWS : Nombre de lignes de la grille de jeu
    * I_NB_COLS : Nombre de colonnes de la grille de jeu
    * NPA_GRID : Grille de jeu
    * T_UNDO_REDO : Liste des coups joués
    * T_REDO : Liste des coups annulés
    * I_DIFFICULTY : Difficulté du bot
    * I_NB_JETONS : Nombre de jetons à aligner pour gagner
    * st_color_grid : Couleur de la grille de jeu
    """
    global T_UNDO_REDO, T_REDO, I_NB_JETONS, ST_COLOR_JOUEUR, ST_COLOR_BOT, \
        I_DIFFICULTY, I_NB_ROWS, I_NB_COLS, NPA_GRID, TK_ROOT, B_BONUS_USED, \
        S_BONUS

    # On enregistre la fenêtre principale
    TK_ROOT = tk_win_root

    # On indique que le bonus n'a pas été utilisé
    B_BONUS_USED = False
    # On récupère le Bonus choisit
    S_BONUS = ctrl_pb.cpb_get_chosen_bonus()

    # Initialisation de la liste pour revenir en arrière
    T_UNDO_REDO = []
    # Initialisation de la liste pour redo
    T_REDO = []

    # Récupération des couleurs pour la grille de jeu
    ST_COLOR_JOUEUR, ST_COLOR_BOT, st_color_grid = (
        ctrl_pp.cpp_custom_load())

    # Récupération des paramètres pour la partie
    I_NB_ROWS, I_NB_COLS, I_NB_JETONS, I_DIFFICULTY = (
        ctrl_pp.cpp_settings_load())
    # Afficher la page de jeu
    view_pj.vpj_init_page_jeu(TK_ROOT, st_color_grid)
    # Initialisation de la grille de jeu
    NPA_GRID = gr.pq_init_grille(I_NB_ROWS, I_NB_COLS)
    # Dessin de la grille de jeu
    cpj_draw_grid(I_NB_ROWS, I_NB_COLS)


def cpj_draw_grid(i_nb_rows: int, i_nb_columns: int):
    """! Dessine la grille de jeu

    @pre i_nb_rows > 0
    @pre i_nb_columns > 0
    @param i_nb_rows: Nombre de lignes de la grille de jeu
    @param i_nb_columns: Nombre de colonnes de la grille de jeu
    @post grille de jeu dessinée
    """
    # Dessin de la grille de jeu
    view_pj.vpj_draw_grid(i_nb_rows, i_nb_columns)


def cpj_put_coin(i_row: int, i_cols: int, i_joueur: int):
    """! Place un jeton dans la grille de jeu

    @pre i_row >= 0
    @pre i_cols >= 0
    @pre i_joueur >= 1 et i_joueur ≤ 2
    @param i_row: Ligne de la grille de jeu
    @param i_cols: Colonne de la grille de jeu
    @param i_joueur: Joueur qui joue
    @post jeton placé dans la grille de jeu

    **Variables :**
    * ST_COLOR_JOUEUR : Couleur des jetons du joueur
    * ST_COLOR_BOT : Couleur des jetons du bot
    """
    global ST_COLOR_JOUEUR
    global ST_COLOR_BOT
    # Si le joueur est le joueur humain
    if i_joueur == 1:
        # Afficher le pion
        view_pj.vpj_show_coin(i_row, i_cols, ST_COLOR_JOUEUR)
    # Si le joueur est le bot
    elif i_joueur == 2:
        # Afficher le pion
        view_pj.vpj_show_coin(i_row, i_cols, ST_COLOR_BOT)


def cpj_undo():
    """! Annule le dernier coup
    """
    global T_UNDO_REDO, T_REDO, NPA_GRID
    # Ajouter à la liste des coups annulés la grille actuelle
    T_REDO.append(NPA_GRID.copy())
    # Récupérer la précédente grille
    NPA_GRID = ps4.pq_undo(NPA_GRID.copy(), T_UNDO_REDO)
    # Mise à jour de la grille
    cpj_update_grid()


def cpj_redo():
    """! Refait le dernier coup
    """
    global T_UNDO_REDO, T_REDO, NPA_GRID
    # Récupération de la grille dont le coup a été annulé
    NPA_GRID = ps4.pq_redo(NPA_GRID.copy(), T_REDO)
    # Mise à jour de la grille
    cpj_update_grid()


def cpj_quit():
    """! Quitte la partie

    @pre tk_root initialisé
    @post page de jeu détruite
    """
    global TK_ROOT
    # Destruction de la page de jeu
    view_pj.vpj_destroy()
    # Fermeture de la fenêtre principale
    ctrl_m.cm_quit(TK_ROOT)


def cpj_play(event: tk.Event, tkf_page_jeu: tk.Frame):
    """! Joue un coup dans la grille de jeu

    @pre event est un évènement de la souris
    @pre tkf_page_jeu initialisé
    @param event: Évènement de la souris sur la grille de jeu
    @param tkf_page_jeu : Frame de la page de jeu

    **Variables :**
    * I_NB_JETONS : Nombre de jetons à aligner pour gagner
    * i_grid_x : Colonne de la grille de jeu
    * i_grid_y : Ligne de la grille de jeu
    * b_joueur_gagne : Booléen indiquant si le joueur a gagné
    * b_joueur_joue : Booléen indiquant si le joueur a joué

    @todo Vérifier que tout est bon
    """
    global I_NB_JETONS, NPA_GRID, T_UNDO_REDO, B_BONUS_USED, T_REDO
    # On enregistre l'état actuel de la grille
    T_UNDO_REDO.append(NPA_GRID.copy())
    # Affichage des coordonnées de la cellule sur laquelle on a cliquée
    i_grid_x, _ = view_pj.vpj_get_grid_cell(event.x, event.y)
    # Initialisation d'un booléen permettant de savoir si le joueur a gagné, à
    # faux
    b_joueur_gagne = False
    # Initialisation d'un booléen permettant de savoir si le joueur a joué,
    # à faux
    b_joueur_joue = False

    # Si la partie n'est pas finie
    if not ps4.pq_partie_finie(NPA_GRID, B_BONUS_USED):
        # Si on peut poser un pion dans cette colonne
        if ps4.pq_verif_colonne(i_grid_x, NPA_GRID):
            # On pose le jeton et on récupère les coordonnées de là où il a été
            # posé
            i_grid_x, i_grid_y = ps4.pq_ajout_piece(npa_grille=NPA_GRID,
                                                    i_colonne=i_grid_x,
                                                    i_joueur=1)
            # Afficher le pion qui vient d'être posé
            cpj_put_coin(i_grid_x, i_grid_y, 1)
            # On réinitialise la liste des coups annulés
            T_REDO = []
            # On indique que le joueur a joué
            b_joueur_joue = True
            # Si le joueur a gagné
            if ps4.pq_victoire(NPA_GRID, i_grid_x, i_grid_y, 1, I_NB_JETONS):
                # Afficher la fenêtre de fin de partie
                ctrl_m.cm_ended_game("Le Joueur 1 a gagné",
                                     tkf_old_frame=tkf_page_jeu)
                # Indiquer que le joueur a gagné
                b_joueur_gagne = True
        # Si le joueur n'a pas gagné, qu'il a joué et que la partie n'est pas
        # finie
        if (not b_joueur_gagne and b_joueur_joue
                and not ps4.pq_partie_finie(NPA_GRID, B_BONUS_USED)):
            # Faire jouer le bot
            cpj_bot_play(tkf_page_jeu)
    # Sinon
    else:
        # Afficher la page de fin de partie indiquant le match nul.
        ctrl_m.cm_ended_game("Match nul",
                             tkf_old_frame=tkf_page_jeu)


def cpj_use_bonus(tkf_page_jeu: tk.Frame):
    """! Utilise un bonus puis met à jour la grille de jeu

    @pre S_BONUS est un bonus
    @pre NPA_GRID est une grille de jeu
    @param tkf_page_jeu : Frame de la page de jeu
    @post Bonus utilisé si B_BONUS_USED est faux

    **Variables :**
    * S_BONUS : Bonus sélectionné
    * NPA_GRID : Grille de jeu
    * B_BONUS_USED : Booléen indiquant si le bonus a été utilisé
    * m_module : Module du bonus
    * f_bonus : Fonction du bonus
    @todo Vérifier si le bonus a entraîné une victoire
    """
    global S_BONUS, NPA_GRID, B_BONUS_USED
    # Si le bonus n'a pas été utilisé
    if not B_BONUS_USED:
        # On indique que le bonus a été utilisé
        B_BONUS_USED = True
        # On importe le module du bonus
        m_module = __import__("src.puissanceQuatre.bonus", fromlist=["bonus"])
        # On récupère la fonction du bonus
        f_bonus = getattr(m_module, bu.bu_unformat_bonus_name(S_BONUS))
        # On applique le bonus à la grille
        NPA_GRID = f_bonus(NPA_GRID.copy())
        # On met à jour la grille
        cpj_update_grid()
        # On désactive le bouton du bonus
        view_pj.vpj_disable_bonus()
        # On fait jouer le bot.
        cpj_bot_play(tkf_page_jeu)


def cpj_bot_play(tkf_page_jeu: tk.Frame):
    """! Fait jouer le bot

    @pre tkf_page_jeu initialisé
    @param tkf_page_jeu : Frame de la page de jeu

    **Variables :**
    * I_NB_JETONS : Nombre de jetons à aligner pour gagner
    * I_DIFFICULTY : Difficulté du bot
    * i_grid_x : Colonne de la grille de jeu
    * i_grid_y : Ligne de la grille de jeu

    @todo Vérifier que tout est bon
    """
    global I_NB_JETONS, I_DIFFICULTY
    # On utilise l'algorithme min max pour choisir le prochain coup du bot
    i_grid_x, _ = ps4.pq_minmax(iNextJoueur=2,
                                npaGrilleCopy=np.copy(NPA_GRID),
                                isFirst=True,
                                tour=-I_DIFFICULTY,
                                i_nb_victoire=4)
    # On pose le pion et on récupère les coordonnées de là où il a été posé
    i_grid_x, i_grid_y = ps4.pq_ajout_piece(npa_grille=NPA_GRID,
                                            i_colonne=i_grid_x, i_joueur=2)
    # On affiche le pion posé
    cpj_put_coin(i_grid_x, i_grid_y, 2)
    # Si le bot a gagné
    if ps4.pq_victoire(NPA_GRID, i_grid_x, i_grid_y, 2, I_NB_JETONS):
        # On affiche la fenêtre de victoire indiquant que le bot a gagné
        ctrl_m.cm_ended_game("Le joueur 2 a gagné",
                             tkf_old_frame=tkf_page_jeu)


def cpj_update_grid():
    """! Réinitialise la grille de jeu

    @pre NPA_GRID initialisé
    @post Grille de jeu mise à jour

    **Variables :**
    * I_NB_ROWS : Nombre de lignes de la grille de jeu
    * I_NB_COLS : Nombre de colonnes de la grille de jeu
    * NPA_GRID : Grille de jeu
    * i_boucle_row : Ligne de la grille de jeu
    * i_boucle_col : Colonne de la grille de jeu
    """
    global I_NB_ROWS, I_NB_COLS, NPA_GRID
    # Dessiner la grille pour la reset
    cpj_draw_grid(I_NB_ROWS, I_NB_COLS)
    # Pour chaque ligne de la grille
    for i_boucle_row in range(I_NB_ROWS):
        # Pour chaque colonne de la ligne
        for i_boucle_col in range(I_NB_COLS):
            # S'il y a un jeton à la position I_ROWS, I_COLS
            if (NPA_GRID[i_boucle_row, i_boucle_col] == 1
                    or NPA_GRID[i_boucle_row, i_boucle_col] == 2):
                # Afficher le pion à cette position
                cpj_put_coin(i_boucle_row, i_boucle_col,
                             NPA_GRID[i_boucle_row, i_boucle_col])
