"""! @brief Un programme qui joue au jeu puissance 4++.

Ce programme est un jeu de puissance 4++ avec une grille de taille variable,
un nombre de pions à aligner variable, des bonus et un undo.

Ce programme utilise les modules externes suivants :
- tkinter
- numpy
- inspect

@package tests.test_puissanceQuatre
@brief Teste le module puissanceQuatre.puissanceQuatre
@details Ce module teste le module puissanceQuatre.puiissanceQuatre.
"""

from src.puissanceQuatre import puissanceQuatre as ps4, grid as gr


# TODO : Pour les vérifications de victoire, mettre plus de cas de non victoire


def tp_verif_colonne():
    """! Teste la fonction pq_verif_colonne

    **Variables :**
        - *npa_grille* : npa_grille de jeu
        - *i_boucle* : variable de boucle
        - *i_boucle_2* : variable de boucle

    @test Vérifie que la fonction renvoie True si la colonne est vide
    @test Vérifie que la fonction renvoie False si la colonne est pleine
    @test Vérifie que la fonction renvoie True si la colonne est presque
    pleine
    @test Vérifie que la fonction renvoie True si la colonne est un peu
    remplie
    @test Vérifie que la fonction renvoie False si la npa_grille est pleine
    """
    npa_grille = gr.pq_init_grille(6, 7)
    # Cas où la npa_grille est vide
    for i_boucle in range(0, 6):
        assert ps4.pq_verif_colonne(i_boucle, npa_grille), \
            "pq_verif_colonne non fonctionnel dans le cas où la npa_grille est vide"
    # Cas où une colonne est pleine
    for i_boucle in range(0, 6):
        npa_grille[i_boucle][0] = 1
    assert not ps4.pq_verif_colonne(0, npa_grille), \
        "pq_verif_colonne non fonctionnel dans le cas où une colonne est pleine"

    # Cas où une colonne est presque pleine
    for i_boucle in range(0, 5):
        npa_grille[i_boucle][1] = 1
    assert ps4.pq_verif_colonne(1, npa_grille), \
        "pq_verif_colonne non fonctionnel dans le cas où une colonne est " \
        "presque pleine"

    # Cas où la npa_grille est un peu remplie
    for i_boucle in range(0, 3):
        for i_boucle_2 in range(0, 7):
            npa_grille[i_boucle][i_boucle_2] = 1
    assert ps4.pq_verif_colonne(3, npa_grille), \
        "pq_verif_colonne non fonctionnel dans le cas où la npa_grille est " \
        "un peu remplie"

    # Cas où la npa_grille est pleine
    for i_boucle in range(0, 7):
        for i_boucle_2 in range(0, 6):
            npa_grille[i_boucle_2][i_boucle] = 1
        assert not ps4.pq_verif_colonne(i_boucle, npa_grille), \
            ("pq_verif_colonne non fonctionnel dans le cas où la npa_grille "
             "est pleine")


def tp_ajout_piece():
    """! Teste la fonction pq_ajout_piece

    **Variables :**
        - *npa_grille* : npa_grille de jeu
        - *ti_coords* : tuple de coordonnées
        - *i_boucle* : variable de boucle

    @test Vérifie que la fonction renvoie les bonnes coordonnées quand le
    joueur joue
    @test Vérifie que la fonction renvoie les bonnes coordonnées quand le bot
    joue
    @test Vérifie que la fonction renvoie les bonnes coordonnées quand le
    joueur joue normalement
    @test Vérifie que la fonction ne renvoie pas de coordonnées quand on ne
    peut pas ajouter de pièce
    """
    npa_grille = gr.pq_init_grille(6, 7)
    # Cas où une seule pièce est ajoutée par le joueur
    ti_coords = ps4.pq_ajout_piece(npa_grille, 0, 1)
    assert npa_grille[ti_coords] == 1 and ti_coords == (5, 0), \
        "pq_ajout_piece non fonctionnel dans le cas où une seule pièce est " \
        "ajoutée par le joueur"

    # Cas où une seule pièce est ajoutée par le bot
    ti_coords = ps4.pq_ajout_piece(npa_grille, 0, 2)
    assert npa_grille[ti_coords] == 2 and ti_coords == (4, 0), \
        "pq_ajout_piece non fonctionnel dans le cas où une seule pièce est " \
        "ajoutée par le bot"

    # Cas normal pour le joueur
    ti_coords = ps4.pq_ajout_piece(npa_grille, 0, 1)
    assert npa_grille[ti_coords] == 1 and ti_coords == (3, 0), \
        "pq_ajout_piece non fonctionnel dans le cas normal pour le joueur"

    # Cas où on ne peut pas ajouter de pièce (verif_colonne)
    for i_boucle in range(0, 6):
        npa_grille[i_boucle][1] = 1
    ti_coords = ps4.pq_ajout_piece(npa_grille, 1, 1)
    assert ti_coords == (None, None), \
        "pq_ajout_piece non fonctionnel dans le cas où on ne peut pas ajouter" \
        "de pièce"


def tp_victoire_ligne():
    """! Test de la fonction pq_victoire_ligne

    **Variables :**
    * *npa_grille* : Grille du jeu
    * *i_boucle* : Variable de boucle
    * *ti_coords* : Tuple de coordonnées

    @test Vérifie que la fonction renvoie True si le joueur gagne
    @test Vérifie que la fonction renvoie True si le bot gagne
    @test Vérifie que la fonction renvoie False si personne ne gagne
    """
    npa_grille = gr.pq_init_grille(6, 7)
    ti_coords = (0, 0)

    # Cas où le joueur gagne
    for i_boucle in range(0, 4):
        ti_coords = ps4.pq_ajout_piece(npa_grille, i_boucle, 1)
    assert ps4.pq_victoire_ligne(npa_grille, ti_coords[0], ti_coords[1],
                                 1, 4), \
        "pq_victoire_ligne non fonctionnel dans le cas où le joueur gagne"

    # Cas où le bot gagne
    gr.pq_reset_grille(npa_grille)
    for i_boucle in range(0, 4):
        ti_coords = ps4.pq_ajout_piece(npa_grille, i_boucle, 2)
    assert ps4.pq_victoire_ligne(npa_grille, ti_coords[0], ti_coords[1],
                                 2, 4), \
        "pq_victoire_ligne non fonctionnel dans le cas où le bot gagne"

    # Cas où personne ne gagne
    gr.pq_reset_grille(npa_grille)
    for i_boucle in range(0, 3):
        ti_coords = ps4.pq_ajout_piece(npa_grille, i_boucle, 2)
    assert not ps4.pq_victoire_ligne(npa_grille, ti_coords[0], ti_coords[1],
                                     2, 4), \
        "pq_victoire_ligne non fonctionnel dans le cas où personne ne gagne"


def tp_victoire_colonne():
    """! Test de la fonction pq_victoire_colonne

    **Variables :**
    * *npa_grille* : Grille du jeu
    * *i_boucle* : Variable de boucle
    * *ti_coords* : Tuple de coordonnées

    @test Vérifie que la fonction renvoie True si le joueur gagne
    @test Vérifie que la fonction renvoie True si le bot gagne
    @test Vérifie que la fonction renvoie False si personne ne gagne
    """
    npa_grille = gr.pq_init_grille(6, 7)
    ti_coords = (0, 0)
    # Cas où le joueur gagne
    for i_boucle in range(0, 4):
        ti_coords = ps4.pq_ajout_piece(npa_grille, 0, 1)
    assert ps4.pq_victoire_colonne(npa_grille, ti_coords[0], ti_coords[1],
                                   1, 4), \
        "pq_victoire_colonne non fonctionnel dans le cas où le joueur gagne"

    # Cas où le bot gagne
    gr.pq_reset_grille(npa_grille)
    for i_boucle in range(0, 4):
        ti_coords = ps4.pq_ajout_piece(npa_grille, 0, 2)
    assert ps4.pq_victoire_colonne(npa_grille, ti_coords[0], ti_coords[1], 2, 4), \
        "pq_victoire_colonne non fonctionnel dans le cas où le bot gagne"

    # Cas où personne ne gagne
    gr.pq_reset_grille(npa_grille)
    for i_boucle in range(0, 3):
        ti_coords = ps4.pq_ajout_piece(npa_grille, 0, 2)
    assert not ps4.pq_victoire_colonne(npa_grille, ti_coords[0], ti_coords[1], 2,
                                       4), \
        "pq_victoire_colonne non fonctionnel dans le cas où personne ne gagne"


def tp_victoire_diago():
    """! Test de la fonction pq_victoire_diagonale

    **Variables :**
    * *npa_grille* : Grille du jeu
    * *i_boucle* : Variable de boucle
    * *i_boucle_2* : Variable de boucle
    * *ti_coords* : Tuple de coordonnées

    @test Vérifie que la fonction renvoie True si le joueur gagne
    @test Vérifie que la fonction renvoie True si le bot gagne
    @test Vérifie que la fonction renvoie False si personne ne gagne
    """
    npa_grille = gr.pq_init_grille(6, 7)
    ti_coords = (0, 0)
    # Cas où le joueur gagne
    for i_boucle in range(0, 4):
        for i_boucle2 in range(0, i_boucle):
            ps4.pq_ajout_piece(npa_grille, i_boucle, 2)
        ti_coords = ps4.pq_ajout_piece(npa_grille, i_boucle, 1)
    assert ps4.pq_victoire_diago(npa_grille, ti_coords[0], ti_coords[1],
                                 1, 4), \
        "pq_victoire_diagonale non fonctionnel dans le cas où le joueur gagne"

    # Cas où le bot gagne
    gr.pq_reset_grille(npa_grille)
    for i_boucle in range(0, 4):
        for i_boucle2 in range(0, i_boucle):
            ps4.pq_ajout_piece(npa_grille, i_boucle, 1)
        ti_coords = ps4.pq_ajout_piece(npa_grille, i_boucle, 2)
    assert ps4.pq_victoire_diago(npa_grille, ti_coords[0], ti_coords[1],
                                 2, 4), \
        "pq_victoire_diagonale non fonctionnel dans le cas où le bot gagne"

    # Cas où personne ne gagne
    gr.pq_reset_grille(npa_grille)
    for i_boucle in range(0, 3):
        for i_boucle2 in range(0, i_boucle):
            ps4.pq_ajout_piece(npa_grille, i_boucle, 1)
        ti_coords = ps4.pq_ajout_piece(npa_grille, i_boucle, 2)
    assert not ps4.pq_victoire_diago(npa_grille, ti_coords[0], ti_coords[1],
                                     2, 4), \
        "pq_victoire_diagonale non fonctionnel dans le cas où personne ne " \
        "gagne"


def tp_test_all():
    """! Fonction qui lance tous les tests unitaires
    """
    tp_verif_colonne()
    tp_ajout_piece()
    tp_victoire_ligne()
    tp_victoire_colonne()
    tp_victoire_diago()


if __name__ == "__main__":
    tp_test_all()
