# Application de Gestion des Salles

## Informations personnelles
- **Nom** : Tchumno Toche
- **Prénom** : Arnauld Duvane 
- **Cours** : INF1093 - Programmation II
- **Professeur** : Youness Boukouchi

## Description de l'atelier
Application Python de gestion de salles développée avec :
- Une base de données **MySQL** pour stocker les salles
- Une architecture en **3 couches** :
  - Couche Data (DAO) : accès à la base de données
  - Couche Service : logique métier et validation
  - Couche View : interface graphique
- Une interface graphique avec **customTkinter**

## Structure du projet
app_gestion_salles/
├── data/
│   ├── config.json
│   └── dao_salle.py
├── models/
│   └── salle.py
├── services/
│   └── services_salle.py
├── views/
│   └── view_salle.py
├── main.py
└── README.md