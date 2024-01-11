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

@package src.view.view_pageBonus
@brief Ce module représente la vue de la page de choix du bonus.
@details Ce module contient les fonctions permettant de gérer la vue de la page
de choix du bonus.
"""
# Importation de tkinter pour l'interface graphique
import tkinter as tk
# Importation du contrôleur de cette fenêtre
from src.controller import ctrl_PageBonus as ctrl_pb
# Importation du contrôleur principal pour le menu
from src.controller import ctrl_main as ctrl_m
# Importation du module de gestion des widgets
from src.utils import widget_utils as wu

# Variables globales ##########################
# Variable de choix du bonus
global TKS_BONUS
# Label de la description du bonus
global TKL_DESCRIPTION_BONUS
# Cadre de la fenêtre de choix du bonus
global TKF_PAGE_CHOIX


def vpb_init(tk_root: tk.Tk) -> None:
    """! Initialisation de la fenêtre de choix du bonus.

    Cette fonction initialise la fenêtre de choix du bonus. Elle crée un cadre,
    un titre, un menu déroulant pour le choix du bonus, un label pour la
    description du bonus et un bouton pour valider le bonus. Elle affiche aussi
    la description du premier bonus. Elle affiche aussi le menu sur la fenêtre.

    @pre tk_root initialisé
    @param tk_root: la fenêtre de base
    @post Fenêtre de choix du bonus initialisée

    **Variables :**
    * TKS_BONUS : Variable de choix du bonus.
    * TKL_DESCRIPTION_BONUS : Label de la description du bonus.
    * TKF_PAGE_CHOIX : Cadre de la fenêtre de choix du bonus.
    * tkL_titre : Label du titre de la fenêtre de choix du bonus.
    * tkC_bonus : Menu déroulant pour le choix du bonus.
    * tkL_description : Label de la description du bonus.
    * tkB_valider : Bouton de validation du bonus.
    """
    global TKS_BONUS, TKL_DESCRIPTION_BONUS, TKF_PAGE_CHOIX
    # Initialisation du cadre de la fenêtre de choix du bonus
    TKF_PAGE_CHOIX = tk.Frame(tk_root, height=500, width=430, padx=20, pady=20)
    # Affichage du cadre de la fenêtre de choix du bonus
    TKF_PAGE_CHOIX.grid(row=0, column=0, sticky="nsew")

    # Récupération de la taille de police du menu
    i_font_size = wu.wu_get_font_size(TKF_PAGE_CHOIX, False)
    # Récupération de la taille de police du titre
    i_font_size_title = wu.wu_get_font_size(TKF_PAGE_CHOIX, True)

    # Affichage du menu sur la fenêtre
    tk_root.configure(menu=ctrl_m.cm_menu(TKF_PAGE_CHOIX, True))
    # Initialisation du titre de la fenêtre de choix du bonus
    tkL_titre = tk.Label(TKF_PAGE_CHOIX, text="Choisissez votre bonus",
                         font=("Helvetica", i_font_size_title))
    # Affichage du titre de la fenêtre de choix du bonus
    tkL_titre.grid(row=0, column=0, sticky="nsew", pady=50, padx=10)

    # Création d'une variable pour le choix du bonus
    TKS_BONUS = tk.StringVar()
    # Récupération de la liste des bonus
    ls_bonuses = ctrl_pb.cpb_get_bonuses()
    # Initialisation de la variable de choix du bonus
    TKS_BONUS.set(ls_bonuses[0])
    # Création du menu déroulant pour le choix du bonus
    tkC_bonus = tk.OptionMenu(TKF_PAGE_CHOIX, TKS_BONUS, *ls_bonuses)
    # Affichage du menu déroulant pour le choix du bonus
    tkC_bonus.grid(row=1, column=0, sticky="nsew", pady=50, padx=10)
    # Affichage de la description du bonus sélectionné
    TKS_BONUS.trace("w", lambda *args: ctrl_pb
                    .cpb_show_bonus_description(TKS_BONUS.get()))
    # Initialisation du label de la description du bonus
    tkL_description = tk.Label(TKF_PAGE_CHOIX, text="Description du bonus :",
                               font=("Helvetica", i_font_size))
    # Affichage du label de la description du bonus
    tkL_description.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)

    # Initialisation du label de la description du bonus
    TKL_DESCRIPTION_BONUS = tk.Label(TKF_PAGE_CHOIX, text="", width=40,
                                     font=("Helvetica", i_font_size),
                                     wraplength=300)
    # Affichage du label de la description du bonus
    TKL_DESCRIPTION_BONUS.grid(row=3, column=0, sticky="nsew", pady=10, padx=10)
    # Affichage de la description du premier bonus
    ctrl_pb.cpb_show_bonus_description(ls_bonuses[0])

    # Initialisation du bouton de validation du bonus
    tkB_valider = tk.Button(TKF_PAGE_CHOIX, text="Valider",
                            font=("Helvetica", i_font_size),
                            command=lambda: ctrl_pb.cpb_valider_bonus())
    # Affichage du bouton de validation du bonus
    tkB_valider.grid(row=4, column=0, sticky="nsew", pady=50, padx=10)


def vpb_get_bonus() -> tuple[str, ...]:
    """! Récupère le nom du bonus sélectionné par le joueur

    Cette fonction récupère le nom du bonus sélectionné par le joueur. Elle
    renvoie le nom du bonus sélectionné.

    @pre TKS_BONUS initialisé
    @return: Le nom du bonus sélectionné par le joueur

    **Variables :**
    * TKS_BONUS : Variable de choix du bonus.
    """
    global TKS_BONUS
    # On retourne le nom du bonus sélectionné
    return TKS_BONUS.get()


def vpb_show_bonus_description(s_description: str):
    """! Affiche la description d'un bonus

    Cette fonction affiche la description d'un bonus. Elle prend en paramètre
    la description du bonus à afficher. Elle affiche la description du bonus
    dans le label de la description du bonus.

    @pre TKL_DESCRIPTION_BONUS initialisé
    @param s_description: Description du bonus

    **Variables :**
    * TKL_DESCRIPTION_BONUS : Label de la description du bonus.
    """
    global TKL_DESCRIPTION_BONUS
    # On affiche la description du bonus
    TKL_DESCRIPTION_BONUS.config(text=s_description)


def vpb_get_frame() -> tk.Frame:
    """! Accesseur du cadre de la fenêtre de choix du bonus

    Cette fonction renvoie le cadre de la fenêtre de choix du bonus. Elle est
    utilisée par le contrôleur principal pour afficher la fenêtre de choix du
    bonus.

    @pre Cadre initialisé
    @return : Cadre de la fenêtre de choix du bonus.

    **Variables :**
    * TKF_PAGE_CHOIX : Cadre de la fenêtre de choix du bonus.
    """
    global TKF_PAGE_CHOIX
    # On retourne le cadre de la fenêtre de choix du bonus
    return TKF_PAGE_CHOIX
