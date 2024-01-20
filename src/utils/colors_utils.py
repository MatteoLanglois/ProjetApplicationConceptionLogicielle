"""! @brief Un programme qui joue au jeu puissance 4++.

Ce programme est un jeu de puissance 4++ avec une grille de taille variable,
un nombre de pions à aligner variable, des bonus et un undo.

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


def cu_rgb_to_hex(rgb: (int, int, int)) -> str:
    """! Convertit une couleur RGB en hexadécimal

    Cette fonction convertit une couleur RGB en hexadécimal.

    @param rgb: Couleur RGB
    @return Couleur hexadécimale
    """
    # Convertit les composantes en hexadécimal
    s_red, s_green, s_blue = rgb
    # Retourne la couleur hexadécimale
    return f'#{s_red:02x}{s_green:02x}{s_blue:02x}'


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


def cu_reduce_hue(i_hue: str) -> str:
    """! Réduit la teinte d'une couleur

    Cette fonction réduit la teinte d'une couleur.

    @param i_hue: Teinte de la couleur
    @return Teinte de la couleur réduite
    """
    # Convertit la couleur en RGB
    ti_color = cu_hex_to_rgb(i_hue)
    # Convertit la couleur en liste
    ti_color = list(ti_color)
    # Pour chaque composante
    for i_boucle in range(3):
        # Réduit la composante de 40%
        ti_color[i_boucle] = int(ti_color[i_boucle] * 0.6)
    # Retourne la couleur réduite
    return cu_rgb_to_hex(ti_color)
