---
versions: 1.0.0
effectiveDate: 2025-12-18
author: RICHARD Wilfried

title: Markdown : l’essentiel
intro: Guide pratique pour comprendre et utiliser la syntaxe Markdown.
type: guide
topics:
  - markdown
  - html
  - écriture
  - documentation
image: "https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg"
---

# Markdown : l’essentiel

Markdown est une syntaxe de mise en forme de texte simple et un outil permettant de convertir ce texte en HTML valide. Il est conçu pour être lisible en texte brut et facilement publiable.

## Pourquoi utiliser Markdown ?
- Écrire des documents clairs, lisibles et convertibles en HTML sans balises complexes.
- Publier du texte brut qui reste structuré et facile à lire.

### Installation
- Nécessite Perl 5.6.0+ et le module Digest::MD5 (souvent préinstallé).
- Téléchargez Markdown sur https://daringfireball.net/projects/markdown/

### Utilisation
- Markdown fonctionne avec de nombreux outils et éditeurs (Movable Type, Blosxom, BBEdit, etc.).
- Pour l’utiliser, copiez le fichier Markdown.pl dans le dossier approprié de votre outil ou éditeur.
- La conversion se fait automatiquement lors de la publication ou via la ligne de commande.

### Configuration
- Par défaut, Markdown produit du XHTML. Pour générer du HTML4, utilisez l’option `output='html4'` ou le commutateur `--html4tags` en ligne de commande.

### Ressources utiles
- [Syntaxe Markdown](http://daringfireball.net/projects/markdown/syntax)
- [Source et documentation](http://daringfireball.net/projects/markdown/index.text)
- [Licence BSD](http://daringfireball.net/projects/markdown/license)
