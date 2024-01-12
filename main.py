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

@package src.main
@brief Programme principal du jeu
@details Ce module permet de lancer le jeu.
"""

import src.controller.ctrl_main as ctrl_m


def main():
    """! Fonction principale du jeu
    """
    ctrl_m.cm_init()


if __name__ == '__main__':
    main()
