@echo off

REM On vérifie qu'il y a bien python d'installé
python --version >nul 2>&1
if errorlevel 1 (
    echo Python n'est pas installé.
    exit /b
)

REM On vérifie qu'il y a bien venv d'installé
python -c "import venv" >nul 2>&1
if errorlevel 1 (
    python -m pip install virtualenv
    if errorlevel 1 (
        echo Une erreur s'est produite lors de l'installation de venv.
        exit /b
    )
)


REM On vérifie si le venv existe déjà
if exist venv (
    echo Le venv existe deja.
) else (
    REM On crée le venv
    python -m venv venv
)


REM On l'active
call venv/Scripts/activate.bat

REM On vérifie qu'il y a bien pip d'installé
pip --version >nul 2>&1
if errorlevel 1 (
  echo "pip is not installed"
  exit /b
)

REM On met à jour pip
python -m pip install --upgrade pip

REM On installe les dépendances
pip install -r requirements.txt

REM On demande à l'utilisateur s'il veut lancer le jeu en ligne de commande ou avec l'interface graphique
set /p UserInput=Voulez-vous lancer le jeu en ligne de commande (C) ou avec l'interface graphique (G) ?

if /I "%UserInput%"=="C" (
    REM On lance le jeu en ligne de commande
    python main.py -cli
) else if /I "%UserInput%"=="G" (
    REM On lance le jeu avec l'interface graphique
    python main.py -gui
)