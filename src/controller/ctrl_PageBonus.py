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

@package src.controller.ctrl_PageBonus
@brief Un module qui gère la page de bonus
@details Ce module contient les fonctions permettant de gérer la page de choix
du bonus.
"""
# Importations de tkinter
import tkinter as tk
# Importation des fonctions utilitaires des bonus
from src.utils import bonus_utils as bu
# Importation de la vue de la page de choix du bonus
from src.view import view_pageBonus as view_pb
# Importation du controller de la page principale afin de lancer une partie
from src.controller import ctrl_main as ctrl_m

# Variables globales ##########################
# Fenêtre principale
global TK_ROOT
# Nom du bonus sélectionné
global S_BONUS


def cpb_init(tk_win_root: tk.Tk):
    """! Initialise la page de choix du bonus

    @pre tk_root initialisé
    @param tk_win_root: Fenêtre principale
    @post page de choix du bonus initialisée

    **Variables :**
    * NPA_GRID : Grille de jeu
    * TK_ROOT : Fenêtre principale
    """
    global TK_ROOT
    # Initialisation de la fenêtre principale
    TK_ROOT = tk_win_root
    # Initialisation de la page de choix des bonus
    view_pb.vpb_init(TK_ROOT)


def cpb_get_bonuses() -> list[str]:
    """! Récupère les bonus disponibles
    """
    # On récupère les fonctions du module bonus en formatant leur nom pour
    # l'affichage
    return [bu.bu_format_bonus_name(bu.bu_get_bonus_name(s_bonus))
            for s_bonus in bu.bu_get_bonuses()]


def cpb_valider_bonus():
    """! Récupère les bonus sélectionnés par le joueur

    @pre fenêtre de choix du bonus affichée
    @post Choix du bonus enregistré

    **Variables :**
    * S_BONUS : Nom du bonus sélectionné
    * TK_ROOT : Fenêtre principale
    """
    global S_BONUS, TK_ROOT
    # Enregistrement du bonus de manière globale
    S_BONUS = view_pb.vpb_get_bonus()
    # Passage à la fenêtre jeu
    ctrl_m.cm_page_play(TK_ROOT, view_pb.vpb_get_frame())


def cpb_show_bonus_description(s_bonus: str):
    """! Affiche la description du bonus sélectionné

    @pre s_bonus non vide
    @param s_bonus: Nom du bonus
    @post Description du bonus affichée

    **Variables :**
    * s_desc : Description du bonus
    """
    # On récupère la description du bonus
    s_desc = bu.bu_get_bonus_description(bu.bu_unformat_bonus_name(s_bonus))
    # On affiche la description du bonus
    view_pb.vpb_show_bonus_description(s_desc)


def cpb_get_chosen_bonus() -> str:
    """! Accesseur du bonus choisi par l'utilisateur

    @pre S_BONUS non nul
    @return : Bonus choisi par l'utilisateur

    **Variables :**
    * S_BONUS : nom du bonus sélectionné
    """
    global S_BONUS
    return S_BONUS
