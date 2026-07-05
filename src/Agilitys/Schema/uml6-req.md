
# Requirement

Le schema de Requirement permet de hierachiser les besoins, et d'ajouté le niveaux de risque et la methode de verification.

> je l'etuluse pour clarifier les autres diagramme et verifier q'uil ne manque rien

## Legende

- **Type** : Mettre de la couleur pour mieux les distinguer
  - `designConstraint` : contrainte de conception
  - `functionalRequirement` : liée à une action attendue
  - `interfaceRequirement` : échange externe
  - `performanceRequirement` : capacité ou rapidité
  - `physicalRequirement` :
  - `requirement` : exigence générale du système
- **Relations** :
  - `contains` : *exigence* contient une sous-exigence <!-- - `copies` -->
  - `derives` : *exigence* découle d’une autre
  - `refines` : *exigence* precise une autre
  - `satisfies` : *élément* satisfait par une *exigence*
  - `traces`: traçabilité entre éléments ou exigences
  - `verifies` : *élément* qui vérifie une *exigence*
- **Risques** :
  - `Low`
  - `Medium`
  - `High`
- **VerificationMethod** :
  - `Analysis`
  - `Inspection`
  - `Test`
  - `Demonstration`

## Exemple

```mermaid
requirementDiagram
element Caisse {
  type: api
}
Caisse -satisfies-> Addition
Caisse -verifies-> Payer
Caisse -satisfies-> Pizza

element Client {
  type: humain
}
Client -satisfies-> Ouverture

interfaceRequirement Ouverture:::interfaceHight {
  text: site web pour commander
}
Ouverture -contains-> Adress
Ouverture -contains-> Menu
Ouverture -contains-> Compte

element Map {
  type: api
}
Map -satisfies-> Rue

functionalRequirement Adress:::functionalMedium {
  text: lieu de livraison
}
Adress -contains-> Coordoner
designConstraint Coordoner:::designMedium {
  text: rentre info de contact
}
Coordoner -derives-> Rue
Coordoner -derives-> Distance
Coordoner -derives-> Comfirmer
functionalRequirement Distance:::functionalLow {
  text: limiter la distance
}
designConstraint Rue:::designLow {
  text: lister des adrres
}

functionalRequirement Menu:::functionalMedium {
  text: Afficher le Menu
}
Menu -contains-> Pizza
Menu -contains-> Selectioner
designConstraint Selectioner:::designMedium {
  text: choix multiple des Piza
}
Selectioner -derives-> Comfirmer
physicalRequirement Pizza:::physicalLow {
  text: liste des proposition
}

functionalRequirement Compte:::functionalMedium {
  text: contrepartie de commande
}
Compte -contains-> Payer
designConstraint Payer:::designMedium {
  text: evoyer la demande
}
Payer -derives-> Comfirmer
Payer -contains-> Reçu
physicalRequirement Addition:::physicalHight {
  text: genere le reçu
}
Addition -contains-> Reçu
designConstraint Reçu:::designHight {
  text: afficher l'addition
}

functionalRequirement Comfirmer:::functionalLow {
  text: bouton fin d'input
}

ClassDef designLow stroke:#005
ClassDef designMedium stroke:#00A
ClassDef designHight stroke:#00F
ClassDef functionalLow stroke:#050
ClassDef functionalMedium stroke:#0A0
ClassDef functionalHight stroke:#0F0
ClassDef interfaceLow stroke:#505
ClassDef interfaceMedium stroke:#A0A
ClassDef interfaceHight stroke:#F0F
ClassDef performanceLow stroke:#005
ClassDef physicalLow stroke:#500
ClassDef physicalMedium stroke:#A00
ClassDef physicalHight stroke:#F00
```
