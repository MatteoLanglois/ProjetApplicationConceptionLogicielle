"""! @brief Un programme qui joue au jeu puissance 4++.

Ce programme est un jeu de puissance 4++ avec une grille de taille variable,
un nombre de pions à aligner variable, des bonus et un undo.

Ce programme utilise les modules externes suivants :
- tkinter
- numpy
- inspect

@package src.controller.ctrl_main
@brief Un module qui gère la fenêtre principale du jeu
@details Ce module gère la fenêtre principale du jeu et les transitions entre
les différentes fenêtres.
"""
# Importation de tkinter
import tkinter as tk
# Importation du controller de la page d'accueil afin d'initialiser la fenêtre
from src.controller import ctrl_pageAccueil as ctrl_pa
# Importation du controller de la page de jeu afin d'initialiser la fenêtre
from src.controller import ctrl_pageJeu as ctrl_pj
# Importation du controller de la page de paramètres afin d'initialiser la
# fenêtre
from src.controller import ctrl_pageParametres as ctrl_pp
# Importation du controller de la page de bonus afin d'initialiser la fenêtre
from src.controller import ctrl_PageBonus as ctrl_pb
# Importation de la vue de la fenêtre globale
from src.view import view_main as view_m


def cm_init():
    """! Initialise la fenêtre de jeu

    Cette fonction initialise la fenêtre de jeu et lance la boucle principale.

    @pre tk_root initialisé
    @post boucle principale lancée

    **Variables :**
    * tk_root : Fenêtre principale

    """
    # Initialisation de la fenêtre
    tk_root = view_m.vm_init()
    # Initialisation de la page d'accueil
    ctrl_pa.cpa_init(tk_root)
    # Boucle principale
    tk_root.mainloop()


def cm_quit(tk_root: tk.Tk):
    """! Ferme la fenêtre de jeu

    Cette fonction appelle la fonction de fermeture de la fenêtre de jeu.

    @pre tk_root initialisé
    @param tk_root: Fenêtre principale
    """
    # Fermeture de la fenêtre
    view_m.vm_quit(tk_root)


def cm_menu(tk_frame: tk.Frame, b_in_game: bool) -> tk.Menu:
    """! Crée le menu de la fenêtre

    Cette fonction appelle la fonction de création du menu de la fenêtre. Elle
    renvoie le menu créé. Elle prend en paramètre le cadre de la dernière
    fenêtre et un booléen indiquant si le joueur est en jeu ou non.

    @pre tkf_old_frame initialisé
    @param tk_frame: Le cadre de la dernière fenêtre
    @param b_in_game: Booléen indiquant si le joueur est en jeu ou non
    @return Menu de la fenêtre
    @post Menu créé
    """
    # Création du menu
    return view_m.vm_menu(tk_frame, b_in_game)


def cm_page_play(tk_root: tk.Tk, tkf_old_frame: tk.Frame):
    """! Fonction permettant de passer à la fenêtre de jeu.

    Cette fonction appelle la fonction de suppression du cadre de la dernière
    fenêtre et la fonction d'initialisation de la page de jeu. Elle permet de
    passer à la fenêtre de jeu.

    @pre tk_root initialisé
    @pre tkf_old_frame initialisé
    @param tk_root: La fenêtre principale
    @param tkf_old_frame: Le cadre de la dernière fenêtre
    @post tkf_old_frame détruit
    @post fenêtre de jeu initialisée
    """
    # Supprime le cadre
    view_m.vm_remove_frame(tkf_old_frame)
    # Initialise la page jeu
    ctrl_pj.cpj_init(tk_root)


def cm_page_bonus(tk_root: tk.Tk, tkf_old_frame: tk.Frame):
    """! Fonction permettant de passer à la fenêtre de jeu.

    Cette fonction appelle la fonction de suppression du cadre de la dernière
    fenêtre et la fonction d'initialisation de la page de jeu. Elle permet de
    passer à la fenêtre de jeu.

    @pre tk_root initialisé
    @pre tkf_old_frame initialisé
    @param tk_root: La fenêtre principale
    @param tkf_old_frame: Le cadre de la dernière fenêtre
    @post tkf_old_frame détruit
    @post fenêtre de jeu initialisée
    """
    # Supprime le cadre
    view_m.vm_remove_frame(tkf_old_frame)
    # Initialise la page jeu
    ctrl_pb.cpb_init(tk_root)


def cm_page_parameters(tk_root: tk.Tk, tkf_old_frame: tk.Frame):
    """! Fonction permettant de passer à la fenêtre de paramètres

    Cette fonction appelle la fonction de suppression du cadre de la dernière
    fenêtre et la fonction d'initialisation de la page de paramètres. Elle
    permet de passer à la fenêtre de paramètres.

    @pre tk_root initialisé
    @pre tkf_old_frame initialisé
    @param tk_root: La fenêtre principale
    @param tkf_old_frame: Le cadre de la dernière fenêtre
    @post tkf_old_frame détruit
    @post fenêtre de paramètres initialisée
    """
    # Supprime le cadre
    view_m.vm_remove_frame(tkf_old_frame)
    # Initialise la page de paramètres
    ctrl_pp.cpp_init(tk_root)


def cm_page_accueil(tk_root: tk.Tk, tkf_old_frame: tk.Frame):
    """! Fonction permettant de passer à la fenêtre d'accueil

    Cette fonction appelle la fonction de suppression du cadre de la dernière
    fenêtre et la fonction d'initialisation de la page d'accueil. Elle permet
    de passer à la fenêtre d'accueil.

    @pre tk_root initialisé
    @pre tkf_old_frame initialisé
    @param tk_root: La fenêtre principale
    @param tkf_old_frame: Le cadre de la dernière fenêtre
    @post tkf_old_frame détruit
    @post fenêtre d'accueil initialisée
    """
    # Supprime le cadre
    view_m.vm_remove_frame(tkf_old_frame)
    # Initialise la page d'accueil
    ctrl_pa.cpa_init(tk_root)


def cm_ended_game(str_message: str, tkf_old_frame: tk.Frame):
    """! Fonction permettant de passer à la fenêtre de fin de partie

    Cette fonction appelle la fonction de suppression du cadre de la dernière
    fenêtre et la fonction d'initialisation de la page de fin de partie. Elle
    permet de passer à la fenêtre de fin de partie.

    @pre tkf_old_frame initialisé
    @param str_message: Message à afficher
    @param tkf_old_frame: Le cadre de la dernière fenêtre
    """
    # Affiche le message de fin de partie
    view_m.vm_message_game_ended(str_message, tkf_old_frame)


def cm_warning(str_message: str):
    """! Affiche un message d'avertissement.

    Cette fonction appelle la fonction d'affichage d'un message d'avertissement.

    @param str_message: Message à afficher
    """
    # Affiche le message d'avertissement
    view_m.vm_message_warning(str_message)


def cm_info(str_message: str):
    """! Affiche un message d'information.

    Cette fonction appelle la fonction d'affichage d'un message d'information.

    @param str_message: Message à afficher
    """
    # Affiche le message d'information
    view_m.vm_message_info(str_message)


def cm_update(tk_root: tk.Tk):
    """! Met à jour la fenêtre

    Cette fonction appelle la fonction de mise à jour de la fenêtre principale.

    @pre tk_root initialisé
    @param tk_root: Fenêtre principale
    """
    # Met à jour la fenêtre
    view_m.vm_update(tk_root)
