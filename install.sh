#!/bin/bash

# On vérifie qu'il y a bien python d'installé
if ! command -v python3 &> /dev/null
then
    echo "Python n'est pas installé."
    exit
fi

# On vérifie qu'il y a bien venv d'installé
if ! python3 -c "import venv" &> /dev/null
then
    echo "venv n'est pas installé."
    python3 -m pip install virtualenv
    if [ $? -ne 0 ]; then
        echo "Une erreur s'est produite lors de l'installation de venv."
        exit
    fi
fi

# On vérifie si le venv existe déjà
if [ ! -d "venv" ]; then
    # On crée le venv
    python3 -m venv venv
else
    echo "Le venv existe deja."
fi

# On l'active
source venv/bin/activate

# On vérifie qu'il y a bien pip d'installé
if ! command -v pip &> /dev/null
then
    echo "pip is not installed"
    exit
fi

# On met à jour pip
python3 -m pip install --upgrade pip

# On installe les dépendances
pip install -r requirements.txt

# On demande à l'utilisateur s'il veut lancer le jeu en ligne de commande ou avec l'interface graphique
read -p "Voulez-vous lancer le jeu en ligne de commande (C) ou avec l'interface graphique (G) ? " UserInput
if [ "$UserInput" = "C" ]; then
    # On lance le jeu en ligne de commande
    python3 main.py -cli
elif [ "$UserInput" = "G" ]; then
    # On lance le jeu avec l'interface graphique
    python3 main.py -gui
fi