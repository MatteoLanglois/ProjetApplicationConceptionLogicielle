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
- inspect

@package src.puissanceQuatre.puissanceQuatre
@brief Ce module contient l'implémentation des règles du puissance 4.
@details Ce module contient la gestion de la structure du puissance 4 et
la gestion du jeu.
"""
# Importation de numpy
import numpy as np
# Importation de la grille
from src.puissanceQuatre import grid as gr
# Importation des bonus
from src.utils import bonus_utils as bu


def pq_verif_colonne(i_colonne: int, npa_grille: np.array) -> bool:
    """! Vérifie si on peut poser un jeton dans cette colonne

    Cette fonction permet de vérifier si on peut poser un jeton dans une
    colonne donnée. Elle vérifie si la colonne est valide et si elle n'est pas
    pleine. Elle renvoie un booléen indiquant si on peut poser un jeton dans
    cette colonne ou non.

    @pre 0 < i_colonne <= npa_grille.shape[0]
    @pre npa_grille initialisé
    @param i_colonne: La colonne où on souhaite poser un jeton
    @param npa_grille: La grille de jeu
    @post npa_grille[i_colonne] contient au moins un 0
    @return True si on peut poser le jeton, False sinon

    **Variable :**
    * b_resultat : Booléen
    * i_boucle : Entier
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

    Cette méthode permet de placer un jeton dans une colonne donnée. Elle
    vérifie si la colonne est valide et si elle n'est pas pleine. Elle renvoie
    les coordonnées du nouveau jeton.

    @pre 0 < i_colonne <= npa_grille.shape[0]
    @pre npa_grille initialisé
    @param i_colonne: La colonne où le joueur pose le jeton
    @param i_joueur: Le joueur qui joue (1 pour le joueur, 2 pour le bot)
    @param npa_grille: La grille du puissance 4
    @post npa_grille contient un nouvel entier
    @return Les coordonnées du nouveau jeton

    **Variables :**
    * i_boucle **Entier** : Compteur de boucle
    * i_max_ligne **Entier** : Nombre de lignes dans la grille
    * ti_coords **Tuple d'entiers** : Coordonnées du nouveau jeton
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
    # Retourner les coordonnées du nouveau jeton
    return ti_coords


def pq_minmax(iJoueur, npaGrilleCopy, i_nb_victoire, s_bonus, b_bonus_used,
              iColonne=0,
              isFirst=False, tour=0, isthebonus = False) -> (int, float):
    """! Méthode implémentant l'algorithme minmax
    """
    # Pour éviter de faire trop de calculs, on limite le nombre de tours à 5
    if tour < 2:
        # Si le joueur est le joueur humain
        if iJoueur == 1:
            # Si on joue un bonus
            if iColonne == -1:
                # On importe le module du bonus
                m_module = __import__("src.puissanceQuatre.bonus",
                                      fromlist=["bonus"])
                # On récupère la fonction du bonus
                f_bonus = getattr(m_module, bu.bu_unformat_bonus_name(s_bonus))
                # On applique le bonus à la grille
                npaGrilleCopy = f_bonus(npaGrilleCopy.copy())
                # On indique que le bonus a été utilisé
                b_bonus_used = True
            # Sinon
            else:
                # On joue le jeton dans la colonne
                ligne, _ = pq_ajout_piece(npaGrilleCopy, iColonne, iJoueur)
                # Si le joueur a gagné
                if pq_victoire(npaGrilleCopy, ligne, iColonne, iJoueur,
                               i_nb_victoire):
                    # On retourne 10
                    if isthebonus:
                        return -10
                    else:
                        return 10
            # Si la partie est finie
            if pq_partie_finie(npaGrilleCopy, False):
                # On retourne 0, indiquant un chemin neutre
                return 0
        # Sinon si c'est à l'ordinateur de jouer, et qu'il ne s'agit pas du
        # premier appel
        elif iJoueur == 2 and not isFirst:
            # On joue le jeton dans la colonne
            ligne, _ = pq_ajout_piece(npaGrilleCopy, iColonne, iJoueur)
            # Si l'ordinateur a gagné
            if pq_victoire(npaGrilleCopy, ligne, iColonne, iJoueur,
                           i_nb_victoire):
                # On retourne -10
                if isthebonus:
                    return 10
                else:
                    return -10
            # Si la partie est finie
            elif pq_partie_finie(npaGrilleCopy, False):
                # On retourne 0, indiquant un chemin neutre
                return 0
        # On change de joueur
        if iJoueur == 1:
            iJoueur = 2
        else:
            iJoueur = 1
        # On crée la liste qui contiendra les résultats
        result = []
        # Pour chaque colonne de la grille
        for i in range(npaGrilleCopy.shape[1]):
            # Si on peut jouer dans la colonne
            if pq_verif_colonne(i, npaGrilleCopy):
                # On ajoute le résultat de l'appel récursif dans la liste (la
                # moyenne des coups joués)
                result.append(
                    pq_minmax(iJoueur, npaGrilleCopy.copy(), i_nb_victoire,
                              s_bonus, b_bonus_used, i,
                              False, tour + 1))
            else:
                # Si on ne peut pas jouer dans la colonne, on renvoie -1 (cela évite mieux ces colonnes)
                result.append(-1)
        # Si le bonus n'a pas encore été joué
        if not b_bonus_used and iJoueur == 1:
            # On enregistre aussi l'appel qui joue le bonus
            result.append(
                pq_minmax(iJoueur, npaGrilleCopy.copy(), i_nb_victoire, s_bonus,
                          False, -1, False, tour + 1))
        # Si c'est le premier appel
        if iJoueur == 1 and isFirst:
            # On retourne l'indice de la meilleure moyenne coup à jouer
            maximum = max(result)
            # On récupère l'indice du maximum
            max_index = result.index(maximum)
            # Pour éviter de jouer dans une colonne pleine, on vérifie qu'elle
            # ne l'est pas
            while max_index >= npaGrilleCopy.shape[1] or not pq_verif_colonne(max_index, npaGrilleCopy):
                # Si c'est le cas, on va prendre le deuxième meilleur coup
                # On met le meilleur coup à -100 pour ne pas le reprendre
                result[max_index] = -100
                maximum = max(result)
                # On récupère le nouvel indice du maximum
                max_index = result.index(maximum)
            # On renvoie la colonne à jouer
            return max_index
        # Sinon on renvoit la moyenne des scores des coups joués
        return float(float(sum(result)) / float(len(result)))
    else:
        # Si on a dépassé le nombre de tours, on renvoie 0
        return 0


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
    # Si pq_victoire_ligne ou pq_victoire_colonne ou pq_victoire_diago renvoie
    # Vrai alors cette méthode renvoie true
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
    * i_nb_colonnes : Entier, Nombre de colonnes dans la grille
    * i_boucle : Entier, Compteur de boucle
    * i_debut : Entier, premier emplacement possible pour la combinaison de
            victoire dans la ligne
    * i_fin : Entier, dernier emplacement possible pour la combinaison de
            victoire dans la ligne

    **Préconditions :**
    * npa_grille initialisé
    * npa_grille contient un jeton en i_ligne, i_colonne
    * 1 <= i_joueur <= 2


    @param npa_grille: La grille du jeu
    @param i_ligne: La ligne où le jeton a été posé
    @param i_colonne: La colonne où le jeton a été posé
    @param i_joueur: Le joueur qui a joué
    @param i_nb_victoire: Le nombre de jetons nécessaire pour la victoire

    @return True si le joueur a gagné, False sinon
    """
    # On récupère la taille de la grille
    _, i_nb_colonnes = np.shape(npa_grille)

    # On calcule le premier emplacement possible pour la combinaison de
    # victoire dans la ligne
    i_debut = i_colonne - i_nb_victoire + 1 \
        if i_colonne - i_nb_victoire + 1 >= 0 else 0
    # On calcule le dernier emplacement possible pour la combinaison de
    # victoire dans la ligne
    i_fin = i_colonne + i_nb_victoire - 1 \
        if i_colonne + i_nb_victoire - 1 < i_nb_colonnes else i_nb_colonnes - 1
    # Pour chaque emplacement possible pour la combinaison de victoire dans la
    # ligne
    for i in range(i_debut, i_fin):
        # Si le jeton est celui du joueur
        if npa_grille[i_ligne][i] == i_joueur:
            # On initialise le compteur à 1
            i_compteur = 1
            # On initialise le compteur de boucle à 1
            i_boucle = 1
            # On initialise le booléen de suite à vrai
            b_suite = True
            # Tant qu'on n'a pas atteint le nombre de jetons nécessaire pour
            # gagner et qu'on est dans la grille et qu'on a une suite
            while (i_boucle < i_nb_victoire and i + i_boucle < i_nb_colonnes
                   and b_suite):
                # Si le jeton est celui du joueur
                if npa_grille[i_ligne][i + i_boucle] == i_joueur:
                    # On incrémente le compteur
                    i_compteur += 1
                # Sinon
                else:
                    # On arrête la suite
                    b_suite = False
                # On incrémente le compteur de boucle
                i_boucle += 1
            # Si le compteur est supérieur ou égal au nombre de jetons
            if i_compteur >= i_nb_victoire:
                # On retourne vrai
                return True
    # On retourne faux
    return False


def pq_victoire_colonne(npa_grille: np.array, i_ligne: int, i_colonne: int,
                        i_joueur: int, i_nb_victoire: int) -> bool:
    """! Verification de la victoire sur une colonne

    **Variables :**
    * i_compteur : Entier, Le nombre de jetons du joueur dans la ligne
    * i_nb_lignes : Entier, Nombre de lignes dans la grille
    * b_victoire : Booléen, Indique si le joueur a gagné ou non

    **Préconditions :**
    * npa_grille initialisé
    * npa_grille contient un jeton en i_ligne, i_colonne
    * 1 <= i_joueur <= 2

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
    i_nb_lignes = npa_grille.shape[0]
    # Si le nombre de lignes restantes est suffisant pour gagner
    if i_nb_lignes >= (i_nb_victoire + i_ligne):
        # On initialise le compteur à 1
        i_compteur = 1
        # Tant qu'on n'a pas atteint le nombre de jetons nécessaire pour
        # gagner et qu'on est dans la grille
        while (i_compteur < i_nb_victoire) and (
                npa_grille[i_ligne + i_compteur][i_colonne] == i_joueur):
            # On incrémente le compteur
            i_compteur += 1
        # On vérifie si le compteur est supérieur ou égal au nombre de jetons
        b_victoire = i_compteur >= i_nb_victoire
    # On retourne le booléen de victoire
    return b_victoire


def pq_victoire_diago(npa_grille: np.array, i_ligne: int, i_colonne: int,
                      i_joueur: int, i_nb_victoire: int) -> bool:
    """! Verification de la victoire sur les diagonales

    **Variables :**
    * i_compteur : Entier, Le nombre de jetons du joueur dans la ligne
    * i_nb_lignes : Entier, Nombre de lignes dans la grille
    * i_nb_colonnes : Entier, Nombre de colonnes dans la grille
    * tti_directions : Tableau de tuples d'entiers, Les directions à vérifier
    * i_dx : Entier, Composante x de la direction
    * i_dy : Entier, Composante y de la direction

    **Préconditions :**
    * npa_grille initialisé
    * npa_grille contient un jeton en i_ligne, i_colonne
    * 1 <= i_joueur <= 2

    @param npa_grille: La grille du puissance 4
    @param i_ligne: La ligne où le jeton a été posé
    @param i_colonne: La colonne où le jeton a été posé
    @param i_joueur: Le joueur qui a joué
    @param i_nb_victoire: Le nombre de jetons nécessaire pour la victoire
    @return True si le joueur i_joueur a gagné, False sinon
    """
    # Récupération de la taille de la grille
    i_nb_lignes, i_nb_colonnes = npa_grille.shape
    # Initialisation du tableau des directions à vérifier
    tti_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i_dx, i_dy in tti_directions:
        i_compteur = 0
        for d in range(-i_nb_victoire + 1, i_nb_victoire):
            x, y = i_ligne + d * i_dx, i_colonne + d * i_dy
            if 0 <= x < i_nb_lignes and 0 <= y < i_nb_colonnes and \
                    npa_grille[x][y] == i_joueur:
                i_compteur += 1
                if i_compteur >= i_nb_victoire:
                    return True
            else:
                i_compteur = 0
    return False


def pq_undo(npa_grille: np.array, t_undo_redo: list) -> np.array:
    """! Méthode permettant de revenir en arrière dans le jeu

    @param npa_grille: La grille du puissance 4
    @param t_undo_redo: La liste contenant les grilles pour l'undo et le redo
    @return La grille du puissance 4 après l'undo

    **Variables :**
    * npa : np.array, la grille du puissance 4 au coup précédent
    """
    # Si la liste contenant les grilles pour l'undo et le redo n'est pas vide
    if len(t_undo_redo) > 0:
        npa = t_undo_redo.pop()
        return npa
    else:
        print("Impossible")
    # On retourne la grille
    return npa_grille


def pq_redo(npa_grille: np.array, t_redo: list) -> np.array:
    """! Méthode permettant de revenir en avant dans le jeu

    @param npa_grille: La grille du puissance 4
    @param t_redo: La liste contenant les grilles pour l'undo et le redo
    @return La grille du puissance 4 après le redo

    **Variables :**
    * npa : np.array, la grille du puissance 4 au coup annulé
    """
    # Si la liste contenant les grilles pour l'undo et le redo n'est pas vide
    if t_redo:
        # On récupère la dernière grille
        npa = t_redo.pop()
        return npa
    # On retourne la grille
    return npa_grille


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
    * 2 <= i_nb_lignes
    * 2 <= i_nb_colonnes

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
        while i_boucle_colonne < i_nb_colonnes and b_tableau_plein:
            # Si la case est vide
            if npa_grille[i_boucle_ligne, i_boucle_colonne] == 0:
                # Le tableau n'est pas plein
                b_tableau_plein = False
            # On incrémente le compteur de colonne
            i_boucle_colonne += 1
        # On incrémente le compteur de ligne
        i_boucle_ligne += 1
    # On retourne le résultat de la négation du booléen
    return b_tableau_plein and b_bonus_utilise
