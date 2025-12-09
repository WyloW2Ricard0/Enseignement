- crée un nouveau répertoire nommé : `mkdir <nom du projet>`
- change le répertoire `cd mon-projet`
installez via `winget` si disponible. winget est l’outil de gestion de paquets natif pour Windows — il permet une installation automatisée et reproducible depuis la ligne de commande, pratique pour les scripts ou les environnements d’entreprise. Note : winget nécessite l’App Installer et une version récente de Windows.
Changez le propriétaire du répertoire pour que ce soit vous : `takeown /F PATH_PROJET /R /D Y`puis `icacls "C:heminersepot"`