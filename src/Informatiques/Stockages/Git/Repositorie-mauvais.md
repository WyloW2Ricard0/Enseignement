
## Anti-patterns à éviter

### ❌ 1. Mélanger code et build artifacts

**Mauvais :**
```
projet/
├── main.py
├── main.pyc                 # ❌ Fichier compilé
├── __pycache__/             # ❌ Cache Python
└── dist/                    # ❌ Build (devrait être ignoré)
```

**Bon :**
```
projet/
├── src/
│   └── main.py
└── .gitignore               # Contient __pycache__/, dist/
```

### ❌ 2. Nommage non descriptif

**Mauvais :**
```
projet/
├── stuff/
├── tmp/
├── old/
├── backup/
└── new_version/
```

**Bon :**
```
projet/
├── src/
├── tests/
├── docs/
└── scripts/
```

### ❌ 3. Duplication de fichiers

**Mauvais :**
```
projet/
├── config.json
├── config_old.json
├── config_backup.json
├── config_final.json
└── config_final_v2.json
```

**Bon :**
Utilisez Git pour l'historique, gardez une seule version actuelle.

### ❌ 4. Secrets committés

**Mauvais :**
```
projet/
├── .env                     # ❌ Contient API_KEY=sk_live_xxx
└── config/
    └── secrets.json         # ❌ Mots de passe en clair
```

**Bon :**
```
projet/
├── .env.example             # ✅ Template sans secrets
├── .gitignore               # ✅ Contient .env
└── README.md                # ✅ Instructions pour créer .env
```

### ❌ 5. Dépendances committées

**Mauvais :**
```
projet/
├── node_modules/            # ❌ 250 MB de dépendances
└── venv/                    # ❌ Environnement Python
```

**Bon :**
```
projet/
├── package.json             # ✅ Déclaration dépendances
├── requirements.txt         # ✅ Déclaration dépendances
└── .gitignore               # ✅ Contient node_modules/, venv/
```

### 3. Flat is better than nested

Évitez les imbrications excessives :
- ❌ `src/app/core/services/user/auth/providers/oauth/google/`
- ✅ `src/services/auth/google_oauth.py`

**Règle empirique :** Maximum 3-4 niveaux de profondeur.

### 4. Nommage explicite

Les noms de répertoires doivent être auto-documentés :
- ✅ `database_migrations/`
- ❌ `tmp/`, `stuff/`, `misc/`

---

---