---
image: "https://www.omg.org/images/logos/UML-logo.png"
featuredLinks:
  - prev:
  - next:
  - mid:
  - exp:
  - ofi: "https://www.omg.org/spec/UML/2.5.1/PDF"
---

# Unified Modeling Language (UML)

UML vise à permettre l’interopérabilité entre les outils de modélisation, s’inscrit dans l’approche *MDA*.

Une opération UML définit ce qui doit se passer (post-condition) mais pas comment (comportement détaillé)

UML modélise un système en séparant deux types de sémantique, à l’aide d’un métamodèle standard basé sur *MOF* :

```mermaid
flowchart TB
UseCase --> Structure
UseCase ----> Dynamiques
UseCase --> Implents

Structure --> Component
Structure ---> Composite
Structure --> Class
Structure ---> Object

Dynamiques --> Activity
Dynamiques ---> Communication
Dynamiques --> Etats
Dynamiques ---> Sequence
Dynamiques --> Timing

Implents --> Deployment
Implents ---> Package
Implents --> Profile
```
