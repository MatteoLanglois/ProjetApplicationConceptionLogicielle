"""! **test_puissanceQuatre**
Ce module contient les tests unitaires pour le module puissanceQuatre.

@see puissanceQuatre
"""

import numpy as np

import puissanceQuatre as ps4


def test_init_grille():
    """! Teste la fonction pq_init_grille

    **Variables :**
        - *liste_tailles* : liste des tailles de grille à tester
        - *i_boucle* : variable de boucle
        - *i_boucle_2* : variable de boucle
        - *grille* : grille de jeu

    **Vérification :**
        - *grille* est bien initialisée avec des 0 partout avec la bonne taille
        - On teste 16 cas différents, avec des tailles différentes :
        - Toutes les combinaisons de 2 nombres de la liste *liste_tailles*
    """
    # On teste 4 cas différents, avec des tailles différentes
    liste_tailles = [2, 5, 7, 100]
    for i_boucle in liste_tailles:
        for i_boucle_2 in liste_tailles:
            grille = ps4.pq_init_grille(i_boucle, i_boucle_2)
            assert np.array_equal(grille, np.zeros((i_boucle, i_boucle_2))), \
                "pq_init_grille non fonctionnel"


def test_verif_colonne():
    """! Teste la fonction pq_verif_colonne

    **Variables :**
        - *grille* : grille de jeu
        - *i_boucle* : variable de boucle
        - *i_boucle_2* : variable de boucle

    **Vérification :**
        - On teste 5 cas différents :
        - Cas où la grille est vide
        - Cas où une colonne est pleine
        - Cas où une colonne est presque pleine
        - Cas où la grille est un peu remplie
        - Cas où la grille est pleine

    """
    grille = ps4.pq_init_grille(6, 7)
    # Cas où la grille est vide
    for i_boucle in range(0, 6):
        assert ps4.pq_verif_colonne(i_boucle, grille), \
            "pq_verif_colonne non fonctionnel dans le cas où la grille est vide"
    # Cas où une colonne est pleine
    for i_boucle in range(0, 6):
        grille[i_boucle][0] = 1
    assert not ps4.pq_verif_colonne(0, grille), \
        "pq_verif_colonne non fonctionnel dans le cas où une colonne est pleine"

    # Cas où une colonne est presque pleine
    for i_boucle in range(0, 5):
        grille[i_boucle][1] = 1
    assert ps4.pq_verif_colonne(1, grille), \
        "pq_verif_colonne non fonctionnel dans le cas où une colonne est " \
        "presque pleine"

    # Cas où la grille est un peu remplie
    for i_boucle in range(0, 3):
        for i_boucle_2 in range(0, 7):
            grille[i_boucle][i_boucle_2] = 1
    assert ps4.pq_verif_colonne(3, grille), \
        "pq_verif_colonne non fonctionnel dans le cas où la grille est " \
        "un peu remplie"

    # Cas où la grille est pleine
    for i_boucle in range(0, 7):
        for i_boucle_2 in range(0, 6):
            grille[i_boucle_2][i_boucle] = 1
        assert not ps4.pq_verif_colonne(i_boucle, grille), \
            "pq_verif_colonne non fonctionnel dans le cas où la grille est " \
            "pleine"


def test_ajout_piece():
    """! Teste la fonction pq_ajout_piece

    **Variables :**
        - *grille* : grille de jeu
        - *ti_coords* : tuple de coordonnées
        - *i_boucle* : variable de boucle

    **Vérification :**
        - On teste 4 cas différents :
        - Cas où une seule pièce est ajoutée par le joueur
        - Cas où une seule pièce est ajoutée par le bot
        - Cas normal pour le joueur
        - Cas où on ne peut pas ajouter de pièce (verif_colonne)
    """
    grille = ps4.pq_init_grille(6, 7)
    # Cas où une seule pièce est ajoutée par le joueur
    ti_coords = ps4.pq_ajout_piece(grille, 0, 1)
    assert grille[ti_coords] == 1 and ti_coords == (5, 0), \
        "pq_ajout_piece non fonctionnel dans le cas où une seule pièce est " \
        "ajoutée par le joueur"

    # Cas où une seule pièce est ajoutée par le bot
    ti_coords = ps4.pq_ajout_piece(grille, 0, 2)
    assert grille[ti_coords] == 2 and ti_coords == (4, 0), \
        "pq_ajout_piece non fonctionnel dans le cas où une seule pièce est " \
        "ajoutée par le bot"

    # Cas normal pour le joueur
    ti_coords = ps4.pq_ajout_piece(grille, 0, 1)
    assert grille[ti_coords] == 1 and ti_coords == (3, 0), \
        "pq_ajout_piece non fonctionnel dans le cas normal pour le joueur"

    # Cas où on ne peut pas ajouter de pièce (verif_colonne)
    for i_boucle in range(0, 6):
        grille[i_boucle][1] = 1
    ti_coords = ps4.pq_ajout_piece(grille, 1, 1)
    assert ti_coords == (None, None), \
        "pq_ajout_piece non fonctionnel dans le cas où on ne peut pas ajouter" \
        "de pièce"


def test_all():
    """! Fonction qui lance tous les tests unitaires
    """
    test_init_grille()
    test_verif_colonne()
    test_ajout_piece()


test_all()
