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

@package src.view.view_pageAccueil
@brief Ce module représente la vue de la page d'accueil.
@details Ce module contient les fonctions d'initialisation et de destruction de
la page d'accueil.
"""
# Importation de tkinter
import tkinter as tk
# Importation du contrôleur principal pour avoir le menu
from src.controller import ctrl_main as ctrl_m
# Importation du contrôleur de la page d'accueil pour lancer une partie
from src.controller import ctrl_pageAccueil as ctrl_pa

# Variables globales ##########################
# Frame de la page d'accueil
global TKF_PAGE_ACCUEIL


def vpa_init(tk_root: tk.Tk):
    """! Initialise la page d'accueil

    **Variables :**
    * tkf_page_accueil : Frame de la page d'accueil
    * tkl_title : Label contenant le titre
    * tkB_play : Bouton pour lancer une partie

    **Préconditions :**
    * tk_root initialisé

    @param tk_root: Fenêtre principale

    @see src/controller/ctrl_pageAccueil.py
    """
    # On définit la variable tkf_page_accueil en globale
    global TKF_PAGE_ACCUEIL
    # Création d'un cadre pour la page d'accueil
    TKF_PAGE_ACCUEIL = tk.Frame(tk_root, height=500, width=500, padx=50,
                                pady=50)
    # Affichage du cadre de la page d'accueil
    TKF_PAGE_ACCUEIL.grid(row=0, column=0, sticky="nsew")

    # Affichage du menu sur toutes les fenêtres
    tk_root.configure(menu=ctrl_m.cm_menu(TKF_PAGE_ACCUEIL, False))

    # Création d'un label contenant puissance 4
    tkl_title = tk.Label(TKF_PAGE_ACCUEIL, text="Puissance 4 !",
                         font=("Helvetica", 24))
    # Affichage de ce label
    tkl_title.grid(row=0, column=0, sticky="nsew", pady=50, padx=50)

    # Création d'un bouton pour jouer
    tkB_play = tk.Button(TKF_PAGE_ACCUEIL, text="Jouer", font=("Helvetica", 20),
                         command=lambda: ctrl_pa.cpa_play(tk_root,
                                                          TKF_PAGE_ACCUEIL)
                         )
    # Affichage de ce bouton
    tkB_play.grid(row=1, column=0, sticky="nsew", pady=50, padx=50)


def vpa_destroy():
    """! Détruit la page d'accueil

    **Variables :**
    * tkf_page_accueil : Frame de la page d'accueil
    """
    # On définit la variable tkf_page_accueil en globale
    global TKF_PAGE_ACCUEIL
    # On efface le cadre
    TKF_PAGE_ACCUEIL.pack_forget()
    # On supprime le cadre
    TKF_PAGE_ACCUEIL.destroy()
