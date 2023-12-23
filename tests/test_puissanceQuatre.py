"""! @brief Un programme qui joue au jeu puissance 4++.

@mainpage Projet Puissance 4++

@section description_main Description
Ce programme est un jeu de puissance 4++ avec une grille de taille variable,
un nombre de pions à aligner variable, des bonus et un undo.

@section import_section Importations
Ce programme utilise les modules externes suivants :
- tkinter
- numpy

@package tests.test_puissanceQuatre
@brief Teste le module puissanceQuatre.puissanceQuatre
@details Ce module teste le module puissanceQuatre.puiissanceQuatre.
"""

from src.puissanceQuatre import puissanceQuatre as ps4, grid as gr


# TODO : Pour les vérifications de victoire, mettre plus de cas de non victoire


def test_verif_colonne():
    """! Teste la fonction pq_verif_colonne

    **Variables :**
        - *grille* : grille de jeu
        - *i_boucle* : variable de boucle
        - *i_boucle_2* : variable de boucle

    @test : Vérifie que la fonction renvoie True si la colonne est vide
    @test : Vérifie que la fonction renvoie False si la colonne est pleine
    @test : Vérifie que la fonction renvoie True si la colonne est presque
    pleine
    @test : Vérifie que la fonction renvoie True si la colonne est un peu
    remplie
    @test : Vérifie que la fonction renvoie False si la grille est pleine
    """
    grille = gr.pq_init_grille(6, 7)
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

    @test : Vérifie que la fonction renvoie les bonnes coordonnées quand le
    joueur joue
    @test : Vérifie que la fonction renvoie les bonnes coordonnées quand le bot
    joue
    @test : Vérifie que la fonction renvoie les bonnes coordonnées quand le
    joueur joue normalement
    @test : Vérifie que la fonction ne renvoie pas de coordonnées quand on ne
    peut pas ajouter de pièce
    """
    grille = gr.pq_init_grille(6, 7)
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


def test_victoire_ligne():
    """! Test de la fonction pq_victoire_ligne

    **Variables :**
    * *grille* : Grille du jeu
    * *i_boucle* : Variable de boucle
    * *ti_coords* : Tuple de coordonnées

    @test : Vérifie que la fonction renvoie True si le joueur gagne
    @test : Vérifie que la fonction renvoie True si le bot gagne
    @test : Vérifie que la fonction renvoie False si personne ne gagne
    """
    grille = gr.pq_init_grille(6, 7)
    ti_coords = (0, 0)

    # Cas où le joueur gagne
    for i_boucle in range(0, 4):
        ti_coords = ps4.pq_ajout_piece(grille, i_boucle, 1)
    assert ps4.pq_victoire_ligne(grille, ti_coords[0], ti_coords[1],
                                 1, 4), \
        "pq_victoire_ligne non fonctionnel dans le cas où le joueur gagne"

    # Cas où le bot gagne
    gr.pq_reset_grille(grille)
    for i_boucle in range(0, 4):
        ti_coords = ps4.pq_ajout_piece(grille, i_boucle, 2)
    assert ps4.pq_victoire_ligne(grille, ti_coords[0], ti_coords[1],
                                 2, 4), \
        "pq_victoire_ligne non fonctionnel dans le cas où le bot gagne"

    # Cas où personne ne gagne
    gr.pq_reset_grille(grille)
    for i_boucle in range(0, 3):
        ti_coords = ps4.pq_ajout_piece(grille, i_boucle, 2)
    assert not ps4.pq_victoire_ligne(grille, ti_coords[0], ti_coords[1],
                                     2, 4), \
        "pq_victoire_ligne non fonctionnel dans le cas où personne ne gagne"


def test_victoire_colonne():
    """! Test de la fonction pq_victoire_colonne

    **Variables :**
    * *grille* : Grille du jeu
    * *i_boucle* : Variable de boucle
    * *ti_coords* : Tuple de coordonnées

    @test : Vérifie que la fonction renvoie True si le joueur gagne
    @test : Vérifie que la fonction renvoie True si le bot gagne
    @test : Vérifie que la fonction renvoie False si personne ne gagne
    """
    grille = gr.pq_init_grille(6, 7)
    ti_coords = (0, 0)
    # Cas où le joueur gagne
    for i_boucle in range(0, 4):
        ti_coords = ps4.pq_ajout_piece(grille, 0, 1)
    assert ps4.pq_victoire_colonne(grille, ti_coords[0], ti_coords[1],
                                   1, 4), \
        "pq_victoire_colonne non fonctionnel dans le cas où le joueur gagne"

    # Cas où le bot gagne
    gr.pq_reset_grille(grille)
    for i_boucle in range(0, 4):
        ti_coords = ps4.pq_ajout_piece(grille, 0, 2)
    assert ps4.pq_victoire_colonne(grille, ti_coords[0], ti_coords[1], 2, 4), \
        "pq_victoire_colonne non fonctionnel dans le cas où le bot gagne"

    # Cas où personne ne gagne
    gr.pq_reset_grille(grille)
    for i_boucle in range(0, 3):
        ti_coords = ps4.pq_ajout_piece(grille, 0, 2)
    assert not ps4.pq_victoire_colonne(grille, ti_coords[0], ti_coords[1], 2,
                                       4), \
        "pq_victoire_colonne non fonctionnel dans le cas où personne ne gagne"


def test_victoire_diago():
    """! Test de la fonction pq_victoire_diagonale

    **Variables :**
    * *grille* : Grille du jeu
    * *i_boucle* : Variable de boucle
    * *i_boucle_2* : Variable de boucle
    * *ti_coords* : Tuple de coordonnées

    @test : Vérifie que la fonction renvoie True si le joueur gagne
    @test : Vérifie que la fonction renvoie True si le bot gagne
    @test : Vérifie que la fonction renvoie False si personne ne gagne
    """
    grille = gr.pq_init_grille(6, 7)
    ti_coords = (0, 0)
    # Cas où le joueur gagne
    for i_boucle in range(0, 4):
        for i_boucle2 in range(0, i_boucle):
            ps4.pq_ajout_piece(grille, i_boucle, 2)
        ti_coords = ps4.pq_ajout_piece(grille, i_boucle, 1)
    assert ps4.pq_victoire_diago(grille, ti_coords[0], ti_coords[1],
                                 1, 4), \
        "pq_victoire_diagonale non fonctionnel dans le cas où le joueur gagne"

    # Cas où le bot gagne
    gr.pq_reset_grille(grille)
    for i_boucle in range(0, 4):
        for i_boucle2 in range(0, i_boucle):
            ps4.pq_ajout_piece(grille, i_boucle, 1)
        ti_coords = ps4.pq_ajout_piece(grille, i_boucle, 2)
    assert ps4.pq_victoire_diago(grille, ti_coords[0], ti_coords[1],
                                 2, 4), \
        "pq_victoire_diagonale non fonctionnel dans le cas où le bot gagne"

    # Cas où personne ne gagne
    gr.pq_reset_grille(grille)
    for i_boucle in range(0, 3):
        for i_boucle2 in range(0, i_boucle):
            ps4.pq_ajout_piece(grille, i_boucle, 1)
        ti_coords = ps4.pq_ajout_piece(grille, i_boucle, 2)
    assert not ps4.pq_victoire_diago(grille, ti_coords[0], ti_coords[1],
                                     2, 4), \
        "pq_victoire_diagonale non fonctionnel dans le cas où personne ne " \
        "gagne"


def test_all():
    """! Fonction qui lance tous les tests unitaires
    """
    test_verif_colonne()
    test_ajout_piece()
    test_victoire_ligne()
    test_victoire_colonne()
    test_victoire_diago()


test_all()
