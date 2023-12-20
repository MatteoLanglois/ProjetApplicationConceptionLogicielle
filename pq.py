import numpy as np


def AjoutPiece(iColonne, iJoueur, npaGrille):
    """
    Préconditions :
        Il faut que le joueur puisse poser son pion dans cette colonne
        VerifColonne(iColonne)
    Postconditions : 
        npaGrille[iColonne] contient le pion posé par le joueur
    Entrée :
        iColonne: Entier
        iJoueur: Entier
    Sortie :
        TEEcoords: Tuple(Entier, Entier)
    Variable :
        npaGrille: Tableau de [0,...,iMaxLigne] 
            de Tableau de [0,...,iMaxColonne] entiers
        iMaxLigne: Entier
        iMaxColonne: Entier      
        iBoucle: Entier
    """
    # Initialisation du compteur de boucle
    iBoucle = 0
    iMaxLigne = len(npaGrille)
    iMaxColonne = len(npaGrille[0])

    # Tant que la case de la grille de notre colonne est vide
    while iBoucle < iMaxLigne and npaGrille[iBoucle][iColonne] == 0:
        # Augmenter le compteur de boucle
        iBoucle += 1

    # Ajouter le jeton du joueur dans la dernière case vide
    npaGrille[iBoucle - 1][iColonne] = iJoueur

    # Retourner un tuple des coordonnées du nouveau jeton
    return (iBoucle - 1, iColonne)


def PartieFinie(npaGrille, bBonusJoueur):
    """
    Variable:
        iMaxLigne, iMaxColonne : Entier
        bTableauPlein : Booleen
    """
    iMaxLigne = len(npaGrille)
    iMaxColonne = len(npaGrille[0])

    bTableauPlein = True

    for i in range(iMaxLigne):
        for j in range(iMaxColonne):
            if npaGrille[i][j] == 0:
                bTableauPlein = False

    return bTableauPlein or bBonusJoueur


def GestionPartie(iMaxLigne, iMaxColonne, npaGrille):
    """
    Variables :
        tUndoRedo: Tableau d'entiers
        npaGrille: Tableau de [0,...,iMaxLigne] 
            de Tableau de [0,...,iMaxColonne] Entiers
        iBoucle, iColonneJoueur, iColonneBot, iLigneJoueur, iLigneBot: Entier
        bVictoire: Booléen
    """
    iBoucle = 0
    bVictoire = False
    tUndoRedo = []
    bBonusJoueur = False

    while (not PartieFinie(npaGrille, bBonusJoueur) and not bVictoire):
        # Les tours de boucle s'effectuent jusqu'à ce qu'il ne reste plus de coup à jouer.
        iColonneJoueur = int(input("Quelle colonne voulez-vous jouer ? "))

        if VerifColonne(iColonneJoueur, npaGrille):
            # On vérifie si le joueur peut jouer dans la colonne qu'il a sélectionnée
            iLigneJoueur, iColonneJoueur = AjoutPiece(iColonneJoueur, 1,
                                                      npaGrille)

            if VictoireColonne(iLigneJoueur, iColonneJoueur, 1, npaGrille) or \
                    VictoireLigne(iLigneJoueur, iColonneJoueur, 1, npaGrille) or \
                    VictoireDiago(iLigneJoueur, iColonneJoueur, 1, npaGrille):
                # Vérification de la victoire
                print("Le joueur 1 a gagné !")
                bVictoire = True
            else:
                iColonneBot = MinMax(2, npaGrille, isFirst=True)
                # On appelle MinesMax pour savoir dans quelle colonne le bot va jouer
                iLigneBot, iColonneBot = AjoutPiece(iColonneBot, 2, npaGrille)

                if VictoireColonne(iLigneBot, iColonneBot, 2, npaGrille) or \
                        VictoireLigne(iLigneBot, iColonneBot, 2, npaGrille) or \
                        VictoireDiago(iLigneBot, iColonneBot, 2, npaGrille):
                    # Vérification de la victoire
                    print("Le joueur 2 a gagné !")
                    bVictoire = True

                tUndoRedo.append(npaGrille)
                iBoucle += 1
            print(npaGrille)
        else:
            print("Vous ne pouvez pas jouer dans cette colonne")
            # Si le joueur ne peut pas jouer dans la colonne qu'il a sélectionnée, il doit en choisir une autre


def MinMax(iNextJoueur, npaGrilleCopy, iColonne=0, isFirst=False, tour=0):
    """
    Variables :
        iNextJoueur: Entier
        Resultat: Tableau de [0,...,iMaxColonne] entiers
        iBoucleTantQue: Entier
    """
    if tour > 4:
        return 0
    if not isFirst:
        # Si ce n'est pas le premier appel de la fonction, alors un coup doit être joué
        if VerifColonne(iColonne, npaGrilleCopy):
            # On doit être sûr de ne pas faire un coup illégal
            iLigne, iColonne = AjoutPiece(iNextJoueur, iColonne, npaGrilleCopy)
            if VictoireColonne(iLigne, iColonne, iNextJoueur, npaGrilleCopy) or \
                    VictoireLigne(iLigne, iColonne, iNextJoueur,
                                  npaGrilleCopy) or \
                    VictoireDiago(iLigne, iColonne, iNextJoueur, npaGrilleCopy):
                if iNextJoueur == 1:
                    # Si il y a une victoire, mais que c'est le joueur qui l'a obtenue, on renvoie -1
                    return -1
                else:
                    # Si c'est le bot qui l'a obtenue, on renvoie 1
                    return 1
        else:
            # Si aucun coup n'a pu être joué, on renvoie 0
            return 0

    # On inverse le prochain joueur
    if iNextJoueur == 1:
        iNextJoueur = 2
    else:
        iNextJoueur = 1

    Resultat = [0] * iMaxColonne

    for iBoucle in range(iMaxColonne):
        # On fait un appel pour chacune des colonnes du plateau pour jouer le prochain coup
        Resultat[iBoucle] = MinMax(iNextJoueur, npaGrilleCopy.copy(),
                                   iColonne=iBoucle, tour=tour + 1)

    if iNextJoueur == 2:
        if not isFirst:
            # Si ce n'est pas le premier appel, on renvoie le MAX de l'arbre
            return max(Resultat)
        else:
            # Si c'est le premier appel, on renvoie le coup à jouer pour le bot
            iBoucleTantQue = 0
            while Resultat[iBoucleTantQue] != max(Resultat):
                iBoucleTantQue += 1
            Jouer(2, iBoucleTantQue)
    else:
        # On renvoie le MIN de l'arbre si c'est le joueur qui a joué
        return min(Resultat)


def VerifColonne(iColonne, npaGrille):
    """
    Entree:
        iColonne: Entier
    Sortie:
        bResultat: Booleen
    Variable:
        npaGrille: Tableau de [0,...,iMaxLigne] 
            de Tableau de [0,...,iMaxColonne] Entiers
        iBoucle: Entier
        bResultat: Booleen
    """
    # Initialisation du booleen a faux
    bResultat = False
    global iMaxLigne
    # Pour chaque ligne de la grille
    for iBoucle in range(iMaxLigne):
        # bResultat recoit Vrai si la case est bien vide
        bResultat = bResultat or (npaGrille[iBoucle][iColonne] == 0)

    # Retourner le résultat
    return bResultat


def VictoireColonne(iLigne, iColonne, iJoueur, npaGrille):
    """
    Preconditions :
        AjoutPiece a été appelé
    Sortie:
        iWinner: Entier
    Variable :
        npaGrille: Tableau de [0,...,iMaxLigne] 
            de Tableau de [0,...,iMaxColonne] entiers
        iNbJetonVictoire: Entier
        iMaxLigne, iMaxColonne, iBoucle, iCompteur : Entier
        iWinnerDown, iWinnerUp, bVu, bSuite: Booleen
    """
    iNbJetonVictoire = 4  # Remplacez par la valeur correcte

    bWinnerDown = True
    bWinnerUp = True
    iCompteur = 0
    bVu = False
    bSuite = False

    if iLigne >= iNbJetonVictoire - 1:
        iDebut = iLigne - iNbJetonVictoire + 1
        iFin = iLigne + iNbJetonVictoire - 1

        if iDebut < 0:
            iDebut = 0

        if iFin > iMaxLigne:
            iFin = iMaxLigne

        for iBoucle in range(iDebut, iFin):
            if npaGrille[iBoucle][iColonne] == iJoueur and not bVu:
                bVu = True
                bSuite = True
                iCompteur = 1
            elif npaGrille[iBoucle][iColonne] == iJoueur and bSuite:
                iCompteur += 1
            elif npaGrille[iBoucle][iColonne] != iJoueur and bVu:
                bSuite = False

        return iCompteur >= iNbJetonVictoire
    else:
        return False


def VictoireDiago(iLigne, iColonne, iJoueur, npaGrille):
    """
    Preconditions :
        AjoutPiece a été appelé
    Sortie:
        Booleen
    Variable :
        npaGrille: Tableau de [0,...,iMaxLigne] 
            de Tableau de [0,...,iMaxColonne] entiers
        iNbJetonVictoire: Entier
        iMaxLigne: Entier
        iMaxColonne: Entier 
        iBoucle: Entier
        bWinner: Booleen
        bIsWinning: Booleen
    """
    iNbJetonVictoire = 4  # Remplacez par la valeur correcte

    bWinnerDown = True
    bWinnerUp = True
    iCompteur = 0
    bVu = False
    bSuite = False
    iCompteur2 = 0
    bVu2 = False
    bSuite2 = False

    if iLigne >= iNbJetonVictoire - 1:
        iDebutL = iColonne - iNbJetonVictoire + 1
        iFinL = iColonne + iNbJetonVictoire - 1

        if iDebutL < 0:
            iDebutL = 0

        if iFinL > iMaxLigne:
            iFinL = iMaxLigne

    if iColonne >= iNbJetonVictoire - 1:
        iDebutC = iColonne - iNbJetonVictoire + 1
        iFinC = iColonne + iNbJetonVictoire - 1

        if iDebutC < 0:
            iDebutC = 0

        if iFinC > iMaxColonne:
            iFinC = iMaxColonne

        for iBoucle in range(1, iFinC - iDebutC - 1):
            if npaGrille[iDebutL + iBoucle][iFinL - 1] == iJoueur and not bVu:
                bVu = True
                bSuite = True
                iCompteur = 1
            elif npaGrille[iDebutL + iBoucle][
                iFinL - iBoucle] == iJoueur and bSuite:
                iCompteur += 1
            elif npaGrille[iDebutL + iBoucle][
                iFinL - iBoucle] != iJoueur and bVu:
                bSuite = False

            if npaGrille[iFinL - iBoucle][
                iFinL - iBoucle] == iJoueur and not bVu2:
                bVu2 = True
                bSuite2 = True
                iCompteur2 = 1
            elif npaGrille[iFinL - iBoucle][
                iFinL - iBoucle] == iJoueur and bSuite2:
                iCompteur2 += 1
            elif npaGrille[iFinL - iBoucle][
                iFinL - iBoucle] != iJoueur and bVu2:
                bSuite2 = False

        return (iCompteur >= iNbJetonVictoire) or (
                    iCompteur2 >= iNbJetonVictoire)
    else:
        return False


def VictoireLigne(iLigne, iColonne, iJoueur, npaGrille):
    """
    Preconditions :
        AjoutPiece a été appelé
    Sortie:
        iWinner: Entier
    Variable :
        npaGrille: Tableau de [0,...,iMaxLigne] 
            de Tableau de [0,...,iMaxColonne] entiers
        iNbJetonVictoire: Entier
        iMaxLigne: Entier
        iMaxColonne: Entier 
        iBoucle, iCompteur: Entier
        bWinnerDown, bWinnerUp, bVu,bSuite: Booleen
    """
    iNbJetonVictoire = 4  # Remplacez par la valeur correcte

    bWinnerDown = True
    bWinnerUp = True
    iCompteur = 0
    bVu = False
    bSuite = False

    if iLigne >= iNbJetonVictoire - 1:
        iDebut = iColonne - iNbJetonVictoire + 1
        iFin = iColonne + iNbJetonVictoire - 1

        if iDebut < 0:
            iDebut = 0

        if iFin > iMaxColonne:
            iFin = iMaxColonne

        for iBoucle in range(iDebut, iFin):
            if npaGrille[iLigne][iBoucle] == iJoueur and not bVu:
                bVu = True
                bSuite = True
                iCompteur = 1
            elif npaGrille[iLigne][iBoucle] == iJoueur and bSuite:
                iCompteur += 1
            elif npaGrille[iLigne][iBoucle] != iJoueur and bVu:
                bSuite = False

        return iCompteur >= iNbJetonVictoire
    else:
        return False


iMaxLigne = 6
iMaxColonne = 7

GestionPartie(6, 7, np.array([[0] * 7] * 6))
