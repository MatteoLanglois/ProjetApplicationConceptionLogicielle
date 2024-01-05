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

@package src.controller.ctrl_pageParametres
@brief Un module qui gère la page des paramètres
@details Contient les fonctions permettant de gérer la page des paramètres
"""
# Importation de tkinter
import tkinter as tk
# Importation d'un module permettant de vérifier si deux couleurs sont trop
# proches
from src.utils.colors_utils import ctrl_page_parameter_colors_too_close
# Importation de la vue de la page des paramètres
from src.view import view_pageParametres as view_pp
# Importation du controller de la page d'accueil afin d'initialiser la fenêtre
from src.controller import ctrl_main as ctrl_m

# Variables globales ##########################
# Fenêtre principale
global TK_ROOT


def ctrl_page_parameter_init(tk_win_root: tk.Tk):
    """! Initialise la page des paramètres

    @pre tk_root initialisé
    @param tk_win_root: Fenêtre principale
    @post page des paramètres initialisée

    **Variables :**
    * tk_root : Fenêtre principale
    * i_rows : Nombre de lignes de la grille
    * i_columns : Nombre de colonnes de la grille
    * i_nb_jetons : Nombre de jetons à aligner pour gagner
    * i_difficulty : Difficulté du bot
    * st_color_joueur : Couleur des jetons du joueur
    * st_color_bot : Couleur des jetons du bot
    * st_color_grid : Couleur de la grille
    """
    global TK_ROOT
    # Enregistrement de manière globale de la fenêtre principale
    TK_ROOT = tk_win_root
    # Initialisation de la page des paramètres
    view_pp.vpp_init(TK_ROOT)

    # Chargement des paramètres sauvegardés
    i_rows, i_columns, i_nb_jetons, i_difficulty = (
        ctrl_page_parameter_settings_load())
    # Affichage du nombre de lignes enregistré
    view_pp.vpp_set_nb_rows(i_rows)
    # Affichage du nombre de colonnes enregistré
    view_pp.vpp_set_nb_columns(i_columns)
    # Affichage du nombre de jetons à aligner enregistré
    view_pp.vpp_set_nb_jetons(i_nb_jetons)
    # Affichage de la difficulté enregistrée
    view_pp.vpp_set_difficulty(i_difficulty)

    # Chargement des paramètres de personnalisation sauvegardés
    st_color_joueur, st_color_bot, st_color_grid = (
        ctrl_page_parameter_custom_load())
    # Affichage de la couleur des jetons du joueur enregistrée
    view_pp.vpp_set_joueur_color(st_color_joueur)
    # Affichage de la couleur des jetons du bot enregistrée
    view_pp.vpp_set_bot_color(st_color_bot)
    # Affichage de la couleur de la grille enregistrée
    view_pp.vpp_set_grid_color(st_color_grid)


def ctrl_page_parameter_settings_save():
    """! Sauvegarde les paramètres

    @pre tk_root initialisé
    @pre res/settings.txt existant
    @post paramètres sauvegardés ou str_message d'erreur affiché

    **Variables :**
    * i_rows : Nombre de lignes de la grille
    * i_columns : Nombre de colonnes de la grille
    * i_nb_jetons : Nombre de jetons à aligner pour gagner
    * i_difficulty : Difficulté du bot
    * str_message : Message d'information
    * f_settings : Fichier de sauvegarde des paramètres
    """
    # Initialisation du str_message d'information
    str_message = "Les paramètres ont été sauvegardés !"
    # Récupération du nombre de lignes choisies par l'utilisateur
    i_rows = view_pp.vpp_get_nb_rows()
    # Récupération du nombre de colonnes choisies par l'utilisateur
    i_columns = view_pp.vpp_get_nb_columns()
    # Récupération du nombre de jetons à aligner choisies par l'utilisateur
    i_nb_jetons = view_pp.vpp_get_nb_jetons()
    # Récupération de la difficulté choisie par l'utilisateur
    i_difficulty = view_pp.vpp_get_difficulty()

    # Vérification des paramètres
    if i_nb_jetons > i_rows and i_nb_jetons > i_columns:
        # Changement du message par un message d'averstissement
        str_message = ("Les paramètres ne peuvent pas être sauvegardés car le "
                       "nombre de jetons est supérieur au nombre de lignes et "
                       "de colonnes !")
        # Affichage du str_message d'information
        ctrl_m.cm_warning(str_message)
    # Sinon
    else:
        # Ouverture du fichier de sauvegarde des paramètres
        with open("res/settings.txt", "w") as f_settings:
            # Écriture du nombre de lignes
            f_settings.write(str(i_rows) + "\n")
            # Écriture du nombre de colonnes
            f_settings.write(str(i_columns) + "\n")
            # Écriture du nombre de jetons à aligner
            f_settings.write(str(i_nb_jetons) + "\n")
            # Écriture de la difficulté
            f_settings.write(str(i_difficulty) + "\n")

        # Affichage du str_message d'information
        ctrl_m.cm_info(str_message)


def ctrl_page_parameter_settings_reset():
    """! Réinitialise les paramètres
    """
    # Réinitialisation des paramètres
    view_pp.v_page_parameter_reset_settings()


def ctrl_page_parameter_custom_save():
    """! Sauvegarde des paramètres de personnalisation

    @pre tk_root initialisé
    @pre res/custom.txt existant
    @post paramètres de personnalisation sauvegardés ou str_message d'erreur
        affiché

    **Variables :**
    * st_color_joueur : Couleur des jetons du joueur
    * st_color_bot : Couleur des jetons du bot
    * st_color_grid : Couleur de la grille
    * str_message : Message d'information
    * f_custom : Fichier de sauvegarde des paramètres de personnalisation
    """
    # Initialisation du str_message d'information
    str_message = "Les paramètres de personnalisation ont été sauvegardés !"
    # Récupération de la couleur des jetons du joueur choisie par l'utilisateur
    st_color_joueur = view_pp.vpp_get_joueur_color()
    # Récupération de la couleur des jetons du bot choisie par l'utilisateur
    st_color_bot = view_pp.vpp_get_bot_color()
    # Récupération de la couleur de la grille choisie par l'utilisateur
    st_color_grid = view_pp.vpp_get_grid_color()

    # Si deux couleurs sont trop proches
    if (ctrl_page_parameter_colors_too_close(st_color_joueur, st_color_bot)
            or
            ctrl_page_parameter_colors_too_close(st_color_joueur, st_color_grid)
            or
            ctrl_page_parameter_colors_too_close(st_color_bot, st_color_grid)):
        # Changement du message par un message d'avertissement
        str_message = ("Les paramètres de personnalisation ne peuvent pas être "
                       "sauvegardés car deux éléments ont la même couleur !")
        # Affichage du str_message d'information
        ctrl_m.cm_warning(str_message)
    # Sinon
    else:
        # Ouverture du fichier de sauvegarde des paramètres de personnalisation
        with open("res/custom.txt", "w") as f_custom:
            # Écriture de la couleur des jetons du joueur
            f_custom.write(st_color_joueur + "\n")
            # Écriture de la couleur des jetons du bot
            f_custom.write(st_color_bot + "\n")
            # Écriture de la couleur de la grille
            f_custom.write(st_color_grid + "\n")

        # Affichage du str_message d'information
        ctrl_m.cm_info(str_message)


def ctrl_page_parameter_settings_load() -> (int, int, int, int):
    """! Charge les paramètres
    @pre res/settings.txt existant
    @return i_rows: Nombre de lignes de la grille
    @return i_columns: Nombre de colonnes de la grille
    @return i_nb_jetons: Nombre de jetons à aligner pour gagner
    @return i_difficulty: Difficulté du bot

    **Variables :**
    * i_rows : Nombre de lignes de la grille
    * i_columns : Nombre de colonnes de la grille
    * i_nb_jetons : Nombre de jetons à aligner pour gagner
    * i_difficulty : Difficulté du bot
    """
    # Initialisation des variables
    i_rows, i_columns, i_nb_jetons, i_difficulty = 0, 0, 0, 0

    # Ouverture du fichier de sauvegarde des paramètres
    with open("res/settings.txt", "r") as f_settings:
        # Lecture de la première ligne
        i_rows = int(f_settings.readline())
        # Lecture de la deuxième ligne
        i_columns = int(f_settings.readline())
        # Lecture de la troisième ligne
        i_nb_jetons = int(f_settings.readline())
        # Lecture de la quatrième ligne
        i_difficulty = int(f_settings.readline())

    # On retourne les paramètres
    return i_rows, i_columns, i_nb_jetons, i_difficulty


def ctrl_page_parameter_custom_load() -> (str, str, str):
    """! Charge les paramètres de personnalisation
    @pre res/custom.txt existant
    @return st_color_joueur: Couleur des jetons du joueur
    @return st_color_bot: Couleur des jetons du bot
    @return st_color_grid: Couleur de la grille

    **Variables :**
    * st_color_joueur : Couleur des jetons du joueur
    * st_color_bot : Couleur des jetons du bot
    * st_color_grid : Couleur de la grille
    """
    # Initialisation des variables
    st_color_joueur, st_color_bot, st_color_grid = "", "", ""

    # Ouverture du fichier de sauvegarde des paramètres de personnalisation
    with open("res/custom.txt", "r") as f_custom:
        # Lecture de la première ligne
        st_color_joueur = f_custom.readline()
        # Lecture de la deuxième ligne
        st_color_bot = f_custom.readline()
        # Lecture de la troisième ligne
        st_color_grid = f_custom.readline()

    # Suppression du retour à la ligne
    st_color_joueur = st_color_joueur[:-1]
    # Suppression du retour à la ligne
    st_color_bot = st_color_bot[:-1]
    # Suppression du retour à la ligne
    st_color_grid = st_color_grid[:-1]

    # On retourne les paramètres
    return st_color_joueur, st_color_bot, st_color_grid


def ctrl_page_parameter_askcolor(s_element: str):
    """! Ouvre un sélecteur de couleur

    @param s_element: Élément à colorer (joueur, bot ou grille)
    """
    # Demande de la couleur
    view_pp.vpp_askcolor(s_element)


def ctrl_page_parameter_custom_reset():
    """! Réinitialise les paramètres de personnalisation
    """
    # Réinitialisation des paramètres de personnalisation
    view_pp.vpp_reset_customs()
