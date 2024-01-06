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

@package src.utils.bonus_utils
@brief Ce module contient les fonctions utiles aux bonus.
@details Ce module contient les fonctions utilitaires relatives aux bonus.
"""
from src.puissanceQuatre import bonus as p4b
from inspect import getmembers, isfunction


def bu_get_bonuses() -> list[tuple[str, ...]]:
    """! Retourne la liste des noms des fonctions bonus

    @post La liste des noms des fonctions bonus est retournée

    **Variables :**
    * ts_functions : Liste des fonctions du module bonus
    """
    # On récupère les fonctions du module bonus
    ts_functions = getmembers(p4b, isfunction)
    # On retourne la liste des noms des fonctions bonus
    return ts_functions


def bu_get_bonus_name(t_function: tuple) -> str:
    """! Retourne le nom d'une fonction bonus
    """
    # On retourne le nom de la fonction
    return t_function[0][t_function[0].find("'") + 1:]


def bu_format_bonus_name(s_bonus_name: str) -> str:
    """! Formate le nom d'un bonus
    """
    # On retourne le nom du bonus formaté
    return (s_bonus_name.replace("_", " ")
            .replace("p4b ", "")).title()


def bu_unformat_bonus_name(s_bonus_name: str) -> str:
    """! Déformate le nom d'un bonus
    """
    # On retourne le nom du bonus déformaté
    return f"p4b_{s_bonus_name.replace(' ', '_').lower()}"


def bu_get_bonus_description(s_bonus_name: str) -> str:
    """! Retourne la description d'un bonus
    """
    # On récupère la fonction bonus choisie
    t_function = [t_function for t_function in bu_get_bonuses()
                  if bu_get_bonus_name(t_function) == s_bonus_name][0]
    # On retourne la description brève du bonus
    return t_function[1].__doc__[1:t_function[1].__doc__.find("@pre")] \
        if t_function[1].__doc__ else ""
