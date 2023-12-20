"""! **puissanceQuatre**
Ce module contient l'implémentation des règles du puissance 4.

Ce module contient la gestion de la structure du puissance 4 et
la gestion du jeu.

@see test_puissanceQuatre.py
"""
import random

import numpy as np


def pq_init_grille(i_max_ligne: int, i_max_colonne: int) -> np.array:
    """! L'initiateur de la grille

    **Variables :**
    * npa_grille : np.array

    **Préconditions :**
    * i_max_ligne > 1
    * i_max_colonne > 1

    **Postconditions :**
    * npa_grille initialisé

    @param i_max_ligne: Le nombre de lignes de la grille
    @param i_max_colonne: Le nombre de colonnes de la grille

    @return La grille créée
    """
    assert i_max_ligne > 1 and i_max_colonne > 1, \
        "La grille doit avoir au moins 2 lignes et 2 colonnes"
    # Création de la grille
    npa_grille = np.zeros((i_max_ligne, i_max_colonne))
    # Changement du type contenu dans la grille par "int"
    npa_grille.astype(int)
    # Retourne la grille
    return npa_grille


def pq_verif_colonne(i_colonne: int, npa_grille: np.array) -> bool:
    """! Vérifie si on peut poser un jeton dans cette colonne

    **Variable :**
    * b_resultat : Booléen
    * i_boucle : Entier

    **Préconditions :**
    * 0 < i_colonne ≤ npa_grille.shape[0]
    * npa_grille initialisé

    **Postconditions :**
    * npa_grille[i_colonne] contient au moins un 0

    @param i_colonne: La colonne où on souhaite poser un jeton
    @param npa_grille: La grille de jeu

    @return True si on peut poser le jeton, False sinon
    """
    # Initialisation du booléen a faux
    b_resultat = False
    # Récupération de la taille de la grille
    i_max_ligne, _ = npa_grille.shape
    # Pour chaque ligne de la grille
    for i_boucle in range(i_max_ligne):
        # b_resultat reçoit Vrai si la case est bien vide
        b_resultat = b_resultat or (npa_grille[i_boucle][i_colonne] == 0)

    # Retourner le résultat
    return b_resultat


def pq_ajout_piece(npa_grille: np.array, i_colonne: int,
                   i_joueur: int) -> (int, int):
    """! La méthode qui gère le placement de jetons

    **Variables :**
    * i_boucle : Entier
    * i_max_ligne : Entier
    * i_boucle : Entier

    **Preconditions :**
    * 0 < i_colonne ≤ npa_grille.shape[0]
    * npa_grille initialisé

    **Postconditions :**
    * npa_grille contient un nouvel entier

    @param i_colonne: La colonne où le joueur pose le jeton
    @param i_joueur: Le joueur qui joue (1 pour le joueur, 2 pour le bot)
    @param npa_grille: La grille du puissance 4

    @return Les coordonnées du nouveau jeton
    """
    # Initialise le compteur de boucle
    i_boucle = 0
    # Récupère la taille de la grille
    i_max_ligne, _ = npa_grille.shape
    # Initialisation des coordonnées du nouveau jeton
    ti_coords = (None, None)

    # Si on peut jouer dans la colonne
    if pq_verif_colonne(i_colonne, npa_grille):
        # Tant que la case de la grille de notre colonne est vide
        while i_boucle < i_max_ligne and npa_grille[i_boucle][i_colonne] == 0:
            # Augmenter le compteur de boucle
            i_boucle += 1
        # Ajouter le jeton du joueur dans la dernière case vide
        npa_grille[i_boucle - 1][i_colonne] = i_joueur
        # Retourner un tuple des coordonnées du nouveau jeton
        ti_coords = (i_boucle - 1, i_colonne)
    return ti_coords


def pq_victoire(npa_grille: np.array, i_ligne: int, i_colonne: int,
                i_joueur: int, i_nb_victoire: int) -> bool:
    """: Méthode appelant les trois vérifications de victoire.

    @param npa_grille: La grille du puissance 4
    @param i_ligne: La ligne où le jeton a été posé
    @param i_colonne: La colonne où le jeton a été posé
    @param i_joueur: Le joueur qui a joué (1 pour le joueur humain, 2 pour le
                    bot)
    @param i_nb_victoire: Nombre de jetons à combiner pour gagner
    @return True si le joueur i_joueur a gagné, False sinon
    """
    return (pq_victoire_ligne(npa_grille, i_ligne, i_colonne, i_joueur,
                              i_nb_victoire)
            or pq_victoire_colonne(npa_grille, i_ligne, i_colonne, i_joueur,
                                   i_nb_victoire)
            or pq_victoire_diago(npa_grille, i_ligne, i_colonne, i_joueur,
                                 i_nb_victoire))


def pq_victoire_ligne(npa_grille: np.array, i_ligne: int, i_colonne: int,
                      i_joueur: int, i_nb_victoire: int) -> bool:
    """! Verification de la victoire sur la ligne

    **Variables :**
    * i_compteur : Entier, Le nombre de jetons du joueur dans la ligne
    * b_vu : Booléen, ajouter explication
    * b_suite : Booléen, ajouter explication
    * i_max_colonne : Entier, Nombre de colonnes dans la grille
    * i_boucle : Entier, Compteur de boucle
    * i_debut : Entier, premier emplacement possible pour la combinaison de
            victoire dans la ligne
    * i_fin : Entier, dernier emplacement possible pour la combinaison de
            victoire dans la ligne

    **Préconditions :**
    * npa_grille initialisé
    * npa_grille contient un jeton en i_ligne, i_colonne
    * 1 ≤ i_joueur ≤ 2


    @param npa_grille: La grille du jeu
    @param i_ligne: La ligne où le jeton a été posé
    @param i_colonne: La colonne où le jeton a été posé
    @param i_joueur: Le joueur qui a joué
    @param i_nb_victoire: Le nombre de jetons nécessaire pour la victoire

    @return True si le joueur a gagné, False sinon
    """
    i_compteur = 0
    b_vu = False
    b_suite = False
    _, i_max_colonne = npa_grille.shape

    if i_ligne >= i_nb_victoire - 1:
        iDebut = i_colonne - i_nb_victoire + 1
        iFin = i_colonne + i_nb_victoire - 1

        if iDebut < 0:
            iDebut = 0

        if iFin > i_max_colonne:
            iFin = i_max_colonne

        for i_boucle in range(iDebut, iFin):
            if npa_grille[i_ligne][i_boucle] == i_joueur and not b_vu:
                b_vu = True
                b_suite = True
                i_compteur = 1
            elif npa_grille[i_ligne][i_boucle] == i_joueur and b_suite:
                i_compteur += 1
            elif npa_grille[i_ligne][i_boucle] != i_joueur and b_vu:
                b_suite = False

        return i_compteur >= i_nb_victoire
    else:
        return False


def pq_victoire_colonne(npa_grille: np.array, i_ligne: int, i_colonne: int,
                        i_joueur: int, i_nb_victoire: int) -> bool:
    """! Verification de la victoire sur une colonne

    **Variables :**
    * i_compteur : Entier, Le nombre de jetons du joueur dans la ligne
    * i_max_ligne : Entier, Nombre de lignes dans la grille

    **Préconditions :**
    * npa_grille initialisé
    * npa_grille contient un jeton en i_ligne, i_colonne
    * 1 ≤ i_joueur ≤ 2

    @param npa_grille: La grille du puissance 4
    @param i_ligne: La ligne où le jeton a été posé
    @param i_colonne: La colonne où le jeton a été posé
    @param i_joueur: Le joueur qui a joué
    @param i_nb_victoire: Le nombre de jetons nécessaire pour la victoire
    @return True si le joueur i_joueur a gagné, False sinon
    """
    i_max_ligne = npa_grille.shape[0]
    if i_max_ligne >= (i_nb_victoire + i_ligne):
        i_compteur = 1
        while (i_compteur < i_nb_victoire) and (
                npa_grille[i_ligne + i_compteur][i_colonne] == i_joueur):
            i_compteur += 1
        return i_compteur >= i_nb_victoire
    else:
        return False


def pq_victoire_diago(npa_grille: np.array, i_ligne: int, i_colonne: int,
                      i_joueur: int, i_nb_victoire: int) -> bool:
    """! Verification de la victoire sur les diagonales

    **Variables :**
    * i_compteur : Entier, Le nombre de jetons du joueur dans la ligne
    * i_max_ligne : Entier, Nombre de lignes dans la grille
    * i_max_colonne : Entier, Nombre de colonnes dans la grille

    **Préconditions :**
    * npa_grille initialisé
    * npa_grille contient un jeton en i_ligne, i_colonne
    * 1 ≤ i_joueur ≤ 2

    @param npa_grille: La grille du puissance 4
    @param i_ligne: La ligne où le jeton a été posé
    @param i_colonne: La colonne où le jeton a été posé
    @param i_joueur: Le joueur qui a joué
    @param i_nb_victoire: Le nombre de jetons nécessaire pour la victoire
    @return True si le joueur i_joueur a gagné, False sinon
    """
    i_max_ligne, i_max_colonne = npa_grille.shape
    i_compteur = 1
    while ((i_ligne + i_compteur < i_max_ligne)
           and (i_colonne - i_compteur >= 0)
           and (i_compteur < i_nb_victoire)
           and (
                   npa_grille[i_ligne + i_compteur][
                       i_colonne - i_compteur] == i_joueur)):
        i_compteur += 1
    if i_compteur >= i_nb_victoire:
        return True
    i_compteur = 1
    while ((i_ligne - i_compteur >= 0)
           and (i_colonne - i_compteur >= 0)
           and (i_compteur < i_nb_victoire)
           and (
                   npa_grille[i_ligne - i_compteur][
                       i_colonne - i_compteur] == i_joueur)):
        i_compteur += 1
    if i_compteur >= i_nb_victoire:
        return True
    i_compteur = 1
    while ((i_ligne + i_compteur < i_max_ligne)
           and (i_colonne + i_compteur < i_max_colonne)
           and (i_compteur < i_nb_victoire)
           and (
                   npa_grille[i_ligne + i_compteur][
                       i_colonne + i_compteur] == i_joueur)):
        i_compteur += 1
    if i_compteur >= i_nb_victoire:
        return True
    i_compteur = 1
    while ((i_ligne + i_compteur >= 0)
           and (i_colonne + i_compteur < i_max_colonne)
           and (i_compteur < i_nb_victoire)
           and (
                   npa_grille[i_ligne - i_compteur][
                       i_colonne + i_compteur] == i_joueur)):
        i_compteur += 1
    if i_compteur >= i_nb_victoire:
        return True
    return False


def pq_print_grille(npa_grille: np.array):
    """! Affiche la grille

    **Variables :**
    * char_joueur : Le caractère du jeton du joueur
    * char_bot : Le caractère du jeton du bot
    * char_vide : Le caractère représentant une case vide
    * i_max_ligne : Le nombre de lignes de la grille
    * i_max_colonne : Le nombre de colonnes de la grille
    * i_boucle_colonne : Le compteur de boucle pour les colonnes de la grille
    * i_boucle_ligne : Le compteur de boucle pour les lignes de la grille

    @param npa_grille: La grille à afficher
    """
    # Le caractère du jeton du joueur
    char_joueur = 'X'
    # Le caractère du jeton du bot
    char_bot = '0'
    # Le caractère représentant une case vide
    char_vide = ' '
    # Récupère la taille de la grille
    i_max_ligne, i_max_colonne = npa_grille.shape

    # Pour chaque colonne du tableau
    for i_boucle_ligne in range(i_max_ligne):
        # Pour chaque case de cette colonne
        for i_boucle_colonne in range(i_max_colonne):
            if npa_grille[i_boucle_ligne, i_boucle_colonne] == 1:
                # Affiche charJoueur si le joueur est le joueur humain
                print(f"|{char_joueur}", end="")
            elif npa_grille[i_boucle_ligne, i_boucle_colonne] == 2:
                # Affiche charBot si le joueur est le bot
                print(f"|{char_bot}", end="")
            else:
                # Affiche charVide si la case est vide
                print(f"|{char_vide}", end="")
        # Retourne à la ligne et affiche la barre de séparation des lignes
        print("|\n" + (2 * i_max_colonne + 1) * "-")


def pq_partie_finie(npa_grille: np.array, b_bonus_utilise: bool) -> bool:
    """! Vérification de si la partie est finie ou non.

    La vérification se fait avec deux critères : Si la grille est pleine ou non,
    ainsi que si le joueur peut encore utiliser son bonus.

    **Variables :**
    * i_nb_lignes : Le nombre de lignes de la grille
    * i_nb_colonnes : Le nombre de colonnes de la grille
    * b_tableau_plein : Booléen, True si la grille est pleine, False sinon
    * i_boucle_ligne : Entier, Compteur de boucle pour les lignes
    * i_boucle_colonne : Entier, Compteur de boucle pour les colonnes

    **Préconditions :**
    * npa_grille initialisé
    * 2 ≤ i_nb_lignes
    * 2 ≤ i_nb_colonnes

    @param npa_grille: La grille du puissance 4
    @param b_bonus_utilise: Un booléen permettant de savoir si le joueur a
        utilisé son bonus ou non.
    @return True si la partie est finie, False sinon
    """
    i_nb_lignes, i_nb_colonnes = npa_grille.shape
    b_tableau_plein = True
    i_boucle_ligne = 0
    i_boucle_colonne = 0

    while i_boucle_ligne <= i_nb_lignes and b_tableau_plein:
        while i_boucle_colonne <= i_nb_colonnes and b_tableau_plein:
            if npa_grille[i_boucle_ligne, i_boucle_colonne] == 0:
                b_tableau_plein = False
            i_boucle_colonne += 1
        i_boucle_ligne += 1

    return b_tableau_plein or b_bonus_utilise


def pq_gestion_partie(i_nb_lignes: int = 6, i_nb_colonnes: int = 7,
                      i_nb_jeton_victoire: int = 4):
    """! Gère le déroulement d'une partie de puissance 4

    Méthode gérant le déroulement d'une partie de puissance 4 en ligne de
    commande.

    **Variables :**
    * b_victoire : Booléen, True si un joueur a gagné, False sinon
    * b_bonus_utilise : Booléen, True si le joueur a utilisé son bonus, False
        sinon
    * t_undo_redo : Liste, contient les grilles pour l'undo et le redo
    * npa_grille : np.array, la grille de jeu
    * i_colonne_joueur : Entier, la colonne où le joueur veut jouer
    * i_ligne_joueur : Entier, la ligne où le joueur veut jouer

    @param i_nb_lignes: Taille de la grille en lignes
    @param i_nb_colonnes: Taille de la grille en colonnes
    @param i_nb_jeton_victoire:  Nombre de jetons à aligner pour gagner
    """
    b_victoire = False
    b_bonus_utilise = False
    t_undo_redo = []
    npa_grille = pq_init_grille(i_nb_lignes, i_nb_colonnes)
    i_colonne_joueur = 0
    i_ligne_joueur = 0

    print("Bienvenue dans le puissance 4 !")
    print("Pour jouer, entrez le numéro de la colonne où vous voulez jouer.")
    print("Vos jetons sont représentés par des X, ceux du bot par des 0.")
    # WIP
    print("Pour utiliser votre bonus, entrez 0. (WIP)")

    while not pq_partie_finie(npa_grille, b_bonus_utilise) and not b_victoire:
        i_colonne_joueur = -1
        pq_print_grille(npa_grille)
        while (not (0 <= i_colonne_joueur < i_nb_colonnes)
               and pq_verif_colonne(i_colonne_joueur, npa_grille)):
            i_colonne_joueur = int(input("\nDans quelle colonne voulez vous "
                                         "jouer ? ")) - 1

        i_ligne_joueur, _ = pq_ajout_piece(npa_grille, i_colonne_joueur, 1)

        if (pq_victoire(npa_grille, i_ligne_joueur, i_colonne_joueur,
                        1, i_nb_jeton_victoire)):
            pq_print_grille(npa_grille)
            print("Le joueur 1 a gagné !")
            b_victoire = True
        else:
            # Appel du minMax (random pour commencer
            i_colonne_joueur = random.randint(0, i_nb_colonnes)
            i_ligne_joueur, _ = pq_ajout_piece(npa_grille, i_colonne_joueur, 2)

            if (pq_victoire(npa_grille, i_ligne_joueur, i_colonne_joueur,
                            2, i_nb_jeton_victoire)):
                pq_print_grille(npa_grille)
                print("Le joueur 2 a gagné !")
                b_victoire = True
        t_undo_redo.append(npa_grille)


if __name__ == '__main__':
    pq_gestion_partie(6, 7, 4)
