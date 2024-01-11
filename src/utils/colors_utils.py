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

@package src.utils.colors_utils
@brief Ce module contient les fonctions relatives aux couleurs.
@details Ce module contient les fonctions de gestion des couleurs. Notamment
la conversion d'une couleur hexadécimale en RGB et la vérification de la
distance entre deux couleurs.
"""


def cu_hex_to_rgb(s_color: str) -> (int, int, int):
    """! Convertit une couleur hexadécimale en RGB

    Cette fonction convertit une couleur hexadécimale en RGB.

    @param s_color: Couleur hexadécimale
    @return Couleur RGB
    """
    return tuple(int(s_color[i:i + 2], 16) for i in (1, 3, 5))


def cu_rgb_distance(rgb1: (int, int, int),
                    rgb2: (int, int, int)) -> int:
    """! Calcule la distance entre deux couleurs RGB

    Cette fonction calcule la distance entre deux couleurs RGB. Elle utilise
    la formule de la distance euclidienne.

    @param rgb1: Couleur 1
    @param rgb2: Couleur 2
    @return Distance entre les deux couleurs
    """
    return sum((a - b) ** 2 for a, b in zip(rgb1, rgb2)) ** 0.5


def cu_colors_too_close(color1: str, color2: str) -> bool:
    """! Vérifie si deux couleurs sont trop proches.

    Cette fonction vérifie si deux couleurs sont trop proches. Elle utilise
    la fonction cu_rgb_distance pour calculer la distance entre les deux
    couleurs. Si la distance est inférieure à 50, les couleurs sont trop
    proches.

    @param color1: Couleur 1 au format hexadécimal
    @param color2: Couleur 2 au format hexadécimal
    @return True si les couleurs sont trop proches, False sinon
    """
    rgb1 = cu_hex_to_rgb(color1)
    rgb2 = cu_hex_to_rgb(color2)

    return cu_rgb_distance(rgb1, rgb2) < 50
