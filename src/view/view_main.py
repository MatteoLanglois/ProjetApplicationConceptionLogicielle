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

@package src.view.view_main
@brief Ce module contient les fonctions de base utile à la vue du jeu.
@details Ce module permet de facilement avoir le menu sur toutes les fenêtres.
De quitter le jeu, de recommencer une partie, etc. Il permet aussi d'afficher
des messages d'information ou d'avertissement.
"""
# Importation de tkinter
import tkinter as tk
# Importation de tkinter.messagebox pour les messages
from tkinter.messagebox import showinfo, askyesno, showwarning
# Importation de ctrl_main pour les fonctions de contrôle
from src.controller import ctrl_main as ctrl_m

# Variables globales ##########################
# Fenêtre principale
global TK_ROOT


def vm_init() -> tk.Tk:
    """! Initialise la fenêtre de jeu

    **Variables :**
    * tk_root : Fenêtre principale

    @return Fenêtre principale
    """
    global TK_ROOT
    # Création de la fenêtre principale
    TK_ROOT = tk.Tk()
    # Changement du titre de la fenêtre principale
    TK_ROOT.title("Puissance 4")
    # Importation du logo
    TK_ROOT.iconbitmap("res/LogoP4++.ico")
    # Renvoie de la fenêtre créée
    return TK_ROOT


def vm_quit(tk_win_root: tk.Tk):
    """! Ferme la fenêtre de jeu

    **Préconditions :**
    * tk_root initialisé

    @param tk_win_root: Fenêtre principale
    """
    # Suppression de la fenêtre principale
    tk_win_root.quit()


def vm_menu(tk_old_frame: tk.Frame, b_in_game: bool) -> tk.Menu:
    """! Initialise le menu de la fenêtre de jeu

    **Variables :**
    * tkm_menu_bar : Menu de la fenêtre de jeu
    * tkm_menu_partie : sous-menu permettant de gérer la partie
    * tkm_menu_param : sous-menu permettant d'accéder aux paramètres
    * tkm_menu_a_propos : sous-menu permettant d'accéder à la page "À propos"

    @return Menu de la fenêtre de jeu
    """
    global TK_ROOT
    # Création du menu
    tkm_menu_bar = tk.Menu()

    # Création du sous menu pour la partie
    tkm_menu_partie = tk.Menu(tkm_menu_bar, tearoff=False)
    # Ajout dans la barre de menu du sous menu.
    tkm_menu_bar.add_cascade(label="Partie",
                             menu=tkm_menu_partie)
    # Ajout d'une commande permettant de lancer une partie
    tkm_menu_partie.add_command(label="Nouvelle partie",
                                command=lambda:
                                ctrl_m.cm_page_bonus(TK_ROOT,
                                                     tk_old_frame))
    if b_in_game:
        # Ajout d'une commande permettant de relancer une partie
        tkm_menu_partie.add_command(label="Recommencer",
                                    command=lambda:
                                    ctrl_m.cm_page_bonus(TK_ROOT,
                                                         tk_old_frame))

    # Ajout d'une commande permettant de quitter le jeu
    tkm_menu_partie.add_command(label="Quitter",
                                command=lambda: vm_quit)

    # Ajout d'un bouton dans le menu pour accéder aux paramètres
    tkm_menu_bar.add_command(label="Paramètres",
                             command=lambda:
                             ctrl_m.cm_page_parameters(TK_ROOT,
                                                       tk_old_frame))

    # Renvoie du menu
    return tkm_menu_bar


def vm_message_game_ended(s_message: str, tkf_page_jeu: tk.Frame):
    """! Affiche un message de fin de partie

    **Préconditions :**
    * tk_root initialisé

    @param s_message: Message à afficher
    @param tkf_page_jeu: La page de jeu
    """
    # Affichage du message
    if askyesno(title="Fin de partie",
                message=f"Fin de partie\n{s_message}\nVoulez-vous rejouer ?"):
        # Si l'utilisateur veut rejouer, on relance une partie
        ctrl_m.cm_page_play(TK_ROOT, tkf_page_jeu)
    else:
        # Sinon, on revient à la page d'accueil
        ctrl_m.cm_page_accueil(TK_ROOT, tkf_page_jeu)


def vm_message_warning(str_message: str):
    """! Affiche un message d'avertissement

    @param str_message: Message à afficher
    """
    # Affiche un message d'avertissement
    showwarning(title="Avertissement", message=str_message)


def vm_message_info(str_message: str):
    """! Affiche un message d'information

    @param str_message: Message à afficher
    """
    # Affiche un message d'information
    showinfo(title="Information", message=str_message)


def vm_remove_frame(frame: tk.Frame):
    """! Supprime un cadre

    @pre frame existe
    @param frame: Le cadre à supprimer
    @post frame n'existe plus
    """
    # Efface le cadre
    frame.forget()
    # Supprime le cadre
    frame.destroy()
