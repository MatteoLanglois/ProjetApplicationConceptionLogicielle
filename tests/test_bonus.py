"""! @brief Un programme qui joue au jeu puissance 4++.

@mainpage Projet Puissance 4++

@section description_main Description
Ce programme est un jeu de puissance 4++ avec une grille de taille variable,
un nombre de pions à aligner variable, des bonus et un undo.

@section import_section Importations
Ce programme utilise les modules externes suivants :
- tkinter
- numpy

@package tests.test_bonus
@brief Teste le module puissanceQuatre.bonus
@details Ce module teste le module puissanceQuatre.bonus.
"""

import numpy as np
from src.puissanceQuatre import grid as gr


def test_invert_grid():
    pass


def test_remove_full_line():
    pass


def test_block_column():
    pass


def test_use_min_max():
    pass


def test_all():
    """! Lance tous les tests
    """
    test_invert_grid()
    test_remove_full_line()
    test_block_column()
    test_use_min_max()


if __name__ == "__main__":
    test_all()
