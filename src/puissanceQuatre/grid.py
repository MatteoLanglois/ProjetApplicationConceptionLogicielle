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

@package src.puissanceQuatre.grid
@brief Ce module contient les fonctions relatives à la grille de jeu.
@details Ce module contient les fonctions de gestion de la grille de jeu.
Notamment l'initialisation de la grille, l'affichage de la grille et la
réinitialisation de la grille.
"""
import numpy as np


def pq_init_grille(i_max_ligne: int, i_max_colonne: int) -> np.array:
    """! L'initiateur de la grille

    @pre i_max_ligne > 1 et i_max_colonne > 1
    @param i_max_ligne: Le nombre de lignes de la grille
    @param i_max_colonne: Le nombre de colonnes de la grille
    @post npa_grille initialisé
    @return La grille créée

    **Variables :**
    * npa_grille : np.array
    """
    assert i_max_ligne > 1 and i_max_colonne > 1, \
        "La grille doit avoir au moins 2 lignes et 2 colonnes"
    # Création de la grille
    npa_grille = np.zeros((i_max_ligne, i_max_colonne))
    # Changement du type contenu dans la grille par "int"
    npa_grille.astype(int)
    # Retourne la grille
    return npa_grille


def pq_reset_grille(npa_grille: np.array) -> np.array:
    """! Réinitialise la grille

    **Variables :**
    * i_boucle : Entier
    * i_max_ligne : Entier
    * i_max_colonne : Entier

    @pre npa_grille initialisé
    @param npa_grille: La grille à réinitialiser
    @post npa_grille contient des 0

    @return La grille réinitialisée
    """
    # Récupération de la taille de la grille
    i_max_ligne, i_max_colonne = npa_grille.shape
    # Pour chaque ligne de la grille
    for i_boucle in range(i_max_ligne):
        # Pour chaque colonne de la grille
        for i_boucle_2 in range(i_max_colonne):
            # La case devient vide
            npa_grille[i_boucle][i_boucle_2] = 0
    # Retourne la grille
    return npa_grille


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
                print(f"|\033[91m{char_joueur}\033[00m", end="")
            elif npa_grille[i_boucle_ligne, i_boucle_colonne] == 2:
                # Affiche charBot si le joueur est le bot
                print(f"|\033[93m{char_bot}\033[00m", end="")
            else:
                # Affiche charVide si la case est vide
                print(f"|\033[00m{char_vide}\033[00m", end="")
        # Retourne à la ligne et affiche la barre de séparation des lignes
        print("|\n" + (2 * i_max_colonne + 1) * "-")


def pq_apply_gravity(npa_grille: np.array) -> np.array:
    """! Applique la gravité sur la grille, cela permet de faire tomber les
    jetons dans la grille.

    @pre npa_grille initialisé
    @param npa_grille: La grille à modifier
    @post npa_grille contient des 0 et des 1 ou 2
    @post il n'y a pas de 0 sous un 1 ou un 2

    **Variables :**
    * i_nb_ligne : Nombre de lignes de la grille
    * i_nb_colonne : Nombre de colonnes de la grille
    * i_boucle_colonne : Compteur de boucle pour les colonnes de la grille
    * i_boucle_ligne : Compteur de boucle pour les lignes de la grille
    * i_boucle_ligne_2 : Compteur de boucle pour les lignes de la grille

    """
    #On définit le nombre de ligne et de colonne de la grille
    i_nb_ligne, i_nb_colonne = npa_grille.shape
    #Pour chaque colonne de la grille
    for i in range(i_nb_colonne):
        #On initialise le compteur de sécurité à 0
        compt = 0
        #Tant que la première ligne de la colonne est vide et que le compteur est inférieur au nombre de ligne - 1
        while npa_grille[i_nb_ligne-1][i] == 0 and compt < i_nb_ligne -1:
            #Pour chaque ligne de la colonne
            for j in range(i_nb_ligne-1,0, -1):
                #On décale la ligne d'un cran vers le bas
                npa_grille[j][i] = npa_grille[j - 1][i]
                #On remplit la ligne copié de la colonne avec un 0
                npa_grille[j-1][i] = 0
            #On incrémente le compteur de sécurité
            compt += 1
    #On retourne la grille
    return npa_grille
