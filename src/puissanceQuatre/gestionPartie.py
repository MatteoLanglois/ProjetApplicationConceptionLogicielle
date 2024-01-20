"""! @brief Un programme qui joue au jeu puissance 4++.

Ce programme est un jeu de puissance 4++ avec une grille de taille variable,
un nombre de pions à aligner variable, des bonus et un undo.

Ce programme utilise les modules externes suivants :
- tkinter
- numpy
- inspect

@package src.puissanceQuatre.gestionPartie
@brief Un module qui gère la partie de puissance 4 en ligne de commande
@details Ce module contient les fonctions permettant de gérer la partie en ligne
de commande.
"""
from src.puissanceQuatre import grid as gr
from src.puissanceQuatre import puissanceQuatre as pq
from src.utils import bonus_utils as bu
import numpy as np

global T_UNDO_REDO
global T_REDO
global B_BONUS_USED


def gp_choose_bonus():
    """! Récupère le bonus choisi par le joueur

    Cette fonction permet de récupérer le bonus que le joueur a choisi avant le
    début de la partie. Elle renvoie le bonus choisi.

    @return Le bonus choisi par le joueur

    **Variables :**
    * ts_bonuses : Liste, contient les fonctions des bonus
    * i_bonus : Entier, le bonus choisi par le joueur
    """
    ts_bonuses = bu.bu_get_bonuses()
    print("Choisissez votre bonus :")
    for i in range(len(ts_bonuses)):
        print(f"{i + 1}. "
              f"{bu.bu_format_bonus_name(bu.bu_get_bonus_name(ts_bonuses[i]))}")
    i_bonus = int(input("Votre choix : ")) - 1
    return ts_bonuses[i_bonus]


def gp_show_rules():
    """! Affiche les règles du jeu

    Cette fonction permet d'afficher les règles dans la console python.
    """
    # Affichage des règles du jeu
    print("Bienvenue dans le puissance 4 !\n"
          "Pour jouer, entrez le numéro de la colonne où vous voulez jouer.\n"
          "Vos jetons sont représentés par des X, ceux du bot par des 0.\n"
          "Pour utiliser votre bonus, entrez bonus. (WIP)\n"
          "Pour annuler votre dernier coup, entrez undo.\n"
          "Pour refaire votre dernier coup, entrez redo.\n"
          "Pour revoir les règles, entrez rules.\n")


def gp_get_player_choice(i_nb_colonnes: int, npa_grille: np.array) -> str:
    """! Récupère le choix du joueur lors de son tour

    Cette fonction permet de récupérer le choix du joueur lors de son tour. Elle
    renvoie le choix du joueur.

    @param i_nb_colonnes: Nombre de colonnes de la grille
    @param npa_grille: Grille de jeu
    @pre i_nb_colonnes > 0
    @pre npa_grille initialisé
    @return Le choix du joueur
    @post Le choix du joueur récupéré

    **Variables :**
    * i_colonne_joueur : Entier, la colonne où le joueur veut jouer
    * s_colonne_joueur : Chaine de caractères, le choix du joueur
    """
    # Initialisation de la colonne où le joueur veut jouer à -1 afin de
    # pouvoir vérifier que la colonne est valide
    i_colonne_joueur = -1
    # Tant que la colonne n'est pas valide
    s_colonne_joueur = input("Voulez vous jouer une action ? \nVous avez le "
                             "choix entre le bonus, undo, redo et rules. \n"
                             "Sinon appuyez sur entrée pour poser un jeton : ")
    # Tant que la colonne n'est pas valide ou que le joueur n'a pas choisi
    # une action
    if not s_colonne_joueur or not (s_colonne_joueur != "bonus"
                                    and s_colonne_joueur != "undo"
                                    and s_colonne_joueur != "redo"
                                    and s_colonne_joueur != "rules"):
        # Tant que la colonne n'est pas valide
        while (not (0 <= i_colonne_joueur < i_nb_colonnes)
               and pq.pq_verif_colonne(i_colonne_joueur, npa_grille)):
            # Récupération de la colonne où le joueur veut jouer
            i_colonne_joueur = int(input("\nDans quelle colonne voulez vous "
                                         "jouer ? ")) - 1
        # Conversion de la colonne en chaine de caractères
        s_colonne_joueur = str(i_colonne_joueur)
    # Retour de la colonne où le joueur veut jouer
    return s_colonne_joueur


def gp_handle_undo_redo(b_undo: bool, npa_grille: np.array) -> np.array:
    """! Méthode permettant au joueur d'annuler ou de refaire son dernier coup

    Cette fonction permet au joueur d'annuler ou de refaire son dernier coup.

    @param b_undo: Booléen indiquant si c'est un undo ou un redo (True pour
        undo, False pour redo)
    @param npa_grille: np.array, La grille de jeu
    @return: np.array, La grille de jeu modifiée
    """
    global T_UNDO_REDO, T_REDO
    # Si c'est un undo
    if b_undo:
        # On ajoute la grille actuelle à la liste pour le redo
        T_REDO.append(np.copy(npa_grille))
        # On récupère la grille précédente
        npa_grille = pq.pq_undo(npa_grille, T_UNDO_REDO)
        # On affiche undo
        print("Undo !")
        # On affiche la grille
        gr.gr_print_grille(npa_grille)
        # On ajoute la grille actuelle à la liste pour l'undo
        T_UNDO_REDO.append(npa_grille)
    # Sinon
    else:
        # On ajoute la grille actuelle à la liste pour l'undo
        T_UNDO_REDO.append(np.copy(npa_grille))
        # On récupère la grille suivante
        npa_grille = pq.pq_redo(npa_grille, T_REDO)
        # On affiche redo
        print("Redo !")
        # On affiche la grille
        gr.gr_print_grille(npa_grille)
    # On retourne la grille
    return npa_grille


def gp_use_bonus(s_bonus: str, npa_grille: np.array):
    """! Méthode permettant au joueur d'utiliser son bonus

    Cette fonction permet au joueur d'utiliser son bonus. Elle renvoie la grille
    modifiée.

    @param s_bonus: str, le nom du bonus
    @param npa_grille: np.array, la grille de jeu
    @return: np.array, la grille de jeu modifiée
    """
    global B_BONUS_USED
    # On passe le booléen de bonus utilisé à vrai
    B_BONUS_USED = True
    # On affiche l'utilisation du bonus
    print("Utilisation du bonus !")
    # On importe le module du bonus
    m_module = __import__("src.puissanceQuatre.bonus",
                          fromlist=["bonus"])
    # On récupère la fonction du bonus
    f_bonus = getattr(m_module, bu.bu_unformat_bonus_name(s_bonus[0]))
    # On applique le bonus à la grille
    npa_grille = f_bonus(npa_grille.copy())
    # On retourne la grille modifiée
    return npa_grille


def gp_handle_player_turn(npa_grille: np.array, s_bonus: str):
    """! Méthode permettant de gérer le tour du joueur

    Cette fonction permet de gérer le tour du joueur. Elle renvoie la grille
    modifiée.

    @param npa_grille: np.array, la grille de jeu
    @param s_bonus: str, le nom du bonus
    @return: np.array, la grille de jeu modifiée

    **Variables :**
    * npa_grille : np.array, la grille de jeu
    * s_bonus : str, le nom du bonus choisi par le joueur
    """
    # Récupération de l'action du joueur
    s_colonne_joueur = gp_get_player_choice(npa_grille.shape[1], npa_grille)
    # Si le joueur a choisi l'action bonus
    if s_colonne_joueur == "bonus":
        # On utilise le bonus
        npa_grille = gp_use_bonus(s_bonus[0], npa_grille)
    # Si le joueur a choisi l'action undo
    elif s_colonne_joueur == "undo":
        # On annule son dernier coup
        gp_handle_undo_redo(True, npa_grille)
    # Si le joueur a choisi l'action redo
    elif s_colonne_joueur == "redo":
        # On refait son dernier coup
        gp_handle_undo_redo(False, npa_grille)
    # Si le joueur a choisi l'action rules
    elif s_colonne_joueur == "rules":
        # On affiche les règles
        gp_show_rules()
    # Sinon
    else:
        # Conversion de la colonne en entier
        i_colonne_joueur = int(s_colonne_joueur)
        # Pose du jeton et récupération de la ligne où le jeton a été posé
        i_ligne_joueur, _ = pq.pq_ajout_piece(npa_grille,
                                              i_colonne_joueur, 1)
    # On retourne la grille
    return npa_grille


def gp_handle_bot_turn(npa_grille: np.array, s_bonus: str,
                       i_nb_jeton_victoire: int):
    """! Méthode permettant de gérer le tour du bot

    Cette fonction permet de gérer le tour du bot. Elle renvoie la grille
    modifiée.

    @param npa_grille: np.array, la grille de jeu
    @param s_bonus: str, le nom du bonus
    @param i_nb_jeton_victoire: int, le nombre de jetons à aligner pour gagner

    **Variables :**
    * npa_grille : np.array, la grille de jeu
    * s_bonus : str, le nom du bonus choisi par le joueur
    * i_colonne_joueur : Entier, la colonne où le joueur veut jouer
    * i_ligne_joueur : Entier, la ligne où le joueur veut jouer
    """
    # Choix de la colonne où le bot va jouer
    i_colonne_joueur = int(pq.pq_minmax(i_joueur=1,
                                        npa_grille_copy=npa_grille.copy(),
                                        i_nb_victoire=i_nb_jeton_victoire,
                                        b_is_first=True,
                                        i_tour=0,
                                        s_bonus=s_bonus,
                                        b_bonus_used=B_BONUS_USED))
    # Pose du jeton et récupération de la ligne où le jeton a été posé
    i_ligne_joueur, _ = pq.pq_ajout_piece(npa_grille, i_colonne_joueur,
                                          2)
    return npa_grille


def gp_handle_victory(npa_grille: np.array, i_ligne_joueur: int, i_joueur: int,
                      i_colonne_joueur: int, i_nb_jeton_victoire: int):
    """! Méthode permettant de gérer la victoire d'un joueur

    Cette fonction permet de gérer la victoire d'un joueur. Elle renvoie un
    booléen indiquant si un joueur a gagné ou non.

    @param npa_grille: np.array, la grille de jeu
    @param i_ligne_joueur: Entier, la ligne où le joueur veut jouer
    @param i_joueur: Entier, le numéro du joueur
    @param i_colonne_joueur: Entier, la colonne où le joueur veut jouer
    @param i_nb_jeton_victoire: Entier, le nombre de jetons à aligner pour
        gagner
    @return: Booléen, True si un joueur a gagné, False sinon

    **Variables :**
    * b_victoire : Booléen, True si un joueur a gagné, False sinon
    """
    b_victoire = False
    if (pq.pq_victoire(npa_grille, i_ligne_joueur, i_colonne_joueur,
                       i_joueur, i_nb_jeton_victoire)):
        # Affichage de la grille
        gr.gr_print_grille(npa_grille)
        # Affichage du message de victoire
        print(f"Le joueur {i_joueur} a gagné !")
        # Passage du booléen de victoire à vrai
        b_victoire = True
    return b_victoire


def gp_gestion_partie(i_nb_lignes: int = 6, i_nb_colonnes: int = 7,
                      i_nb_jeton_victoire: int = 4):
    """! Gère le déroulement d'une partie de puissance 4

    Cette fonction gère l'entièreté du déroulement d'une partie de puissance 4.
    Elle prend en paramètre la taille de la grille en lignes, la taille de la
    grille en colonnes et le nombre de jetons à aligner pour gagner.

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
    global T_UNDO_REDO, T_REDO, B_BONUS_USED
    # Initialisation d'un booléen pour savoir s'il y a une victoire
    b_victoire = False
    # Initialisation d'un booléen pour savoir si le joueur a utilisé son bonus
    B_BONUS_USED = False
    # Initialisation d'une liste pour l'undo et le redo
    T_UNDO_REDO = []
    T_REDO = []
    # Initialisation de la grille de jeu
    npa_grille = gr.gr_init_grille(i_nb_lignes, i_nb_colonnes)
    # Initialisation de la colonne où le joueur veut jouer
    i_colonne_joueur = 0
    # Initialisation de la ligne où le joueur veut jouer
    i_ligne_joueur = 0
    # Appel de la fonction de choix du bonus
    s_bonus = gp_choose_bonus()
    # Affichage des règles du jeu
    gp_show_rules()

    # Tant que la partie n'est pas finie et qu'il n'y a pas de victoire
    while not pq.pq_partie_finie(npa_grille,
                                 B_BONUS_USED) and not b_victoire:
        # Affichage de la grille
        gr.gr_print_grille(npa_grille)
        # Tant que la colonne n'est pas valide
        T_REDO = []

        npa_grille = gp_handle_player_turn(npa_grille, s_bonus[0])

        # Si le joueur a gagné
        b_victoire = gp_handle_victory(npa_grille, i_ligne_joueur,
                                       1, i_colonne_joueur,
                                       i_nb_jeton_victoire)
        if not b_victoire and not pq.pq_partie_finie(npa_grille, B_BONUS_USED):
            npa_grille = gp_handle_bot_turn(npa_grille, s_bonus[0],
                                            i_nb_jeton_victoire)
            # Si le bot a gagné
            b_victoire = gp_handle_victory(npa_grille, i_ligne_joueur, 2,
                                           i_colonne_joueur,
                                           i_nb_jeton_victoire)
        # Ajout de la grille à la liste pour l'undo et le redo
        T_UNDO_REDO.append(np.copy(npa_grille))
    # Fin de partie
    return


def gp_start_game():
    """! Lance une partie normale en ligne de commande

    Cette fonction démarre une partie de puissance 4 dans la console
    python.

    Cette fonction lance une partie normale en ligne de commande avec une grille
    de 6 lignes, 7 colonnes et 4 jetons à aligner pour gagner.
    """
    gp_gestion_partie(6, 7, 4)


# Si on exécute ce fichier
if __name__ == '__main__':
    # Lance une partie normale en ligne de commande
    gp_gestion_partie(6, 7, 4)
