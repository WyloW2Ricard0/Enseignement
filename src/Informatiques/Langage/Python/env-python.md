---
title: Environnements et automatisation Python
intro: Guide pratique pour gérer les bibliothèques, variables d’environnement et automatiser avec Python.
type: guide
topics:
  - python
  - environnement
  - automatisation
  - pip
  - dotenv
image: "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"

versions: 1.0.0
effectiveDate: 2025-12-13
author: RICHARD Wilfried
---
## Utilisation

### Bibliotheque

```shell
#installation d'une bibliothèque Python via pip
!pip install "BIBLIOTHEQUE_NAME"

# Mise à jour d'une bibliothèque Python via pip
python -m pip install --upgrade "BIBLIOTHEQUE_NAME"
```

### Recupere une variable d'environement

```shell
# 
!pip install python-dotenv
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Cré une variable d'environement
CONSTANTa = os.getenv("CONSTANT_NAME", "CONSTANT_VALEUR")

# Si la constant est dejat dans .env
CONSTANTb = os.getenv("CONSTANT_NAME")
```

## Exemple d'automatisation

exemple Exécution powershell : python Data/setup_git.py

## Ressources
- [GitPython — Bibliothèque Git pour Python](https://gitpython.readthedocs.io/)
- [python-dotenv — Gestion de variables d'environnement](https://pypi.org/project/python-dotenv/)
- [subprocess — Documentation Python](https://docs.python.org/3/library/subprocess.html)