
## Exercices pratiques

### Exercice 1 : Auditer un projet existant

1. Clonez un projet open source sur GitHub
2. Analysez sa structure de répertoires
3. Identifiez :
   - Les standards suivis
   - Les anti-patterns présents
   - Les améliorations possibles

### Exercice 2 : Restructurer un projet désordonné

Soit le projet suivant :
```
mon_projet/
├── code.py
├── code_old.py
├── test.py
├── data.csv
├── config.txt
└── readme.txt
```

**Mission :** Restructurez-le selon les standards. Solution attendue :
```
mon_projet/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── mon_projet/
│       └── __init__.py
│       └── main.py
├── tests/
│   └── test_main.py
├── data/
│   └── data.csv
└── config/
    └── config.yaml
```

### Exercice 3 : Créer une structure de projet from scratch

Créez la structure complète pour :
1. **API REST Python (FastAPI)** avec base de données PostgreSQL
2. **Application web React + TypeScript** avec authentification
3. **Projet data science** avec notebooks et scripts

**Livrables :**
- Arborescence complète
- Fichiers de configuration minimaux (package.json, requirements.txt, etc.)
- README.md décrivant le projet

---

---

## Exemples concrets

### Exemple 1 : Projet Python data science

```
data-analysis/
├── README.md
├── requirements.txt
├── .gitignore
├── notebooks/               # Jupyter notebooks
│   ├── 01_exploration.ipynb
│   └── 02_modeling.ipynb
├── src/
│   └── data_analysis/
│       ├── __init__.py
│       ├── preprocessing.py
│       ├── models.py
│       └── visualization.py
├── data/
│   ├── raw/                 # Données brutes (non commitées si volumineuses)
│   ├── processed/           # Données traitées
│   └── external/            # Données tierces
├── models/                  # Modèles entraînés (.pkl, .h5)
├── reports/                 # Rapports générés (PDF, HTML)
│   └── figures/             # Graphiques
└── tests/
```

### Exemple 2 : API REST (Node.js + Express)

```
api-rest/
├── package.json
├── .env.example
├── .gitignore
├── README.md
├── src/
│   ├── app.ts               # Point d'entrée
│   ├── server.ts            # Configuration serveur
│   ├── routes/              # Définitions routes
│   │   ├── index.ts
│   │   ├── users.ts
│   │   └── auth.ts
│   ├── controllers/         # Logique métier
│   │   ├── userController.ts
│   │   └── authController.ts
│   ├── models/              # Schémas base de données
│   │   └── User.ts
│   ├── middleware/          # Middlewares Express
│   │   ├── auth.ts
│   │   └── errorHandler.ts
│   ├── services/            # Services (email, paiement)
│   │   └── emailService.ts
│   ├── utils/               # Fonctions utilitaires
│   │   └── logger.ts
│   └── config/              # Configuration
│       └── database.ts
├── tests/
│   ├── unit/
│   └── integration/
├── docs/
│   └── api-spec.yaml        # Spécification OpenAPI
└── prisma/                  # Si utilisation de Prisma ORM
    └── schema.prisma
```

### Exemple 3 : Monorepo (plusieurs projets)

```
monorepo/
├── README.md
├── .gitignore
├── package.json             # Root package.json (workspaces)
├── lerna.json               # Configuration Lerna (optionnel)
├── packages/
│   ├── api/                 # Backend API
│   │   ├── package.json
│   │   └── src/
│   ├── web/                 # Frontend web
│   │   ├── package.json
│   │   └── src/
│   ├── mobile/              # Application mobile
│   │   ├── package.json
│   │   └── src/
│   └── shared/              # Code partagé
│       ├── package.json
│       └── src/
├── docs/                    # Documentation commune
└── scripts/                 # Scripts communs
```

---
