
## 🤝 Contribution

<!-- 
Cette section explique comment les autres peuvent contribuer.
Soyez clair sur le processus et accueillant pour les débutants.
-->

Les contributions sont **fortement encouragées** ! Ce dépôt est ouvert aux suggestions, corrections, ajouts de contenu, traductions, etc.

### Comment contribuer ?

#### Méthode 1 : Issues (signaler un problème ou suggérer une amélioration)

1. Aller dans l'onglet [Issues](https://github.com/WyloW2Ricard0/Enseignement/issues)
2. Cliquer sur **New Issue**
3. Choisir un template ou décrire votre suggestion
4. Soumettre

**Exemples de contributions via Issues :**
- ❌ Signaler une erreur (typo, commande incorrecte, lien mort)
- 💡 Proposer un nouveau sujet (ex: "Ajouter guide GitHub Actions")
- 🌍 Proposer une traduction (ex: "Traduire README en anglais")
- ❓ Poser une question sur le contenu

#### Méthode 2 : Pull Requests (proposer des modifications directes)

<!--
Workflow Git standard pour contributions.
Expliquez chaque étape clairement pour les débutants.
-->

1. **Forker le dépôt**
   - Cliquer sur le bouton **Fork** en haut à droite sur GitHub
   - Cela crée une copie du dépôt sur votre compte

2. **Cloner votre fork localement**
   ```powershell
   git clone https://github.com/VOTRE_USERNAME/Enseignement.git
   cd Enseignement
   ```

3. **Créer une branche pour vos modifications**
   ```powershell
   git checkout -b feature/ma-contribution
   # Nommage suggéré :
   # - feature/nom-fonctionnalite (nouvelle fonctionnalité)
   # - fix/description-bug (correction de bug)
   # - docs/sujet (amélioration documentation)
   # - refactor/description (refactorisation)
   ```

4. **Faire vos modifications**
   - Éditer les fichiers concernés
   - Tester que tout fonctionne
   - Respecter le style existant

5. **Committer vos changements**
   ```powershell
   git add .
   git commit -m "feat: Ajoute guide sur SSH pour Git"
   # Préfixes conventionnels :
   # feat: nouvelle fonctionnalité
   # fix: correction bug
   # docs: documentation
   # style: formatage
   # refactor: refactorisation
   # test: ajout tests
   # chore: maintenance
   ```

6. **Pousser vers votre fork**
   ```powershell
   git push origin feature/ma-contribution
   ```

7. **Ouvrir une Pull Request**
   - Aller sur GitHub → votre fork
   - Cliquer sur **Compare & pull request**
   - Remplir le formulaire :
     - **Titre** : Résumé clair (ex: "Ajoute guide SSH")
     - **Description** : Détails des changements, motivation, captures d'écran si pertinent
   - Soumettre

8. **Répondre aux retours**
   - Un mainteneur examinera votre PR
   - Répondre aux commentaires et faire les ajustements demandés
   - Une fois approuvée, la PR sera fusionnée 🎉

### Règles de contribution

<!--
Définissez des règles claires mais pas restrictives.
Le but est de faciliter la contribution, pas de décourager.
-->

✅ **À faire :**
- Vérifier qu'une issue/PR similaire n'existe pas déjà
- Tester vos modifications avant de soumettre
- Écrire des messages de commit clairs
- Documenter les nouveaux fichiers/fonctionnalités
- Respecter le [Code de Conduite](CODE_OF_CONDUCT.md)

❌ **À éviter :**
- Commits avec des fichiers non pertinents (node_modules, .DS_Store, etc.)
- Modifications massives sans discussion préalable
- Copier-coller de contenu sous copyright sans attribution
- Ton irrespectueux ou commentaires offensants

### Types de contributions recherchées

<!--
Guidez les contributeurs vers les besoins prioritaires.
-->

| Type | Exemples | Priorité |
|------|----------|----------|
| 🐛 **Corrections** | Typos, liens morts, commandes incorrectes | ⭐⭐⭐ Haute |
| 📝 **Documentation** | Clarifier sections, ajouter exemples | ⭐⭐⭐ Haute |
| ✨ **Nouveaux contenus** | Guide SSH, CI/CD, workflows avancés | ⭐⭐ Moyenne |
| 🌍 **Traductions** | Traduire README/guides en anglais | ⭐⭐ Moyenne |
| 🎨 **Améliorations visuelles** | Diagrammes, captures d'écran, badges | ⭐ Basse |

### Reconnaissance des contributeurs

Tous les contributeurs seront listés dans la section [Remerciements](#-remerciements) du README. Pour les contributions majeures, possibilité d'être ajouté comme co-mainteneur.
