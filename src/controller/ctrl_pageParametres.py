"""! @file ctrl_pageParametres
Contrôleur de la page des paramètres

Contient les fonctions permettant de gérer la page des paramètres

"""
import tkinter as tk
from src.view import view_pageParametres as view_pp
from src.controller import ctrl_main as ctrl_m

global tk_root


def ctrl_page_parameter_init(tk_win_root: tk.Tk):
    """! Initialise la page des paramètres

    **Variables :**
    * tk_root : Fenêtre principale

    **Préconditions :**
    * tk_root initialisé

    @param tk_win_root: Fenêtre principale
    """
    global tk_root
    # Enregistrement de manière globale de la fenêtre principale
    tk_root = tk_win_root
    # Initialisation de la page des paramètres
    view_pp.v_page_parameter_init(tk_root)

    i_rows, i_columns, i_nb_jetons, i_difficulty = (
        ctrl_page_parameter_settings_load())
    view_pp.v_page_parameter_set_nb_rows(i_rows)
    view_pp.v_page_parameter_set_nb_columns(i_columns)
    view_pp.v_page_parameter_set_nb_jetons(i_nb_jetons)
    view_pp.v_page_parameter_set_difficulty(i_difficulty)

    st_color_joueur, st_color_bot, st_color_grid = (
        ctrl_page_parameter_custom_load())
    view_pp.v_page_parameter_set_joueur_color(st_color_joueur)
    view_pp.v_page_parameter_set_bot_color(st_color_bot)
    view_pp.v_page_parameter_set_grid_color(st_color_grid)


def ctrl_page_parameter_settings_save():
    """! Sauvegarde les paramètres
    """
    # Initialisation du message d'information
    message = "Les paramètres ont été sauvegardés !"
    # Récupération des paramètres
    i_rows = view_pp.v_page_parameter_get_nb_rows()
    i_columns = view_pp.v_page_parameter_get_nb_columns()
    i_nb_jetons = view_pp.v_page_parameter_get_nb_jetons()
    i_difficulty = view_pp.v_page_parameter_get_difficulty()

    # Vérification des paramètres
    if i_nb_jetons > i_rows and i_nb_jetons > i_columns:
        message = ("Les paramètres ne peuvent pas être sauvegardés car le "
                   "nombre de jetons est supérieur au nombre de lignes et de "
                   "colonnes !")
        # Affichage du message d'information
        ctrl_m.win_ctrl_warning(message)
    else:
        # Sauvegarde des paramètres
        with open("res/settings.txt", "w") as f_settings:
            f_settings.write(str(i_rows) + "\n")
            f_settings.write(str(i_columns) + "\n")
            f_settings.write(str(i_nb_jetons) + "\n")
            f_settings.write(str(i_difficulty) + "\n")

        # Affichage du message d'information
        ctrl_m.win_ctrl_info(message)


def ctrl_page_parameter_settings_reset():
    """! Réinitialise les paramètres
    """
    # Réinitialisation des paramètres
    view_pp.v_page_parameter_reset_settings()


def ctrl_page_parameter_custom_save():
    """! Sauvegarde des paramètres de personnalisation
    """
    # Initialisation du message d'information
    message = "Les paramètres de personnalisation ont été sauvegardés !"
    # Récupération des paramètres
    st_color_joueur = view_pp.v_page_parameter_get_joueur_color()
    st_color_bot = view_pp.v_page_parameter_get_bot_color()
    st_color_grid = view_pp.v_page_parameter_get_grid_color()

    if (ctrl_page_parameter_colors_too_close(st_color_joueur, st_color_bot)
            or
            ctrl_page_parameter_colors_too_close(st_color_joueur, st_color_grid)
            or
            ctrl_page_parameter_colors_too_close(st_color_bot, st_color_grid)):
        message = ("Les paramètres de personnalisation ne peuvent pas être "
                   "sauvegardés car deux éléments ont la même couleur !")
        # Affichage du message d'information
        ctrl_m.win_ctrl_warning(message)
    else:
        # Sauvegarde des paramètres
        with open("res/custom.txt", "w") as f_custom:
            f_custom.write(st_color_joueur + "\n")
            f_custom.write(st_color_bot + "\n")
            f_custom.write(st_color_grid + "\n")

        # Affichage du message d'information
        ctrl_m.win_ctrl_info(message)


def ctrl_page_parameter_settings_load() -> (int, int, int, int):
    with open("res/settings.txt", "r") as f_settings:
        i_rows = int(f_settings.readline())
        i_columns = int(f_settings.readline())
        i_nb_jetons = int(f_settings.readline())
        i_difficulty = int(f_settings.readline())

    return i_rows, i_columns, i_nb_jetons, i_difficulty


def ctrl_page_parameter_custom_load() -> (str, str, str):
    """! Charge les paramètres de personnalisation
    """
    with open("res/custom.txt", "r") as f_custom:
        st_color_joueur = f_custom.readline()
        st_color_bot = f_custom.readline()
        st_color_grid = f_custom.readline()

    st_color_joueur = st_color_joueur[:-1]
    st_color_bot = st_color_bot[:-1]
    st_color_grid = st_color_grid[:-1]

    return st_color_joueur, st_color_bot, st_color_grid


def ctrl_page_parameter_askcolor(s_element: str):
    """! Ouvre un sélecteur de couleur
    """
    view_pp.v_page_parameter_askcolor(s_element)


def ctrl_page_parameter_custom_reset():
    """! Réinitialise les paramètres de personnalisation
    """
    view_pp.v_page_parameter_reset_customs()


def ctrl_page_parameter_hex_to_rgb(s_color: str) -> (int, int, int):
    """! Convertit une couleur hexadécimale en RGB

    @param s_color: Couleur hexadécimale
    @return Couleur RGB
    """
    return tuple(int(s_color[i:i + 2], 16) for i in (1, 3, 5))


def ctrl_page_parameter_rgb_distance(rgb1: (int, int, int),
                                     rgb2: (int, int, int)) -> int:
    """! Calcule la distance entre deux couleurs RGB

    @param rgb1: Couleur 1
    @param rgb2: Couleur 2
    @return Distance entre les deux couleurs
    """
    return sum((a - b) ** 2 for a, b in zip(rgb1, rgb2)) ** 0.5


def ctrl_page_parameter_colors_too_close(color1: str, color2: str) -> bool:
    """! Vérifie si deux couleurs sont trop proches

    @param color1: Couleur 1 au format hexadécimal
    @param color2: Couleur 2 au format hexadécimal
    @return True si les couleurs sont trop proches, False sinon
    """
    rgb1 = ctrl_page_parameter_hex_to_rgb(color1)
    rgb2 = ctrl_page_parameter_hex_to_rgb(color2)

    return ctrl_page_parameter_rgb_distance(rgb1, rgb2) < 50
