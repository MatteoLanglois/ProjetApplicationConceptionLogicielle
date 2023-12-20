import numpy as np

def pq_init_grille(i_max_ligne: int, i_max_colonne: int) -> np.array:
    """! L'initiateur de la grille

    **Variables :**
    * npa_grille : np.array

    **Préconditions :**
    * i_max_ligne > 1
    * i_max_colonne > 1

    **Postconditions :**
    * npa_grille initialisé

    @param i_max_ligne: Le nombre de lignes de la grille
    @param i_max_colonne: Le nombre de colonnes de la grille

    @return La grille créée
    """
    assert i_max_ligne > 1 and i_max_colonne > 1, \
        "La grille doit avoir au moins 2 lignes et 2 colonnes"
    # Création de la grille
    npa_grille = np.zeros((i_max_ligne, i_max_colonne))
    # Changement du type contenu dans la grille par "int"
    npa_grille.astype(int)
    # Retourne la grille
    return npa_grille

def pq_reset_grille(npa_grille: np.array) -> np.array:
    """! Réinitialise la grille

    **Variables :**
    * i_boucle : Entier
    * i_max_ligne : Entier
    * i_max_colonne : Entier

    **Préconditions :**
    * npa_grille initialisé

    **Postconditions :**
    * npa_grille contient des 0.

    @param npa_grille: La grille à réinitialiser

    @return La grille réinitialisée
    """
    # Récupération de la taille de la grille
    i_max_ligne, i_max_colonne = npa_grille.shape
    # Pour chaque ligne de la grille
    for i_boucle in range(i_max_ligne):
        # Pour chaque colonne de la grille
        for i_boucle_2 in range(i_max_colonne):
            # La case devient vide
            npa_grille[i_boucle][i_boucle_2] = 0
    # Retourne la grille
    return npa_grille

def pq_print_grille(npa_grille: np.array):
    """! Affiche la grille

    **Variables :**
    * char_joueur : Le caractère du jeton du joueur
    * char_bot : Le caractère du jeton du bot
    * char_vide : Le caractère représentant une case vide
    * i_max_ligne : Le nombre de lignes de la grille
    * i_max_colonne : Le nombre de colonnes de la grille
    * i_boucle_colonne : Le compteur de boucle pour les colonnes de la grille
    * i_boucle_ligne : Le compteur de boucle pour les lignes de la grille

    @param npa_grille: La grille à afficher
    """
    # Le caractère du jeton du joueur
    char_joueur = 'X'
    # Le caractère du jeton du bot
    char_bot = '0'
    # Le caractère représentant une case vide
    char_vide = ' '
    # Récupère la taille de la grille
    i_max_ligne, i_max_colonne = npa_grille.shape

    # Pour chaque colonne du tableau
    for i_boucle_ligne in range(i_max_ligne):
        # Pour chaque case de cette colonne
        for i_boucle_colonne in range(i_max_colonne):
            if npa_grille[i_boucle_ligne, i_boucle_colonne] == 1:
                # Affiche charJoueur si le joueur est le joueur humain
                print(f"|\033[91m{char_joueur}\033[00m", end="")
            elif npa_grille[i_boucle_ligne, i_boucle_colonne] == 2:
                # Affiche charBot si le joueur est le bot
                print(f"|\033[93m{char_bot}\033[00m", end="")
            else:
                # Affiche charVide si la case est vide
                print(f"|\033[00m{char_vide}\033[00m", end="")
        # Retourne à la ligne et affiche la barre de séparation des lignes
        print("|\n" + (2 * i_max_colonne + 1) * "-")