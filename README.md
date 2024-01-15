## ProjetApplicationConceptionLogicielle
Lors de ce projet, nous devons réaliser un puissance 4. Cependant, ce puissance 
4 sera amélioré, les joueurs pourront changer la taille de la grille et le 
nombre de jetons requis pour gagner.

De plus, le joueur aura des bonus permettant de renverser la partie ou de se 
donner un avantage, par exemple, il pourra avoir une bombe pour supprimer une 
ligne ou une colonne, ou alors retourner la grille.
Nous allons aussi apporter de la personnalisation au joueur, il pourra changer 
la couleur des jetons et de la grille.

Ce projet se divise en trois parties : l’algorithmie, le génie logiciel ainsi 
que la réalisation de l’interface graphique. Ces trois parties sont essentielles
à ce projet.

## Modules externes utilisés :
* [Numpy](https://numpy.org)
* [Inspect](https://docs.python.org/3/library/inspect.html)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [argparse](https://docs.python.org/3/library/argparse.html)

## Installation
* Pour installer le jeu, il suffit de cloner le dépôt git avec la commande suivante :
```bash
git clone https://github.com/matteolanglois/projetApplicationConceptionLogicielle.git
```
* Ensuite, il faut se placer dans le dossier du jeu :
```bash
cd projetApplicationConceptionLogicielle
```
* Enfin, il faut installer les modules externes utilisés :
```bash
pip3 install -r requirements.txt
```

## Installation bis
* Après avoir cloné le dépôt git et vous être placé dans le dossier du jeu, il est possible 
d'exécuter le fichier install.bat (si vous êtes sous windows) ou install.sh (si vous êtes sous linux)
* Ce fichier va installer les modules externes utilisés et lancer le jeu.

## Lancement
* Pour lancer le jeu, il suffit de lancer le fichier `main.py` avec python3.
* Si vous lancez le jeu avec l'argument '--cli', le jeu se lancera en ligne de commande.
* Si vous lancez le jeu sans argument, le jeu se lancera avec l'interface graphique.

_____________________
## Fonctionnalités
### Algorithmie
- [x] Vérification de la victoire
- [x] Vérification de la jouabilité
- [x] Algorithme MinMax
- [x] Ajout de pièce
- [x] Algorithme de gestion de partie en ligne de commande
- [x] Implémentation du undo/redo

### Interface graphique
- [x] Page d'accueil
- [x] Page de paramètres
- [x] Sauvegarde des paramètres
- [x] Page de jeu
- [x] Affichage de la grille
- [x] Affichage des jetons
- [x] Utilisation des bonus
- [x] Affichage de la victoire/Défaite
- [ ] Affichage de l'aide
- [x] Affichage du tour du joueur
- [x] Interface responsive

### Personnalisation
- [x] Personnalisation des jetons
- [x] Personnalisation de la couleur de la grille
- [x] Personnalisation de la taille de la grille
- [x] Personnalisation du nombre de jetons à aligner pour gagner
- [x] Personnalisation de la difficulté de l'IA

### Bonus
- [x] Utilisation des bonus en ligne de commande
- [x] Utilisation des bonus dans la fenêtre
- [x] Bonus d'inversion de la grille
- [x] Bonus de suppression de ligne pleine
- [x] Bonus d'aide avec MinMax
- [x] Bonus de retournement de la grille

_____________________
## Expliquation du code
### Documentation
* La documentation du code se trouve dans le dossier `docs` à la racine du projet.
* Elle peut être générée avec Doxygen, le fichier de configuration doxyFile se trouve à la racine du projet.
* Pour générer la documentation, il suffit de lancer la commande suivante :
```bash
doxygen doxyFile
```

### Convention de nommage
* Les variables et fonctions sont nommées en snake_case.
* Les fonctions commencent par un acronyme désignant le fichier et le module dans lequel elles se trouvent.
* Les noms de variables commencent par leur type :
  * `b_` pour les booléens
  * `i_` pour les entiers
  * `f_` pour les flottants
  * `s_` pour les chaînes de caractères
  * `t_` pour les listes
  * `t_` pour les tuples
  * `npa_` pour les tableaux numpy
  * `tkl_` pour les labels tkinter
  * `tkb_` pour les boutons tkinter
  * `tkc_` pour les canvas tkinter
  * `tksb_` pour les spinbox tkinter
  * `tkf_` pour les frames tkinter
  * `tks_` pour les scales tkinter
  * `tksv_` pour les stringvar tkinter