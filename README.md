# Projet Déploiement Continu "No SSH" sur AWS

Ce projet implémente une pipeline CI/CD complète permettant de déployer une application microservices (Frontend + API) sur AWS de manière totalement automatisée ("Industrialisation & Automatisation "Zero Touch"").

## Architecture

*   **Cloud Provider** : AWS (Région `eu-west-3`)
*   **Infrastructure** : Instance EC2 Ubuntu (Provisionnée via Terraform)
*   **Configuration** : Ansible (Installation Docker, configuration)
*   **Conteneurs** : Docker Compose (Images stockées sur GHCR)
*   **CI/CD** : GitHub Actions

## Structure du Projet

```
.
├── .github/workflows/
│   └── deploy.yml        # Pipeline GitHub Actions
├── ansible/
│   └── deploy.yml        # Playbook Ansible pour configurer le serveur
├── infra/
│   └── main.tf           # Code Terraform pour l'infrastructure AWS
├── frontend/             # Code source du Frontend
├── app/                  # Code source de l'API (Python)
├── docker-compose.prod.yml # Stack Docker pour la production
└── README.md
```

## Fonctionnement du Pipeline

Le pipeline est déclenché manuellement (`workflow_dispatch`) depuis l'onglet Actions de GitHub. Il exécute les étapes suivantes :

1.  **Build & Push** :
    *   Construction des images Docker pour le Frontend et l'API.
    *   Push des images vers le GitHub Container Registry (GHCR).

2.  **Deploy (Infrastructure & Config)** :
    *   **Terraform** provisionne une instance EC2, un Security Group et génère une paire de clés SSH temporaire.
    *   Récupération de l'IP publique et de la clé privée générées.
    *   **Ansible** se connecte à l'instance (après une attente de sécurité pour le démarrage SSH).
    *   Installation de Docker et Docker Compose.
    *   Connexion au registre GHCR.
    *   Démarrage de l'application via `docker compose`.

## Prérequis

Pour faire tourner ce projet, les secrets suivants doivent être configurés dans le dépôt GitHub :

*   `AWS_ACCESS_KEY_ID` : Clé d'accès AWS.
*   `AWS_SECRET_ACCESS_KEY` : Clé secrète AWS.

## Accès à l'application

Une fois le pipeline terminé avec succès :
1.  Récupérez l'adresse IP publique dans les logs de l'étape "Generate Inventory" ou "Get Terraform Outputs".
2.  Accédez à l'application via `http://13.38.102.228`.

## Auteurs

Ce projet a été réalisé dans le cadre du TP "Industrialisation & Automatisation Zero Touch".