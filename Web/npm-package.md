---
versions: 1.0.0
effectiveDate: 2025-12-19
author: RICHARD Wilfried

title: package.json : l’essentiel
excerpt: Guide pratique pour comprendre et rédiger un fichier package.json pour Node.js/npm.
type: guide
topics:
  - npm
  - nodejs
  - package.json
  - configuration
image: "https://upload.wikimedia.org/wikipedia/commons/d/db/Npm-logo.svg"
---

# package.json : l’essentiel

Le fichier package.json décrit un projet Node.js/npm. Il doit être au format JSON.

## Champs principaux

- **name** : nom du paquet (obligatoire si publication)
- **version** : version du paquet (obligatoire si publication)
- **description** : courte description
- **keywords** : mots-clés (tableau de chaînes)
- **author** / **contributors** : auteur et contributeurs
- **license** : licence (ex : "MIT", "ISC", "UNLICENSED")
- **repository** : URL du dépôt (ex : GitHub)
- **homepage** : page d’accueil du projet
- **bugs** : suivi des bugs (URL/email)
- **funding** : financement (URL)
- **main** : point d’entrée principal (ex : "index.js")
- **bin** : exécutables CLI
- **scripts** : scripts npm (ex : start, test, build)
- [dependencies](#dependencies) : dépendances à installer en production
- **devDependencies** : dépendances de développement
- **peerDependencies** : dépendances à installer par l’utilisateur final
- **optionalDependencies** : dépendances optionnelles
- **engines** : versions de Node/npm requises
- **private** : true pour empêcher la publication
- **files** : fichiers à inclure lors de la publication
- **workspaces** : gestion de monorepo

### Exemples
```json
{
  "name": "mon-projet",
  "version": "1.0.0",
  "description": "Un exemple de package.json minimal",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "echo \"Pas de test\""
  },
  "author": "Nom <email@exemple.com>",
  "license": "MIT",
  "dependencies": {
    "express": "^4.18.0"
  },
  "devDependencies": {
    "nodemon": "^2.0.0"
  }
}
```

### Bonnes pratiques
- Garder le fichier valide (utiliser un validateur JSON)
- Mettre à jour la version à chaque modification majeure
- Utiliser des scripts pour automatiser les tâches
- Préciser la licence et le dépôt

## dependencies

La **plage de versions** est une chaîne qui possède un ou plusieurs descripteurs séparés par espace.

Les dépendances peuvent ***également être identifiées par une URL tarball ou git***.


### Signification des opérateurs de version

Par exemple, toutes ces éléments sont valides :

```json
{
  "dependencies": {
    "foo": "1.0.0 - 2.9999.9999", // accepte toute version comprise entre inclus.
    "bar": ">=1.0.2 <2.1.2", 
    "baz": ">1.0.2 <=2.3.4",
    "boo": "2.0.1", //exactement la version
    "qux": "<1.0.0 || >=2.3.1 <2.4.5 || >=2.5.2 <3.0.0", // ou
    "asd": "http://asdf.com/asdf.tar.gz", //installe le paquet depuis une URL tarball
    "til": "~1.2", // accepte la dernière version mineure compatible
    "elf": "~1.2.3", //  accepte la dernière version correctif compatible
    "two": "2.x", // accepte toute version majeure
    "thr": "3.3.x",
    "lat": "latest", // installe la dernière version publiée.
    "dyl": "file:../dyl", // installe depuis un dossier local
    "kpg": "npm:pkg@1.0.0" //  alias pour installer un autre paquet npm à une version précise
  }
}
```

---
*Voir la [documentation officielle](https://docs.npmjs.com/cli/v10/configuring-npm/package-json?v=true#urls-as-dependencies) npm pour plus de détails sur chaque champ.*