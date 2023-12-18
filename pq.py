import numpy as np
iNbJetonVictoire = 4

def MinMax(iNextJoueur, npaGrilleCopy, iColonne = 0, isFirst = False, turn = 0):
    global iNbJetonVictoire
    if turn > 3:
        return 0
    if not(isFirst):
    #Si ce n'est pas le premier appel de la fonction, : un coup doit être joué
        if VerifColonne(iColonne,npaGrilleCopy) :
            #On doit être sûr de ne pas Faire un coup illégal
            (iLigne,iColonne,npaGrilleCopy) = AjoutPiece(iNextJoueur, iColonne, npaGrilleCopy)
            if VictoireColonne(iLigne, iColonne,iNextJoueur, npaGrilleCopy) or VictoireLigne(iLigne, iColonne,iNextJoueur, npaGrilleCopy) or VictoireDiablo(iLigne, iColonne,iNextJoueur, npaGrilleCopy) :
                    if iNextJoueur == 1 :
                        #Si il y a une victoire, mais que c'est le joueur qui l'a obtenu, on renvoit -1
                        return -1
                    else:
                        #Si c'est le bot qui l'a obtenu, on renvoit 1
                        return 1
        else:
            #Si aucun coup n'a pu être joué, on renvoit 0
            return 0
    #On inverse le prochain joueur
    if iNextJoueur == 1 :
        iNextJoueur = 2
    else:
        iNextJoueur = 1
    Resultat = []
    for iBoucle in range (iMaxColonne): 
        #On fait un appel pour chacune des colonnes du plateau pour jouer le prochain coup
        n = MinMax(iNextJoueur, npaGrilleCopy.copy(), iColonne = iBoucle, turn = turn + 1)
        if n == None:
            n = 0
        Resultat.append(n)
    if iNextJoueur == 2 :
        if not(isFirst) :
            #Si il ne s'agit pas du premier appel, on renvoit le MAX de l'arbre
            return max(Resultat)
        else:
            #Si il s'agit du premier appel, : on renvoit le coup à jouer pour le bot
            iBoucleTantQue = 0
            while (Resultat[iBoucleTantQue] != max(Resultat)):
                iBoucleTantQue = iBoucleTantQue + 1
            AjoutPiece(2,iBoucleTantQue,npaGrille)
        #On renvoit le MIN de l'arbre si c'est le joueur qui a joué.
        return min(Resultat)

def VictoireLigne(iLigne,iColonne, iJoueur, npaGrille):
    global iNbJetonVictoire
    bWinnerDown = True
    bWinnerUp = True
    iCompteur = 0
    bVu = False
    bSuite = False
    if iLigne >= iNbJetonVictoire-1 :
        iDebut = iColonne - iNbJetonVictoire-1
        iFin = iColonne + iNbJetonVictoire-1
        if iDebut < 0 :
            iDebut = 0
        if iFin > iMaxColonne :
            iFin = iMaxColonne
        for iBoucle in range (iDebut, iFin):
            if npaGrille[iLigne][iBoucle] == iJoueur and not(bVu) :
                bVu = True
                bSuite = True
                iCompteur = 1
            elif npaGrille[iLigne][iBoucle] == iJoueur and bSuite :
                iCompteur = iCompteur + 1
            elif npaGrille[iLigne][iBoucle] != iJoueur and bVu :
                bSuite = False
        return iCompteur >= iNbJetonVictoire
    else:
        return False

def VictoireDiablo(iLigne, iColonne, iJoueur, npaGrille):
    global iNbJetonVictoire
    bWinnerDown = True
    bWinnerUp = True
    iCompteur = 0
    bVu = False
    bSuite = False
    iCompteur2 = 0
    bVu2 = False
    bSuite2 = False
    if iLigne >= iNbJetonVictoire-1 :
        iDebutL = iColonne - iNbJetonVictoire-1
        iFinL = iColonne + iNbJetonVictoire-1
        if iDebutL < 0 :
            iDebutL = 0
        if iFinL > iMaxLigne :
            iFinL = iMaxLigne
    if iColonne >= iNbJetonVictoire-1 :
        iDebutC = iColonne - iNbJetonVictoire-1
        iFinC = iColonne + iNbJetonVictoire-1
        if iDebutC < 0 :
            iDebutC = 0
        if iFinC > iMaxColonne :
            iFinC = iMaxColonne
        for iBoucle in range (iFinC-iDebutC):
            if npaGrille[iDebutC+iBoucle][iFinC-1] == iJoueur and not(bVu) :
                bVu = True
                bSuite = True
                iCompteur = 1
            elif npaGrille[iDebutC+iBoucle][iFinC-iBoucle] == iJoueur and bSuite :
                iCompteur = iCompteur + 1
            elif npaGrille[iDebutC+iBoucle][iFinC-iBoucle] != iJoueur and bVu :
                bSuite = False
            if npaGrille[iFinC-iBoucle][iFinC-iBoucle] == iJoueur and not(bVu2) :
                bVu2 = True
                bSuite2 = True
                iCompteur2 = 1
            elif npaGrille[iFinC-iBoucle][iFinC-iBoucle] == iJoueur and bSuite2 :
                iCompteur2 = iCompteur + 1
            elif npaGrille[iFinC-iBoucle][iFinC-iBoucle] != iJoueur and bVu2 :
                bSuite2 = False
        return (iCompteur >= iNbJetonVictoire) or (iCompteur2 >= iNbJetonVictoire)
    else:
        return False

def VictoireColonne(iLigne, iColonne, iJoueur, npaGrille):
    global iNbJetonVictoire
    bWinnerDown = True
    bWinnerUp = True
    iCompteur = 0
    bVu = False
    bSuite = False
    if iLigne >= iNbJetonVictoire-1:
        iDebut = iLigne - iNbJetonVictoire-1
        iFin = iLigne + iNbJetonVictoire-1
        if iDebut < 0:
            iDebut = 0
        if iFin > iMaxLigne:
            iFin = iMaxLigne
        for iBoucle in range (iDebut, iFin):
            if npaGrille[iBoucle][iColonne] == iJoueur and not(bVu):
                bVu = True
                bSuite = True
                iCompteur = 1
            elif npaGrille[iBoucle][iColonne] == iJoueur and bSuite:
                iCompteur = iCompteur + 1
            elif npaGrille[iBoucle][iColonne] != iJoueur and bVu:
                bSuite = False
        return iCompteur >= iNbJetonVictoire
    else:
        return False

def AjoutPiece(iColonne, iJoueur, npaGrille):
    # Initialisation du compteur de boucle
    iBoucle = 0
    # Tant que la case de la grille de notre colonne est vide
    while (iBoucle < iMaxLigne and npaGrille[iBoucle][iColonne] == 0):
        # Augmenter le compteur de compteur de boucle
        iBoucle = iBoucle + 1
    # Ajouter le jeton du joueur dans la derniere case vide
    npaGrille[iBoucle-1][iColonne] = iJoueur
    # return un tuple des coordonnées du nouveau jeton
    return (iBoucle-1, iColonne, npaGrille)

def VerifColonne(iColonne, npaGrille):
    #Initialisation du booleen a faux
    bResultat = False
    # Pour chaque ligne de la grille
    for iBoucle in range (iMaxLigne):
        # bResultat recoit Vrai si la case est bien vide
        bResultat = bResultat or (npaGrille[iBoucle][iColonne] == 0)
    # return le resultat
    return bResultat

def GestionPartie(iMaxLigne, iMaxColonne, npaGrille):
    global iNbJetonVictoire
    iBoucle = 0
    bVictoire = False
    while (iBoucle < ((iMaxLigne*iMaxColonne)/2) and not(bVictoire)): 
        #Les tours de boucles s'effectue jusqu'à ce qu'il ne reste plus de coup à jouer.
        iColonneJoueur = int(input("Quelle colonne jouer. "))
        if VerifColonne(iColonneJoueur, npaGrille) :
            #On vérifie si le joueur peut jouer dans la colonne qu'il a selectionné
            (iLigneJoueur,iColonneJoueur,npaGrille) = AjoutPiece(iColonneJoueur,1,npaGrille)
            if VictoireColonne(iLigneJoueur, iColonneJoueur, 1, npaGrille) or VictoireLigne(iLigneJoueur,iColonneJoueur, 1, npaGrille) or VictoireDiablo(iLigneJoueur,iColonneJoueur, 1, npaGrille):
                #Vérification de la victoire

                print("Le joueur 1 a gagné !")
                bVictoire = True
            else:
                iColonneBot = MinMax(2, npaGrille, isFirst = True)
                #On appelle MinesMax pour savoir dans quel colonne le bot va jouer
                (iLigneBot,iColonneBot,npaGrille) = AjoutPiece(iColonneBot,1,npaGrille)
                if VictoireColonne(iLigneBot, iColonneBot, npaGrille) or VictoireLigne(iLigneBot,iColonneBot, npaGrille) or VictoireDiablo(iLigneBot,iColonneBot, npaGrille):
                    #Vérification de la victoire
                    
                    print("Le joueur 2 a gagné !")
                    bVictoire = Vrai
            tUndoRedo[iBoucle] = npaGrille
            iBoucle = iBoucle + 1
            print(npaGrille)
        else:
            print("Vous ne pouvez pas jouer dans cette colonne")
            #Si le joueur ne peut pas jouer dans la colonne qu'il a selectionné, il doit en choisir une autre
            
iMaxColonne = 7
iMaxLigne = 6
npaGrille = np.array([[0]*iMaxColonne]*iMaxLigne)
print(np.shape(npaGrille))
GestionPartie(iMaxLigne, iMaxColonne, npaGrille)
