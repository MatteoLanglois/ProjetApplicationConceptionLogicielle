"""! @brief Un programme qui joue au jeu puissance 4++.

Ce programme est un jeu de puissance 4++ avec une grille de taille variable,
un nombre de pions à aligner variable, des bonus et un undo.

Ce programme utilise les modules externes suivants :
- tkinter
- numpy
- inspect

@package tests.test_grid
@brief Teste le module puissanceQuatre.grid
@details Ce module teste le module puissanceQuatre.grid.
"""

import numpy as np
from src.puissanceQuatre import grid as gr


def tg_init_grille():
    """! Teste la fonction pq_init_grille

    **Variables :**
        - *liste_tailles* : liste des tailles de grille à tester
        - *i_boucle* : variable de boucle
        - *i_boucle_2* : variable de boucle
        - *grille* : grille de jeu

    @test Vérifie que la grille est bien initialisée avec des 0 partout avec
    la bonne taille
    @test Vérifie que toutes les combinaisons de 2 nombres de la liste
    *liste_tailles* sont testées
    """
    # On teste 4 cas différents, avec des tailles différentes
    liste_tailles = [2, 5, 7, 100]
    for i_boucle in liste_tailles:
        for i_boucle_2 in liste_tailles:
            grille = gr.pq_init_grille(i_boucle, i_boucle_2)
            assert np.array_equal(grille, np.zeros((i_boucle, i_boucle_2))), \
                "pq_init_grille non fonctionnel"


def tg_test_all():
    """! Lance tous les tests
    """
    tg_init_grille()
    tg_reset_grille()


if __name__ == "__main__":
    tg_test_all()
