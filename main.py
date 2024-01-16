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
- argparse

@package src.main
@brief Programme principal du jeu
@details Ce module permet de lancer le jeu. Il contient un parser d'arguments
qui permet de lancer le jeu en ligne de commande ou avec l'interface graphique.
"""
import src.puissanceQuatre.gestionPartie as gp
import src.controller.ctrl_main as ctrl_m
import argparse


def main():
    """! Fonction principale du jeu

    **Variables**
    * **parser** : Parser d'arguments
    * **group** : Groupe d'arguments mutuellement exclusifs
    * **args** : Arguments parsés

    @pre Lancer le programme avec l'argument --gui ou --cli
    @post Lance le jeu en ligne de commande ou avec l'interface graphique
    @return None

    """
    # On crée un parser d'arguments
    parser = argparse.ArgumentParser(description='Lance le jeu Puissance 4++.')
    # On crée un groupe d'arguments mutuellement exclusifs
    group = parser.add_mutually_exclusive_group()
    # On ajoute le paramètre gui au groupe
    group.add_argument('-gui', action='store_true',
                       help='Lance le jeu avec l\'interface graphique')
    # On ajoute le paramètre cli au groupe
    group.add_argument('-cli', action='store_true',
                       help='Lance le jeu en ligne de commande')
    # On parse les arguments
    args = parser.parse_args()
    # On lance le jeu en fonction des arguments
    if args.cli:
        # On lance le jeu en ligne de commande
        gp.gp_start_game()
    # Sinon
    else:
        # On lance le jeu avec l'interface graphique
        ctrl_m.cm_init()


# Si le module est le module principal
if __name__ == '__main__':
    # On lance la fonction principale
    main()
