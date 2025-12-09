#!/usr/bin/env python3
"""Script d'initialisation Git pour le projet Enseignement."""

import subprocess
import sys
from Data.variable import (
    GIT_USER_NAME,
    GIT_USER_EMAIL,
    GIT_EDITOR_VSCODE,
    URL_DEPOT_DISTANT,
    REMOTE_DEFAUT,
    PATH_PROJET
)

def run_command(cmd, check=True):
    """Exécute une commande shell et affiche la sortie."""
    print(f"-> {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True, check=check)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result

def setup_git():
    """Configure Git avec les paramètres du projet."""
    print("Configuration de Git...")
    
    # Configuration globale
    run_command(["git", "config", "--global", "user.name", GIT_USER_NAME])
    run_command(["git", "config", "--global", "user.email", GIT_USER_EMAIL])
    run_command(["git", "config", "--global", "core.editor", GIT_EDITOR_VSCODE])
    
    # Ajouter safe.directory si nécessaire
    run_command(["git", "config", "--global", "--add", "safe.directory", PATH_PROJET], check=False)
    
    # Vérifier si le remote existe
    result = run_command(["git", "remote", "get-url", REMOTE_DEFAUT], check=False)
    if result.returncode != 0:
        print(f"Ajout du remote '{REMOTE_DEFAUT}'...")
        run_command(["git", "remote", "add", REMOTE_DEFAUT, URL_DEPOT_DISTANT])
    else:
        print(f"Remote '{REMOTE_DEFAUT}' déjà configuré.")
    
    print("\n✅ Configuration Git terminée !")
    print(f"   User: {GIT_USER_NAME} <{GIT_USER_EMAIL}>")
    print(f"   Remote: {REMOTE_DEFAUT} -> {URL_DEPOT_DISTANT}")

if __name__ == "__main__":
    setup_git()
