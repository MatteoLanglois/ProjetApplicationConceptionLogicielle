"""! Vue principale du jeu
Ce module contient les fonctions de base utile à la vue du jeu.

Ce module permet de facilement avoir le menu sur toutes les fenêtres. De quitter
le jeu, de recommencer une partie, etc.

@see src/controller/ctrl_main.py
"""

import tkinter as tk
from tkinter.messagebox import showinfo, askyesno, showwarning

from src.controller import ctrl_main as ctrl_m

global tk_root


def win_init() -> tk.Tk:
    """! Initialise la fenêtre de jeu

    **Variables :**
    * tk_root : Fenêtre principale

    @return Fenêtre principale
    """
    global tk_root
    # Création de la fenêtre principale
    tk_root = tk.Tk()
    # Changement du titre de la fenêtre principale
    tk_root.title("Puissance 4")
    # Renvoie de la fenêtre créée
    return tk_root


def win_quit(tk_win_root: tk.Tk):
    """! Ferme la fenêtre de jeu

    **Préconditions :**
    * tk_root initialisé

    @param tk_win_root: Fenêtre principale
    """
    # Suppression de la fenêtre principale
    tk_win_root.quit()


def win_menu(tk_old_frame: tk.Frame, b_in_game: bool) -> tk.Menu:
    """! Initialise le menu de la fenêtre de jeu

    **Variables :**
    * tkm_menu_bar : Menu de la fenêtre de jeu
    * tkm_menu_partie : sous-menu permettant de gérer la partie
    * tkm_menu_param : sous-menu permettant d'accéder aux paramètres
    * tkm_menu_a_propos : sous-menu permettant d'accéder à la page "À propos"

    @return Menu de la fenêtre de jeu
    """
    global tk_root
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
                                ctrl_m.win_ctrl_page_play(tk_root,
                                                          tk_old_frame))
    if b_in_game:
        # Ajout d'une commande permettant de relancer une partie
        tkm_menu_partie.add_command(label="Recommencer",
                                    command=lambda:
                                    ctrl_m.win_ctrl_page_play(tk_root,
                                                              tk_old_frame))

    # Ajout d'une commande permettant de quitter le jeu
    tkm_menu_partie.add_command(label="Quitter",
                                command=lambda: win_quit)

    # Ajout d'un bouton dans le menu pour accéder aux paramètres
    tkm_menu_bar.add_command(label="Paramètres",
                             command=lambda:
                             ctrl_m.win_ctrl_page_parameters(tk_root,
                                                             tk_old_frame))
    # Ajout d'un bouton dans le menu pour accéder à la page à propos
    tkm_menu_bar.add_command(label="A propos",
                             command=lambda: print("A propos"))
    # Renvoie du menu
    return tkm_menu_bar


def win_message_game_ended(s_message: str, tkf_page_jeu: tk.Frame):
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
        ctrl_m.win_ctrl_page_play(tk_root, tkf_page_jeu)
    else:
        # Sinon, on revient à la page d'accueil
        ctrl_m.win_ctrl_page_accueil(tk_root, tkf_page_jeu)


def win_message_warning(str_message):
    """! Affiche un message d'avertissement

    @param str_message: Message à afficher
    """
    showwarning(title="Avertissement", message=str_message)


def win_message_info(str_message):
    """! Affiche un message d'information

    @param str_message: Message à afficher
    """
    showinfo(title="Information", message=str_message)