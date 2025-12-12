# Standards de structuration de répertoires — Cours pratique

Ce cours présente les bonnes pratiques et standards reconnus pour organiser les répertoires d'un projet logiciel, améliorer la maintenabilité et faciliter la collaboration.

**Avantages :**
- Navigation intuitive
- Maintenance simplifiée
- Onboarding rapide pour nouveaux contributeurs

## Principes fondamentaux

### Règles générales

- Préférez **lowercase** pour compatibilité entre OS (Windows insensible à la casse, Linux/macOS sensibles)
- Évitez espaces, accents, caractères spéciaux
- Utilisez tirets (`-`) ou underscores (`_`) pour séparer les mots

### 🎯 Règles d'or

1. **Un fichier = une responsabilité**
2. **Un dossier = un domaine fonctionnel**
3. **Pas de code dans la racine** (sauf point d'entrée minimal)
4. **Documentation proche du code** qu'elle documente
5. **Tests mirrorent la structure** du code source
6. **Configuration séparée** du code
7. **Secrets jamais committés**
8. **Build artifacts toujours ignorés**

### Conventions de nommage

- Dossier : lowercase le tout au pluriel
- Fichiers : kebab-case
- Interfaces : PascalCase préfixe `I`
- Classes : PascalCase
- Fonctions : camelCase avec un verbe d'action
- Variables : snake_case au singulier
- Constants :  UPPERCASE Descriptives
- **Variables booléennes** : Préfixer par `is_`

## Checklist complète de structure de projet

### ✅ Fichiers obligatoires à la racine

- [ ] **📄 README.md** — Documentation principale du projet
- [ ] **📜 LICENSE** — Licence du projet
- [ ] 🤝 CONTRIBUTING.md
- [ ] 📋 CHANGELOG.md
- [ ] **🚫 .gitignore** — Exclusions Git
- [ ] **.editorconfig** — Configuration IDE
    - Indentation (spaces/tabs)
    - Charset (UTF-8)
    - Fin de ligne (LF/CRLF)
    - Trim trailing whitespace
- [ ] **.env.example** — Template variables d'environnement
    - Variables nécessaires documentées
    - Valeurs d'exemple (non sensibles)
    - Instructions de configuration
- [ ] **docker-compose.yml** — Environnement conteneurisé
    - Services nécessaires (DB, cache, etc.)
    - Configuration développement
    - Volumes et réseaux
- [ ] **📦 Fichiers de dépendances** (selon langage)
    - Python: `requirements.txt`, `pyproject.toml`
    - Node.js: `package.json`, `package-lock.json`
    - Java: `pom.xml`, `build.gradle`
    - Rust: `Cargo.toml`
    - Go: `go.mod`, `go.sum`
- [ ] `src/` — Code source principal
    - main.py              # Point d'entrée (`main.py`, `index.js`, `main.go`)
    - config/              # Configuration applicative
    - models/              # Modèles de données
    - controllers/         # Contrôleurs/handlers
    - services/            # Logique métier
    - utils/               # Utilitaires génériques
    - middleware/          # Middleware (web apps)
- [ ] `tests/` — Tests automatisés
    - unit/                # Tests unitaires
        - test_models.py
        - test_utils.py
    - integration/         # Tests d'intégration
        - test_api.py
    -  e2e/                 # Tests end-to-end
        - test_workflows.py
    - fixtures/            # Données de test
    - conftest.py          # Configuration pytest
- [ ] `docs/` — Documentation technique
    - architecture.md      # Vue d'ensemble système
    - api.md              # Documentation API
    - deployment.md       # Guide déploiement
    - database.md         # Schéma base de données
    - adr/                # Architecture Decision Records
        - 001-choix-database.md
- [ ] `configs/` — Configuration applicative
    - default.yaml         # Configuration par défaut
    - development.yaml     # Config développement
    - staging.yaml         # Config staging
    - production.yaml      # Config production
    - logging.yaml         # Configuration logs
- [ ] `scripts/` — Scripts d'automatisation
    -  setup.sh             # Installation initiale
    -  build.sh             # Build du projet
    -  deploy.sh            # Déploiement
    -  migrate.sh           # Migrations DB
    -  seed-data.sh         # Données initiales
- [ ] `data/` — Données du projet
    - Données d'exemple non sensibles
    - Fichiers de seed pour tests
    - Datasets de démonstration
    - Fixtures pour développement
    - **⚠️ JAMAIS de données sensibles ou personnelles**
- [ ] `public/` — Assets publics (web)
    - asset/                # Fichiers statiques
        - Images, icônes, favicon
        - Fichiers téléchargeables
        - Articles de blog (YYYY-MM-DD-titre.md)
    - components/           # Composants réutilisables
    - pages/                # Pages de l'application
    - hooks/                # Hooks personnalisés
        - atoms/
        - molecules/
        - organismes/
        - templates/
        - layouts/
    - styles/               # Fichiers de style CSS/SCSS, Polices de caractères
    - App.jsx               # Composant principal
    - index.jsx             # Point d'entrée
- [ ] `build/` — Artefacts compilés
    - Code compilé/transcompilé
    - Bundles JavaScript minifiés
    - Fichiers de distribution
    - Packages prêts au déploiement
    - **⚠️ Toujours dans `.gitignore`**

### 🚨 Vérifications de sécurité

- [ ] **`.env` dans `.gitignore`** — Pas de secrets committés
- [ ] **Pas de clés API en dur** dans le code
- [ ] **Pas de mots de passe** dans les fichiers de config
- [ ] **Credentials dans variables d'environnement** uniquement
- [ ] **Scanner les secrets** avec tools (git-secrets, trufflehog)
- [ ] **Dépendances à jour** (vulnérabilités connues)
- [ ] **Lockfiles committés** (sécurité reproductible)

## Ressources

### Standards et guides officiels

- [Python Packaging User Guide](https://packaging.python.org/)
- [Node.js Best Practices](https://github.com/goldbergyoni/nodebestpractices)
- [The Twelve-Factor App](https://12factor.net/) (applications cloud-native)
- [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines)

### Outils

- **cookiecutter** : Générateurs de templates de projets (Python, JS, etc.)
- **yeoman** : Générateur d'applications web
- **Scaffold** : Templates de projets prêts à l'emploi

## Conclusion

Une bonne structure de répertoires :
- **Facilite la collaboration** : Nouveaux contributeurs comprennent rapidement le projet
- **Améliore la maintenabilité** : Trouver et modifier du code devient intuitif
- **Réduit les erreurs** : Séparation claire entre code, tests, configuration
- **Professionnalise le projet** : Démontre rigueur et bonnes pratiques

**Règle d'or :** Suivez les conventions de votre écosystème, adaptez selon vos besoins, documentez les choix non standards.
