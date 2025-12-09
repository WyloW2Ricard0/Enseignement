# Data — Configuration

Ce dossier contient des fichiers de configuration et des scripts Python utilisés pour automatiser et standardiser les opérations Git dans le projet `Enseignement`.

## Contenu

📄 variable.py # Fichier de configuration Python centralisant les variables.

## Utilité

Ce fichier sert de source unique de vérité pour les configurations du projet, permettant :

1. **Automatisation des scripts** : Importer ces variables dans d'autres scripts Python pour automatiser les opérations Git sans hardcoder les valeurs.

2. **Cohérence** : Garantir que tous les scripts utilisent les mêmes paramètres (nom de branche, URL, remote).

3. **Facilité de maintenance** : Modifier une configuration à un seul endroit au lieu de chercher dans tous les fichiers.

4. **Documentation** : Servir de référence rapide pour les paramètres du projet.

## Bonnes pratiques

### ⚠️ Ne pas committer de secrets
Si vous ajoutez des tokens, mots de passe ou clés API à ce fichier :
1. Renommez-le en `variable_local.py`
2. Ajoutez `*_local.py` au `.gitignore`
3. Créez un `variable_template.py` avec des valeurs factices pour la documentation

### 🔒 Variables sensibles
Pour stocker des secrets, utilisez plutôt :
- Fichiers `.env` (avec `python-dotenv`)
- Variables d'environnement système
- Gestionnaires de secrets (Azure Key Vault, AWS Secrets Manager)

### 📝 Documentation
Ajoutez des commentaires explicatifs pour chaque variable, surtout si leur usage n'est pas évident.

## Extension possible

Vous pouvez enrichir `variable.py` avec :
- Chemins vers des dossiers spécifiques (`LOGS_DIR`, `BACKUP_DIR`)
- Configuration pour CI/CD (branche de déploiement, environnements)
- Paramètres d'API (URLs, timeouts, retry)
- Constantes métier du projet
