---
versions: 1.0.0
effectiveDate: 2025-12-19
author: RICHARD Wilfried

title: Arbre de décision — Choisir une licence
intro: Guide visuel pour choisir la licence la plus adaptée à votre projet (code, données, documentation).
type: reference
topics:
   - licence
   - open source
   - arbre de décision
   - legal
image: "https://upload.wikimedia.org/wikipedia/commons/4/43/Creative_Commons_logo.svg"
---

# Arbre de décision (format puces) — Choisir une licence

## GLOSSAIRE

- SPDX : Standard d'identifiants de licences (ex: "MIT", "Apache-2.0").
- CLA / DCO : Contrat clarifiant les droits des contributeurs (Contributor License Agreement ou Developer Certificate of Origin).
- Copyleft : Principe qui oblige les œuvres dérivées à conserver la même licence libre.
- Permissive : Licence qui impose peu de contraintes sur la réutilisation.
- Brevet : Protection d'une invention; peut nécessiter clause spécifique dans la licence.
- RGPD : Règlement général sur la protection des données personnelles; à vérifier si projet traite des données.

## Arvre de dessision

Suivez les puces du haut vers le bas. Chaque étape donne une recommandation claire et le lien pour copier le texte officiel.

- Voulez‑vous partager le code publiquement ?
  - ❌ Non → Option : Propriétaire / "All Rights Reserved" (pas de fichier LICENSE ou fichier indiquant "All rights reserved").
  - ✅ Oui → 📖 Open Source, Continuer

- Documentation / tutoriels → Voulez-vous autoriser l'usage commercial ?
   - ✅ Oui → CC‑BY‑4.0 — Attribution requise, usage commercial autorisé. Texte : https://creativecommons.org/licenses/by/4.0/
   - Non → Voulez-vous obliger le partage des modifications ?
      - ✅ Oui → CC‑BY‑NC‑SA‑4.0 —  ShareAlike (modifications doivent être partagées sous même licence). Texte : https://creativecommons.org/licenses/by-nc-sa/4.0/
      - ❌ Non → CC‑BY‑NC‑4.0 — modifications autorisées sans obligation de partage. Texte : https://creativecommons.org/licenses/by-nc/4.0/
- Datasets → CC0, Domaine public pour données / contenus (domaine public). Texte : https://creativecommons.org/publicdomain/zero/1.0/
- Les dérivés doivent‑ils rester obligatoirement libres (copyleft) ?
  - ✅ Oui (copyleft fort) → Est‑ce une application web / SaaS ?
    - ✅ Oui → AGPL‑3.0 — protège l'usage via réseau. Comme la GPL mais étend l'obligation au service réseau (SaaS). Texte : https://www.gnu.org/licenses/agpl-3.0.en.html
    - ❌ Non → GPL‑3.0 — copyleft fort pour applications, oblige les dérivés à rester sous GPL. Texte : https://www.gnu.org/licenses/gpl-3.0.en.html
    - Si vous voulez copyleft par fichier → MPL‑2.0. Texte : https://www.mozilla.org/en-US/MPL/2.0/
  - Non (permise) → Avez‑vous des préoccupations brevets / contributions d'entreprises ?
    - ✅ Oui → Apache‑2.0 — permissive + clause brevets. Texte : https://www.apache.org/licenses/LICENSE-2.0
    - ❌ Non → Est‑ce une bibliothèque que vous voulez permettre de lier par du code propriétaire ?
      - ✅ Oui → LGPL‑3.0 — copyleft faible pour bibliothèques (autorise linking propriétaire). Texte : https://www.gnu.org/licenses/lgpl-3.0.en.html
      - ❌ Non → MIT — très simple, adoption maximale, permet usage commercial et fermeture des dérivés. Texte : https://opensource.org/licenses/MIT
    - Variante permissive alternative → BSD‑3‑Clause, similaire à MIT avec clause anti‑endorsement. Texte : https://opensource.org/licenses/BSD-3-Clause

## ⚖️ Implications juridiques

### Vue d'ensemble rapide

| Licence | Type | Complexité | Usage commercial | Copyleft | Brevets | Popularité |
|---------|------|------------|------------------|----------|---------|------------|
| **MIT** | Permissive | ⭐ Simple | ✅ Oui | ❌ Non | ⚠️ Implicite | ⭐⭐⭐⭐⭐ |
| **Apache 2.0** | Permissive | ⭐⭐ Modéré | ✅ Oui | ❌ Non | ✅ Explicite | ⭐⭐⭐⭐ |
| **BSD 3-Clause** | Permissive | ⭐ Simple | ✅ Oui | ❌ Non | ⚠️ Implicite | ⭐⭐⭐ |
| **GPL v3** | Copyleft | ⭐⭐⭐ Complexe | ✅ Oui* | ✅ Fort | ✅ Explicite | ⭐⭐⭐⭐ |
| **LGPL v3** | Copyleft faible | ⭐⭐⭐ Complexe | ✅ Oui* | ⚠️ Partiel | ✅ Explicite | ⭐⭐⭐ |
| **AGPL v3** | Copyleft réseau | ⭐⭐⭐ Complexe | ✅ Oui* | ✅ Très fort | ✅ Explicite | ⭐⭐ |
| **MPL 2.0** | Copyleft par fichier | ⭐⭐ Modéré | ✅ Oui | ⚠️ Par fichier | ✅ Explicite | ⭐⭐ |
| **Unlicense** | Domaine public | ⭐ Minimal | ✅ Oui | ❌ Non | ❌ Aucune | ⭐⭐ |
| **CC BY 4.0** | Contenu | ⭐⭐ Modéré | ✅ Oui | ❌ Non | ❌ N/A | ⭐⭐⭐⭐ |
| **CC0** | Domaine public | ⭐ Minimal | ✅ Oui | ❌ Non | ❌ N/A | ⭐⭐⭐ |

*Usage commercial autorisé, mais avec obligation de redistribuer le code source modifié.

### Compatibilité entre licences

<!--
POINT CRITIQUE : Toutes les licences ne peuvent pas être combinées.
-->

#### Matrice de compatibilité (peut intégrer du code X dans un projet Y ?)

|                  | **Vers MIT** | **Vers Apache 2.0** | **Vers GPL v3** | **Vers AGPL v3** | **Vers Propriétaire** |
|------------------|--------------|---------------------|-----------------|------------------|-----------------------|
| **Depuis MIT**   | ✅           | ✅                  | ✅              | ✅               | ✅                    |
| **Depuis Apache**| ⚠️*          | ✅                  | ✅              | ✅               | ✅                    |
| **Depuis BSD**   | ✅           | ✅                  | ✅              | ✅               | ✅                    |
| **Depuis GPL v3**| ❌           | ❌                  | ✅              | ✅               | ❌                    |
| **Depuis AGPL**  | ❌           | ❌                  | ❌              | ✅               | ❌                    |
| **Depuis LGPL**  | ⚠️**         | ⚠️**                | ✅              | ✅               | ⚠️** (linking)        |

*Apache → MIT : Perd les clauses de brevets  
**LGPL : Dépend du type de linking (statique vs dynamique)

### Obligations principales par licence

| Licence | Redistribuer code source | Conserver notice copyright | Déclarer modifications | Même licence pour dérivés | Accorder licence brevets |
|---------|--------------------------|----------------------------|------------------------|---------------------------|--------------------------|
| **MIT** | ❌ Non | ✅ Oui | ❌ Non | ❌ Non | ⚠️ Implicite |
| **Apache 2.0** | ❌ Non | ✅ Oui | ✅ Oui (NOTICE) | ❌ Non | ✅ Oui (explicite) |
| **GPL v3** | ✅ Oui | ✅ Oui | ✅ Oui | ✅ Oui | ✅ Oui (explicite) |
| **AGPL v3** | ✅ Oui (même hébergement) | ✅ Oui | ✅ Oui | ✅ Oui | ✅ Oui (explicite) |
| **BSD 3-Clause** | ❌ Non | ✅ Oui | ❌ Non | ❌ Non | ⚠️ Implicite |

## 🛠️ Outils et ressources

### Outils en ligne

1. **[choosealicense.com](https://choosealicense.com/)** ⭐⭐⭐⭐⭐
   - Par GitHub, interface simple
   - Recommandations claires
   - Comparaison visuelle

2. **[TLDRLegal](https://tldrlegal.com/)** ⭐⭐⭐⭐
   - Résumés en langage simple
   - "Vous pouvez" / "Vous devez" / "Vous ne pouvez pas"
   - Couverture de 70+ licences

3. **[Licensecheck](https://github.com/licensee/licensee)** ⭐⭐⭐
   - Outil CLI pour détecter licences dans projets
   - Utilisé par GitHub pour badge de licence

4. **[SPDX License List](https://spdx.org/licenses/)** ⭐⭐⭐⭐
   - Liste officielle de 400+ licences
   - Identifiants standardisés (pour package.json, etc.)

### Lectures essentielles

1. **[Open Source Guide](https://opensource.guide/legal/)** (GitHub)
   - Guide juridique complet et accessible
   
2. **[GNU License Recommendations](https://www.gnu.org/licenses/license-recommendations.html)**
   - Par Free Software Foundation
   
3. **[Apache License FAQ](https://www.apache.org/foundation/license-faq.html)**
   - Questions fréquentes sur Apache 2.0

### Livres recommandés

- **"Understanding Open Source and Free Software Licensing"** par Andrew M. St. Laurent
- **"Open Source Licensing: Software Freedom and Intellectual Property Law"** par Lawrence Rosen

### Consultation juridique

⚠️ **Disclaimer** : Ce guide est informatif, pas un avis juridique.

Pour des décisions importantes (projet commercial, entreprise, brevets complexes), **consultez un avocat spécialisé en propriété intellectuelle**.

## ✅ Checklist finale

Avant de publier votre projet, vérifiez :

- [ ] **Fichier LICENSE présent** à la racine du dépôt
- [ ] **Copyright notice** avec année et nom dans LICENSE
- [ ] **Badge de licence** dans README.md
  ```markdown
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  ```
- [ ] **Section "Licence" dans README** expliquant brièvement les droits
- [ ] **package.json / setup.py / pom.xml** avec champ `license` (si applicable)
  ```json
  "license": "MIT"
  ```
- [ ] **THIRD-PARTY-NOTICES** si vous utilisez des dépendances (optionnel mais recommandé)
- [ ] **En-têtes de fichiers** (si licence l'exige, ex: Apache, GPL)
- [ ] **Compatibilité vérifiée** avec licences des dépendances

---

<div align="center">

**⚖️ Choisissez avec soin, partagez avec clarté ! 📜**

*Ce guide est lui-même sous licence **CC BY 4.0** — partagez et adaptez librement avec attribution.*

</div>