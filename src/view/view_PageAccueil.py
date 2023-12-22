"""! Page d'accueil du jeu.
Ce module contient les fonctions d'initialisation et de destruction de la page
d'accueil.

@see src/controller/ctrl_pageAccueil.py
"""

import tkinter as tk
from src.controller import ctrl_main as ctrl_m

"""! Frame de la page d'accueil
"""
global tkf_page_accueil


def v_page_accueil_init(tk_root: tk.Tk):
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
    global tkf_page_accueil
    # Création d'un cadre pour la page d'accueil
    tkf_page_accueil = tk.Frame(tk_root, height=500, width=500, padx=50,
                                pady=50)
    # Affichage du cadre de la page d'accueil
    tkf_page_accueil.grid(row=0, column=0, sticky="nsew")

    # Affichage du menu sur toutes les fenêtres
    tk_root.configure(menu=ctrl_m.win_ctrl_menu(tkf_page_accueil, False))

    # Création d'un label contenant puissance 4
    tkl_title = tk.Label(tkf_page_accueil, text="Puissance 4 !",
                         font=("Helvetica", 24))
    # Affichage de ce label
    tkl_title.grid(row=0, column=0, sticky="nsew", pady=50, padx=50)

    # Création d'un bouton pour jouer
    tkB_play = tk.Button(tkf_page_accueil, text="Jouer", font=("Helvetica", 20),
                         command=lambda:
                         ctrl_m.win_ctrl_page_play(tk_root, tkf_page_accueil))
    # Affichage de ce bouton
    tkB_play.grid(row=1, column=0, sticky="nsew", pady=50, padx=50)


def v_page_accueil_destroy():
    """! Détruit la page d'accueil

    **Variables :**
    * tkf_page_accueil : Frame de la page d'accueil
    """
    # On définit la variable tkf_page_accueil en globale
    global tkf_page_accueil
    # On efface le cadre
    tkf_page_accueil.pack_forget()
    # On supprime le cadre
    tkf_page_accueil.destroy()
