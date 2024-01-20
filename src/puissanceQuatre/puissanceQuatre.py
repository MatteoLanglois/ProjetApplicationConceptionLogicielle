"""! @brief Un programme qui joue au jeu puissance 4++.

Ce programme est un jeu de puissance 4++ avec une grille de taille variable,
un nombre de pions à aligner variable, des bonus et un undo.

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
# Importation des bonus
from src.utils import bonus_utils as bu
from src.puissanceQuatre import grid as gr


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


def pq_find_hole(i_colonne: int, npa_grille: np.array) -> int:
    """! Trouve la première case vide dans une colonne

    Cette fonction permet de trouver la première case vide dans une colonne
    donnée. Elle vérifie si la colonne est valide et si elle n'est pas pleine.
    Elle renvoie un entier indiquant la première case vide dans cette colonne.

    **Variables :**
    * i_max_ligne **Entier** : Nombre de lignes dans la grille
    * i_boucle **Entier** : Compteur de boucle

    @pre 0 < i_colonne <= npa_grille.shape[0]
    @pre npa_grille initialisé
    @param i_colonne: La colonne où on souhaite poser un jeton
    @param npa_grille: La grille de jeu
    """
    # Si on peut jouer dans la colonne
    if pq_verif_colonne(i_colonne, npa_grille):
        # Récupération de la taille de la grille
        i_max_ligne, _ = npa_grille.shape
        # Pour chaque ligne de la grille
        for i_boucle in range(i_max_ligne - 1, 0, -1):
            # Si la case est vide
            if npa_grille[i_boucle][i_colonne] == 0:
                # On retourne la ligne
                return i_boucle


def pq_ajout_piece(npa_grille: np.array, i_colonne: int,
                   i_joueur: int) -> (int, int):
    """! La méthode qui gère le placement de jetons

    Cette méthode permet d'ajouter une pièce dans la colonne indiquée. Elle
    vérifie si la colonne est valide et si elle n'est pas pleine. Elle renvoie
    les coordonnées du nouveau jeton.

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
    * i_line **Entier** : Compteur de boucle
    * i_max_ligne **Entier** : Nombre de lignes dans la grille
    * ti_coords **Tuple d'entiers** : Coordonnées du nouveau jeton
    """
    # Initialise le compteur de boucle
    i_line = 0
    # Récupère la taille de la grille
    i_max_ligne, _ = npa_grille.shape
    # Initialisation des coordonnées du nouveau jeton
    ti_coords = (None, None)

    # Si on peut jouer dans la colonne
    if pq_verif_colonne(i_colonne, npa_grille):
        # On récupère la première case vide dans la colonne
        i_line = pq_find_hole(i_colonne, npa_grille)
        # Ajouter le jeton du joueur dans la dernière case vide
        npa_grille[i_line][i_colonne] = i_joueur
        # Retourner un tuple des coordonnées du nouveau jeton
        ti_coords = (i_line, i_colonne)
    # Retourner les coordonnées du nouveau jeton
    return ti_coords


def pq_minmax(i_joueur, npa_grille_copy, i_nb_victoire, s_bonus, b_bonus_used,
              i_colonne=0,
              b_is_first=False, i_tour=0, b_is_the_bonus=False) -> float:
    """! Méthode implémentant l'algorithme minmax

    Cette méthode permet de jouer un coup en utilisant l'algorithme minmax.
    Elle prend en paramètre le joueur qui joue, la grille de jeu, le nombre de
    jetons à aligner pour gagner, le bonus à jouer, un booléen indiquant si le
    bonus a déjà été joué, la colonne où jouer le bonus, un booléen indiquant
    si c'est le premier appel de la méthode, le nombre de tours effectués et un
    booléen indiquant si le bonus est utilisé ou non.

    **Variables :**
    * m_module : Module, Le module du bonus
    * f_bonus : Fonction, La fonction du bonus
    * tf_result : Liste, La liste contenant les résultats
    * i_maximum : Entier, Le i_maximum de la liste
    * i_max_index : Entier, L'indice du i_maximum de la liste
    * ligne : Entier, La ligne où le jeton a été posé

    @pre npa_grille initialisé
    @pre 1 <= i_joueur <= 2
    @pre 0 <= i_colonne <= npa_grille.shape[0]

    @param i_joueur: Le joueur qui joue (1 pour le joueur, 2 pour le bot)
    @param npa_grille_copy: La grille du puissance 4
    @param i_nb_victoire: Le nombre de jetons à aligner pour gagner
    @param s_bonus: Le bonus à jouer
    @param b_bonus_used: Un booléen indiquant si le bonus a déjà été joué
    @param i_colonne: La colonne où jouer le bonus
    @param b_is_first: Un booléen indiquant si c'est le premier appel de la
    méthode
    @param i_tour: Le nombre de tours effectués
    @param b_is_the_bonus: Un booléen indiquant si le bonus est utilisé ou non

    @return La colonne où jouer le jeton
    """
    # Pour éviter de faire trop de calculs, on limite le nombre de tours à 5
    if i_tour < 2:
        # Si le joueur est le joueur humain
        if i_joueur == 1:
            # Si on joue un bonus
            if i_colonne == -1:
                # On importe le module du bonus
                m_module = __import__("src.puissanceQuatre.bonus",
                                      fromlist=["bonus"])
                # On récupère la fonction du bonus
                f_bonus = getattr(m_module, bu.bu_unformat_bonus_name(s_bonus))
                # On applique le bonus à la grille
                npa_grille_copy = f_bonus(npa_grille_copy.copy())
                # On indique que le bonus a été utilisé
                b_bonus_used = True
            # Sinon
            else:
                if pq_verif_colonne(i_colonne, npa_grille_copy):
                    # On joue le jeton dans la colonne
                    i_ligne, _ = pq_ajout_piece(npa_grille_copy, i_colonne,
                                                i_joueur)
                    # Si on peut bien poser un jeton dans la ligne
                    if i_ligne is not None:
                        # Si le joueur a gagné
                        if pq_victoire(npa_grille_copy, i_ligne, i_colonne, i_joueur,
                                       i_nb_victoire):
                            # On retourne -10 si b_is_the_bonus, 10 sinon
                            return -10 if b_is_the_bonus else 10
                    return -10
            # Si la partie est finie
            if pq_partie_finie(npa_grille_copy, False):
                # On retourne 0, indiquant un chemin neutre
                return 0
        # Sinon si c'est à l'ordinateur de jouer, et qu'il ne s'agit pas du
        # premier appel
        elif i_joueur == 2 and not b_is_first:
            if pq_verif_colonne(i_colonne, npa_grille_copy):
                # On joue le jeton dans la colonne
                i_ligne, _ = pq_ajout_piece(npa_grille_copy, i_colonne, i_joueur)
                # Si l'ordinateur a gagné
                if pq_victoire(npa_grille_copy, i_ligne, i_colonne, i_joueur,
                               i_nb_victoire):
                    # On retourne -10
                    if b_is_the_bonus:
                        return 10
                    else:
                        return -10
            # Si la partie est finie
            elif pq_partie_finie(npa_grille_copy, False):
                # On retourne 0, indiquant un chemin neutre
                return 0
        # On change de joueur
        if i_joueur == 1:
            i_joueur = 2
        else:
            i_joueur = 1
        # On crée la liste qui contiendra les résultats
        tf_result = []
        # Pour chaque colonne de la grille
        for i in range(npa_grille_copy.shape[1]):
            # Si on peut jouer dans la colonne
            if pq_verif_colonne(i, npa_grille_copy):
                # On ajoute le résultat de l'appel récursif dans la liste (la
                # moyenne des coups joués)
                tf_result.append(
                    pq_minmax(i_joueur, npa_grille_copy.copy(), i_nb_victoire,
                              s_bonus, b_bonus_used, i,
                              False, i_tour + 1))
            else:
                # Si on ne peut pas jouer dans la colonne, on renvoie -1
                # (cela évite mieux ces colonnes)
                tf_result.append(-1)
        # Si le bonus n'a pas encore été joué
        if not b_bonus_used and i_joueur == 1:
            # On enregistre aussi l'appel qui joue le bonus
            tf_result.append(
                pq_minmax(i_joueur, npa_grille_copy.copy(), i_nb_victoire,
                          s_bonus, False, -1, False, i_tour + 1))
        # Si c'est le premier appel
        if i_joueur == 1 and b_is_first:
            # On retourne l'indice de la meilleure moyenne coup à jouer
            i_maximum = max(tf_result)
            # On récupère l'indice du maximum
            i_max_index = tf_result.index(i_maximum)
            # Pour éviter de jouer dans une colonne pleine, on vérifie qu'elle
            # ne l'est pas
            while (i_max_index >= npa_grille_copy.shape[1]
                   or not pq_verif_colonne(i_max_index, npa_grille_copy)):
                # Si c'est le cas, on va prendre le deuxième meilleur coup
                # On met le meilleur coup à -100 pour ne pas le reprendre
                tf_result[i_max_index] = -100
                i_maximum = max(tf_result)
                # On récupère le nouvel indice du i_maximum
                i_max_index = tf_result.index(i_maximum)
            # On renvoie la colonne à jouer
            return i_max_index
        # Sinon on renvoie la moyenne des scores des coups joués
        return float(float(sum(tf_result)) / float(len(tf_result)))
    else:
        # Si on a dépassé le nombre de tours, on renvoie 0
        return 0


def pq_victoire(npa_grille: np.array, i_ligne: int, i_colonne: int,
                i_joueur: int, i_nb_victoire: int) -> bool:
    """: Méthode appelant les trois vérifications de victoire.

    Cette méthode permet de vérifier si le joueur a gagné ou non. Elle prend en
    paramètre la grille de jeu, la ligne et la colonne où le jeton a été posé,
    le joueur qui a joué et le nombre de jetons à aligner pour gagner. Elle
    renvoie un booléen indiquant si le joueur a gagné ou non.

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

    Cette méthode permet de vérifier si le joueur a gagné sur la ligne où il a
    joué. Elle prend en paramètre la grille de jeu, la ligne et la colonne où
    le jeton a été posé, le joueur qui a joué et le nombre de jetons à aligner
    pour gagner. Elle renvoie un booléen indiquant si le joueur a gagné ou non.

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

    Cette méthode permet de vérifier si le joueur a gagné sur la colonne où il
    a joué. Elle prend en paramètre la grille de jeu, la ligne et la colonne où
    le jeton a été posé, le joueur qui a joué et le nombre de jetons à aligner
    pour gagner. Elle renvoie un booléen indiquant si le joueur a gagné ou non.

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

    Cette méthode permet de vérifier si le joueur a gagné sur les diagonales où
    il a joué. Elle prend en paramètre la grille de jeu, la ligne et la colonne
    où le jeton a été posé, le joueur qui a joué et le nombre de jetons à
    aligner pour gagner. Elle renvoie un booléen indiquant si le joueur a gagné
    ou non.

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

    # Pour chaque direction à vérifier
    for i_dx, i_dy in tti_directions:
        i_compteur = 0
        # Pour chaque position dans la plage de victoire
        for d in range(-i_nb_victoire + 1, i_nb_victoire):
            x, y = i_ligne + d * i_dx, i_colonne + d * i_dy
            # Si la position est dans la grille et contient le jeton du joueur
            if 0 <= x < i_nb_lignes and 0 <= y < i_nb_colonnes and \
                    npa_grille[x][y] == i_joueur:
                # Incrémente le compteur
                i_compteur += 1
                # Si le compteur atteint le nombre de jetons
                # nécessaire pour la victoire
                if i_compteur >= i_nb_victoire:
                    # Retourne True (le joueur a gagné)
                    return True
            else:
                # Réinitialise le compteur
                i_compteur = 0
    # Si aucune victoire n'a été trouvée, retourne False
    return False


def pq_undo(npa_grille: np.array, t_undo_redo: list) -> np.array:
    """! Méthode permettant de revenir en arrière dans le jeu

    Cette méthode permet de revenir en arrière dans le jeu. Elle prend en
    paramètre la grille du puissance 4 et la liste contenant les grilles pour
    l'undo et le redo. Elle renvoie la grille du puissance 4 après l'undo.

    @param npa_grille: La grille du puissance 4
    @param t_undo_redo: La liste contenant les grilles pour l'undo et le redo
    @return La grille du puissance 4 après l'undo

    **Variables :**
    * npa_grille : np.array, la grille du puissance 4 au coup précédent
    """
    # Si la liste contenant les grilles pour l'undo et le redo n'est pas vide
    if len(t_undo_redo) > 0:
        # On récupère la dernière grille
        npa_grille = t_undo_redo.pop()
        # On retourne la grille
        return npa_grille
    # On retourne la grille
    return npa_grille


def pq_redo(npa_grille: np.array, t_redo: list) -> np.array:
    """! Méthode permettant de revenir en avant dans le jeu

    Cette méthode permet de revenir en avant dans le jeu. Elle prend en
    paramètre la grille du puissance 4 et la liste contenant les grilles pour
    l'undo et le redo. Elle renvoie la grille du puissance 4 après le redo.

    @param npa_grille: La grille du puissance 4
    @param t_redo: La liste contenant les grilles pour l'undo et le redo
    @return La grille du puissance 4 après le redo

    **Variables :**
    * npa_grille : np.array, la grille du puissance 4 au coup annulé
    """
    # Si la liste contenant les grilles pour l'undo et le redo n'est pas vide
    if t_redo:
        # On récupère la dernière grille
        npa_grille = t_redo.pop()
        # On retourne la grille
        return npa_grille
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
