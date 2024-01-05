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

@package tests.test_bonus
@brief Teste le module puissanceQuatre.bonus
@details Ce module teste le module puissanceQuatre.bonus.
"""

import numpy as np
from src.puissanceQuatre import grid as gr


def tb_invert_grid():
    """! Teste la fonction pq_invert_grid
    @todo A tester
    """
    pass


def tb_remove_full_line():
    """! Teste la fonction pq_remove_full_line
    @todo A tester
    """
    pass


def tb_block_column():
    """! Teste la fonction pq_block_column
    @todo A tester
    """
    pass


def tb_use_min_max():
    """! Teste la fonction pq_use_min_max
    @todo A tester
    """
    pass


def tb_test_all():
    """! Lance tous les tests
    """
    tb_invert_grid()
    tb_remove_full_line()
    tb_block_column()
    tb_use_min_max()


if __name__ == "__main__":
    tb_test_all()
