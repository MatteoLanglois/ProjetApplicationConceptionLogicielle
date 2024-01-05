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
@details Ce module contient les fonctions utilitaires relatives aux bonus.
"""
from src.puissanceQuatre import bonus as p4b
from inspect import getmembers, isfunction


def p4b_get_bonuses() -> list[tuple[str, ...]]:
    """! Retourne la liste des noms des fonctions bonus
    @todo Finir commentaire
    """
    # On récupère les fonctions du module bonus
    ts_functions = getmembers(p4b, isfunction)
    # On enlève les fonctions qui ne sont pas des bonus
    ts_functions = [t_function for t_function in ts_functions
                    if t_function[0].startswith("p4b_")]
    # On enlève la fonction p4b_get_bonuses
    ts_functions = [t_function for t_function in ts_functions
                    if t_function[0] != "p4b_get_bonuses"]
    # On enlève la fonction p4b_get_bonus_name
    # On retourne la liste des noms des fonctions bonus
    return ts_functions


def p4b_get_bonus_name(t_function: tuple) -> str:
    """! Retourne le nom d'une fonction bonus
    @todo Finir commentaire
    """
    # On retourne le nom de la fonction
    return t_function[0][t_function[0].find("'") + 1:]