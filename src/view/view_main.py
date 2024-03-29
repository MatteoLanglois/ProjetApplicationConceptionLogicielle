"""! @brief Un programme qui joue au jeu puissance 4++.

Ce programme est un jeu de puissance 4++ avec une grille de taille variable,
un nombre de pions à aligner variable, des bonus et un undo.

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
from tkinter import font
# Importation de tkinter.messagebox pour les messages
from tkinter.messagebox import showinfo, askyesno, showwarning
# Importation de ctrl_main pour les fonctions de contrôle
from src.controller import ctrl_main as ctrl_m
# Importation de widget_utils pour les fonctions de gestion des widgets
from src.utils import widget_utils as wu

# Variables globales ##########################
# Fenêtre principale
global TK_ROOT


def vm_init() -> tk.Tk:
    """! Initialise la fenêtre de jeu

    Cette fonction initialise la fenêtre principale du jeu. Elle crée la
    fenêtre, lui donne un titre, un logo, la rend non redimensionnable et
    renvoie la fenêtre créée.

    **Variables :**
    * tk_root : Fenêtre principale
    * tkfo_default_font : Police par défaut

    @return Fenêtre principale
    """
    global TK_ROOT
    # Création de la fenêtre principale
    TK_ROOT = tk.Tk()
    # Changement du titre de la fenêtre principale
    TK_ROOT.title("Puissance 4")
    # Importation du logo
    TK_ROOT.iconbitmap("res/LogoP4++.ico")
    # Désactive le redimensionnement de la fenêtre
    TK_ROOT.resizable(width=False, height=False)
    # Récupère la police par défaut
    tkfo_default_font = font.Font(name="TkDefaultFont", exists=True)
    # Change la taille de la police par défaut
    tkfo_default_font.configure(size=wu.wu_get_font_size_window(TK_ROOT, False))
    # Renvoie de la fenêtre créée
    return TK_ROOT


def vm_quit(tk_win_root: tk.Tk):
    """! Ferme la fenêtre de jeu

    Cette fonction ferme la fenêtre principale du jeu.


    **Préconditions :**
    * tk_root initialisé

    @param tk_win_root: Fenêtre principale
    """
    # Suppression de la fenêtre principale
    tk_win_root.quit()


def vm_menu(tk_old_frame: tk.Frame, b_in_game: bool) -> tk.Menu:
    """! Initialise le menu de la fenêtre de jeu

    Cette fonction initialise le menu de la fenêtre principale du jeu. Elle
    crée le menu, les sous-menus, les commandes et renvoie le menu créé. Ce
    menu est affiché dans toutes les fenêtres.

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

    Cette fonction affiche un message de fin de partie. Elle demande à
    l'utilisateur s'il veut rejouer ou non. Si oui, elle relance une partie
    sinon elle revient à la page d'accueil. Elle est appelée lorsque la partie
    est terminée.

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

    Cette fonction affiche un message d'avertissement. Elle est appelée lorsque
    l'utilisateur fait une action qui n'est pas autorisée. Par exemple, si
    l'utilisateur choisit des paramètres qui ne sont pas compatibles avec le
    jeu.

    @param str_message: Message à afficher
    """
    # Affiche un message d'avertissement
    showwarning(title="Avertissement", message=str_message)


def vm_message_info(str_message: str):
    """! Affiche un message d'information

    Cette fonction affiche un message d'information. Elle est appelée lorsque
    l'utilisateur fait une action qui est autorisée. Par exemple, lorsque
    l'utilisateur change les paramètres du jeu.

    @param str_message: Message à afficher
    """
    # Affiche un message d'information
    showinfo(title="Information", message=str_message)


def vm_remove_frame(frame: tk.Frame):
    """! Supprime un cadre

    Cette fonction supprime un cadre. Elle est appelée lorsque l'on veut
    changer de page.

    @pre frame existe
    @param frame: Le cadre à supprimer
    @post frame n'existe plus
    """
    # Efface le cadre
    frame.forget()
    # Supprime le cadre
    frame.destroy()


def vm_update(tk_root: tk.Tk):
    """! Met à jour la fenêtre principale

    Cette fonction met à jour la fenêtre principale. Elle est appelée lorsque
    l'on veut mettre à jour la fenêtre principale.

    @param tk_root: Fenêtre principale
    """
    # Met à jour la fenêtre principale
    tk_root.update_idletasks()
