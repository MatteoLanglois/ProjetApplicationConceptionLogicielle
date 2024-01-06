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

@package src.view.view_PageBonus
@brief Ce module représente la vue de la page de choix du bonus.
@details Ce module contient les fonctions permettant de gérer la vue de la page
de choix du bonus.
"""
import tkinter as tk
from src.controller import ctrl_PageBonus as ctrl_pb
from src.controller import ctrl_main as ctrl_m

global TKS_BONUS
global TKL_DESCRIPTION_BONUS
global TKF_PAGE_CHOIX


def vpb_init(tk_root: tk.Tk) -> None:
    """! Initialisation de la fenêtre de choix du bonus.
    @todo à commenter

    @param tk_root: la fenêtre de base
    """
    global TKS_BONUS, TKL_DESCRIPTION_BONUS, TKF_PAGE_CHOIX
    TKF_PAGE_CHOIX = tk.Frame(tk_root, height=500, width=430, padx=20, pady=20)
    TKF_PAGE_CHOIX.grid(row=0, column=0, sticky="nsew")

    # Affichage du menu sur la fenêtre
    tk_root.configure(menu=ctrl_m.cm_menu(TKF_PAGE_CHOIX, True))

    tkL_titre = tk.Label(TKF_PAGE_CHOIX, text="Choisissez votre bonus",
                         font=("Helvetica", 20))
    tkL_titre.grid(row=0, column=0, sticky="nsew", pady=50, padx=10)

    TKS_BONUS = tk.StringVar()
    ls_bonuses = ctrl_pb.cpb_get_bonuses()
    TKS_BONUS.set(ls_bonuses[0])

    tkC_bonus = tk.OptionMenu(TKF_PAGE_CHOIX, TKS_BONUS, *ls_bonuses)
    tkC_bonus.grid(row=1, column=0, sticky="nsew", pady=50, padx=10)
    TKS_BONUS.trace("w", lambda *args: ctrl_pb
                    .cpb_show_bonus_description(TKS_BONUS.get()))

    tkL_description = tk.Label(TKF_PAGE_CHOIX, text="Description du bonus :",
                               font=("Helvetica", 16))
    tkL_description.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)

    TKL_DESCRIPTION_BONUS = tk.Label(TKF_PAGE_CHOIX, text="", width=40,
                                     font=("Helvetica", 14), wraplength=300)
    TKL_DESCRIPTION_BONUS.grid(row=3, column=0, sticky="nsew", pady=10, padx=10)
    ctrl_pb.cpb_show_bonus_description(ls_bonuses[0])

    tkB_valider = tk.Button(TKF_PAGE_CHOIX, text="Valider",
                            font=("Helvetica", 16),
                            command=lambda: ctrl_pb.cpb_valider_bonus())
    tkB_valider.grid(row=4, column=0, sticky="nsew", pady=50, padx=10)


def vpb_get_bonus() -> tuple[str, ...]:
    """! Récupère le nom du bonus sélectionné par le joueur
    @return: Le nom du bonus sélectionné par le joueur
    @pre TKS_BONUS initialisé
    """
    global TKS_BONUS
    # On retourne le nom du bonus sélectionné
    return TKS_BONUS.get()


def vpb_show_bonus_description(s_description: str):
    """! Affiche la description d'un bonus
    @param s_description: Description du bonus
    @pre TKL_DESCRIPTION_BONUS initialisé
    """
    global TKL_DESCRIPTION_BONUS
    # On affiche la description du bonus
    TKL_DESCRIPTION_BONUS.config(text=s_description)


def vpb_get_frame() -> tk.Frame:
    """! Accesseur du cadre de la fenêtre de choix du bonus

    @pre Cadre initialisé
    @return : Cadre de la fenêtre de choix du bonus.

    **Variables :**
    * TKF_PAGE_CHOIX : Cadre de la fenêtre de choix du bonus.
    """
    global TKF_PAGE_CHOIX
    return TKF_PAGE_CHOIX
