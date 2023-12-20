"""! **puissanceQuatre**
Ce module contient l'implémentation des règles du puissance 4.

Ce module contient la gestion de la structure du puissance 4 et
la gestion du jeu.

@see test_puissanceQuatre.py
"""
import random
import numpy as np
import grid as gr


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
    * b_victoire : Booléen, Indique si le joueur a gagné ou non

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
    # Initialisation du booléen de victoire à faux
    b_victoire = False
    # Récupération du nombre de lignes de la grille
    i_max_ligne = npa_grille.shape[0]
    # Si le nombre de lignes restantes est suffisant pour gagner
    if i_max_ligne >= (i_nb_victoire + i_ligne):
        i_compteur = 1
        while (i_compteur < i_nb_victoire) and (
                npa_grille[i_ligne + i_compteur][i_colonne] == i_joueur):
            i_compteur += 1
        b_victoire = i_compteur >= i_nb_victoire
    return b_victoire


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
    # Récupération de la taille de la grille
    i_nb_lignes, i_nb_colonnes = npa_grille.shape
    # Initialisation du booléen à vrai afin de pouvoir le nier
    b_tableau_plein = True
    # Initialisation du compteur de boucle pour les lignes
    i_boucle_ligne = 0
    # Initialisation du compteur de boucle pour les colonnes
    i_boucle_colonne = 0

    # Tant que le tableau est supposé plein et qu'on n'a pas parcouru toutes
    # les lignes
    while i_boucle_ligne <= i_nb_lignes and b_tableau_plein:
        # Tant que le tableau est supposé plein et qu'on n'a pas parcouru toutes
        # les colonnes
        while i_boucle_colonne <= i_nb_colonnes and b_tableau_plein:
            # Si la case est vide
            if npa_grille[i_boucle_ligne, i_boucle_colonne] == 0:
                # Le tableau n'est pas plein
                b_tableau_plein = False
            # On incrémente le compteur de colonne
            i_boucle_colonne += 1
        # On incrémente le compteur de ligne
        i_boucle_ligne += 1
    # On retourne le résultat de la négation du booléen
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
    # Initialisation d'un booléen pour savoir s'il y a une victoire
    b_victoire = False
    # Initialisation d'un booléen pour savoir si le joueur a utilisé son bonus
    b_bonus_utilise = False
    # Initialisation d'une liste pour l'undo et le redo
    t_undo_redo = []
    # Initialisation de la grille de jeu
    npa_grille = gr.pq_init_grille(i_nb_lignes, i_nb_colonnes)
    # Initialisation de la colonne où le joueur veut jouer
    i_colonne_joueur = 0
    # Initialisation de la ligne où le joueur veut jouer
    i_ligne_joueur = 0

    # Affichage des règles du jeu
    print("Bienvenue dans le puissance 4 !\n"
          "Pour jouer, entrez le numéro de la colonne où vous voulez jouer.\n"
          "Vos jetons sont représentés par des X, ceux du bot par des 0.\n"
          "Pour utiliser votre bonus, entrez 0. (WIP)\n")

    # Tant que la partie n'est pas finie et qu'il n'y a pas de victoire
    while not pq_partie_finie(npa_grille, b_bonus_utilise) and not b_victoire:
        # Initialisation de la colonne où le joueur veut jouer à -1 afin de
        # pouvoir vérifier que la colonne est valide
        i_colonne_joueur = -1
        # Affichage de la grille
        gr.pq_print_grille(npa_grille)
        # Tant que la colonne n'est pas valide
        while (not (0 <= i_colonne_joueur < i_nb_colonnes)
               and pq_verif_colonne(i_colonne_joueur, npa_grille)):
            # Demande de la colonne où le joueur veut jouer
            i_colonne_joueur = int(input("\nDans quelle colonne voulez vous "
                                         "jouer ? ")) - 1
        # Pose du jeton et récupération de la ligne où le jeton a été posé
        i_ligne_joueur, _ = pq_ajout_piece(npa_grille, i_colonne_joueur, 1)

        # Si le joueur a gagné
        if (pq_victoire(npa_grille, i_ligne_joueur, i_colonne_joueur,
                        1, i_nb_jeton_victoire)):
            # Affichage de la grille
            gr.pq_print_grille(npa_grille)
            # Affichage du message de victoire
            print("Le joueur 1 a gagné !")
            # Passage du booléen de victoire à vrai
            b_victoire = True
        # Sinon
        else:
            # Choix de la colonne où le bot va jouer (random pour commencer)
            i_colonne_joueur = random.randint(0, i_nb_colonnes)
            # Pose du jeton et récupération de la ligne où le jeton a été posé
            i_ligne_joueur, _ = pq_ajout_piece(npa_grille, i_colonne_joueur, 2)

            # Si le bot a gagné
            if (pq_victoire(npa_grille, i_ligne_joueur, i_colonne_joueur,
                            2, i_nb_jeton_victoire)):
                # Affichage de la grille
                gr.pq_print_grille(npa_grille)
                # Affichage du message de victoire
                print("Le joueur 2 a gagné !")
                # Passage du booléen de victoire à vrai
                b_victoire = True
        # Ajout de la grille à la liste pour l'undo et le redo
        t_undo_redo.append(npa_grille)
    # Fin de partie
    return


if __name__ == '__main__':
    pq_gestion_partie(6, 7, 4)
