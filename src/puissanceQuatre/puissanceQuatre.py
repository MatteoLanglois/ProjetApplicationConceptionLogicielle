"""! @brief Un programme qui joue au jeu puissance 4++.

@mainpage Projet Puissance 4++

@section description_main Description
Ce programme est un jeu de puissance 4++ avec une grille de taille variable,
un nombre de pions à aligner variable, des bonus et un undo.

@section import_section Importations
Ce programme utilise les modules externes suivants :
- tkinter
- numpy

@package src.puissanceQuatre.puissanceQuatre
@brief Ce module contient l'implémentation des règles du puissance 4.
@details Ce module contient la gestion de la structure du puissance 4 et
la gestion du jeu.
"""
# Importation de numpy
import numpy as np
# Importation de la grille
from src.puissanceQuatre import grid as gr


def pq_verif_colonne(i_colonne: int, npa_grille: np.array) -> bool:
    """! Vérifie si on peut poser un jeton dans cette colonne

    @pre 0 < i_colonne ≤ npa_grille.shape[0]
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
    @pre 0 < i_colonne ≤ npa_grille.shape[0]
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


def pq_minmax(iNextJoueur, npaGrilleCopy, i_nb_victoire, iColonne=0,
              isFirst=False, tour=0) -> (int, float):
    """! Méthode implémentant l'algorithme minmax
    """
    if tour > 5:
        return 0, 0
    if not isFirst:
        if pq_verif_colonne(iColonne, npaGrilleCopy):
            i_ligne, _ = pq_ajout_piece(npaGrilleCopy, iColonne, iNextJoueur)
            if pq_victoire(npaGrilleCopy, i_ligne, iColonne, iNextJoueur,
                           i_nb_victoire):
                if iNextJoueur == 1:
                    return -1, -1
                else:
                    return 1, 1
    if iNextJoueur == 2:
        iNextJoueur = 1
    else:
        iNextJoueur = 2

    Resultat = [0] * (np.shape(npaGrilleCopy)[1])
    Moy = [0] * (np.shape(npaGrilleCopy)[1])

    for i in range(np.shape(npaGrilleCopy)[1]):
        Resultat[i], Moy[i] = pq_minmax(iNextJoueur, np.copy(npaGrilleCopy),
                                        iColonne=i, tour=tour + 1,
                                        i_nb_victoire=i_nb_victoire)
    if iNextJoueur == 2:
        return min(Resultat), sum(Resultat) / len(Resultat)
    else:
        if not isFirst:
            return max(Resultat), sum(Resultat) / len(Resultat)
        else:
            mini = min(Resultat)
            maxi = max(Resultat)
            if mini == -1:
                maxi = mini
            list_index = []
            for i in range(len(Resultat)):
                if Resultat[i] == maxi:
                    list_index.append(i)
            if len(list_index) == 1:
                return list_index[0], 0
            else:
                maxi_moy = min(Moy)
                for i in range(len(list_index)):
                    if Moy[list_index[i]] == maxi_moy and pq_verif_colonne(
                            list_index[i], npaGrilleCopy):
                        return list_index[i], 0
                return None, None


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
    * i_nb_colonnes : Entier, Nombre de colonnes dans la grille
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
    i_nb_colonnes = np.shape(npa_grille)[1]

    i_debut = i_colonne - i_nb_victoire + 1 \
        if i_colonne - i_nb_victoire + 1 >= 0 else 0
    i_fin = i_colonne + i_nb_victoire - 1 \
        if i_colonne + i_nb_victoire - 1 < i_nb_colonnes else i_nb_colonnes - 1
    for i in range(i_debut, i_fin):
        if npa_grille[i_ligne][i] == i_joueur:
            i_compteur = 1
            i_boucle = 1
            b_suite = True
            while (i_boucle < i_nb_victoire and i + i_boucle < i_nb_colonnes
                   and b_suite):
                if npa_grille[i_ligne][i + i_boucle] == i_joueur:
                    i_compteur += 1
                else:
                    b_suite = False
                i_boucle += 1
            if i_compteur >= i_nb_victoire:
                return True
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
    i_nb_lignes = npa_grille.shape[0]
    # Si le nombre de lignes restantes est suffisant pour gagner
    if i_nb_lignes >= (i_nb_victoire + i_ligne):
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
    * i_nb_lignes : Entier, Nombre de lignes dans la grille
    * i_nb_colonnes : Entier, Nombre de colonnes dans la grille

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
    i_nb_lignes, i_nb_colonnes = npa_grille.shape
    i_haut_ligne = i_ligne - i_nb_victoire + 1 \
        if i_ligne - i_nb_victoire + 1 >= 0 else 0
    i_bas_ligne = i_ligne + i_nb_victoire - 1 \
        if i_ligne + i_nb_victoire - 1 < i_nb_lignes else i_nb_lignes - 1
    i_gauche_colonne = i_colonne - i_nb_victoire + 1 \
        if i_colonne - i_nb_victoire + 1 >= 0 else 0
    i_droite_colonne = i_colonne + i_nb_victoire - 1 \
        if i_colonne + i_nb_victoire - 1 < i_nb_colonnes else i_nb_colonnes - 1
    for i in range(i_haut_ligne, i_bas_ligne):
        for j in range(i_gauche_colonne, i_droite_colonne):
            if npa_grille[i][j] == i_joueur:
                i_compteur = 1
                i_boucle = 1
                b_suite = True
                while (i_boucle < i_nb_victoire and i + i_boucle < i_nb_lignes
                       and j + i_boucle < i_nb_colonnes and b_suite):
                    if npa_grille[i + i_boucle][j + i_boucle] == i_joueur:
                        i_compteur += 1
                    else:
                        b_suite = False
                    i_boucle += 1
                if i_compteur >= i_nb_victoire:
                    return True


def pq_undo(npa_grille: np.array, t_undo_redo: list) -> np.array:
    """! Méthode permettant de revenir en arrière dans le jeu

    @param npa_grille: La grille du puissance 4
    @param t_undo_redo: La liste contenant les grilles pour l'undo et le redo
    @return La grille du puissance 4 après l'undo
    """
    # Si la liste contenant les grilles pour l'undo et le redo n'est pas vide
    if t_undo_redo:
        # On récupère la dernière grille
        if len(t_undo_redo) == 1:
            print("Recommence et fait pas chier")
        else:
            npa = t_undo_redo.pop()
            npa = t_undo_redo.pop()
            return npa
    # On retourne la grille
    return npa_grille


def pq_redo(npa_grille: np.array, t_redo: list) -> np.array:
    """! Méthode permettant de revenir en avant dans le jeu

    @param npa_grille: La grille du puissance 4
    @param t_redo: La liste contenant les grilles pour l'undo et le redo
    @return La grille du puissance 4 après le redo
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
    t_redo = []
    # Initialisation de la grille de jeu
    npa_grille = gr.pq_init_grille(i_nb_lignes, i_nb_colonnes)
    # Initialisation de la colonne où le joueur veut jouer
    i_colonne_joueur = 0
    # Initialisation de la ligne où le joueur veut jouer
    i_ligne_joueur = 0
    b_is_play = False

    # Affichage des règles du jeu
    print("Bienvenue dans le puissance 4 !\n"
          "Pour jouer, entrez le numéro de la colonne où vous voulez jouer.\n"
          "Vos jetons sont représentés par des X, ceux du bot par des 0.\n"
          "Pour utiliser votre bonus, entrez 0. (WIP)\n")

    # Tant que la partie n'est pas finie et qu'il n'y a pas de victoire
    while not pq_partie_finie(npa_grille, b_bonus_utilise) and not b_victoire:
        # Initialisation de la colonne où le joueur veut jouer à -1 afin de
        # pouvoir vérifier que la colonne est valide
        i_colonne_joueur = -4
        # Affichage de la grille
        gr.pq_print_grille(npa_grille)
        # Tant que la colonne n'est pas valide
        t_redo = []
        while (not (0 <= i_colonne_joueur < i_nb_colonnes)
               and pq_verif_colonne(i_colonne_joueur, npa_grille)):
            # Demande de la colonne où le joueur veut jouer
            b_is_play = False
            i_colonne_joueur = int(input("\nDans quelle colonne voulez vous "
                                         "jouer ? ")) - 1
            if i_colonne_joueur == -1:
                print("Utilisation du bonus !")

            elif i_colonne_joueur == -2:
                t_redo.append(np.copy(npa_grille))
                npa_grille = pq_undo(npa_grille, t_undo_redo)
                print("Undo !")
                gr.pq_print_grille(npa_grille)
                t_undo_redo.append(npa_grille)

            elif i_colonne_joueur == -3:
                t_undo_redo.append(np.copy(npa_grille))
                npa_grille = pq_redo(npa_grille, t_redo)
                print("Redo !")
                gr.pq_print_grille(npa_grille)

            else:
                b_is_play = True
        # Pose du jeton et récupération de la ligne où le jeton a été posé
        if b_is_play:
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

        if not b_victoire and not pq_partie_finie(npa_grille, b_bonus_utilise):
            # Choix de la colonne où le bot va jouer (random pour commencer)
            i_colonne_joueur, _ = pq_minmax(2, np.copy(npa_grille),
                                            i_nb_jeton_victoire, isFirst=True,
                                            tour=0)
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
        t_undo_redo.append(np.copy(npa_grille))
    # Fin de partie
    return


# Si on exécute ce fichier
if __name__ == '__main__':
    # Lance une partie normale en ligne de commande
    pq_gestion_partie(6, 7, 4)
