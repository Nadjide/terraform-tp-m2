# TP Docker - Orchestration, Résilience et Industrialisation

Ce projet met en place une stack applicative complète (Frontend, Backend, Base de données, Cache) pour un Dashboard Étudiant.

## Architecture

- **Frontend** : Nginx (Port 8080)
- **Backend** : API Python FastAPI (Port 8000)
- **Database** : PostgreSQL (Interne)
- **Cache** : Redis (Interne)

## Pré-requis

- Docker Desktop
- Docker Compose

## Lancement

1.  Cloner le dépôt :
    ```bash
    git clone https://github.com/Nadjide/tp1-docker-ynov-m2.git
    cd tp1-docker-ynov-m2
    ```

2.  Lancer la stack :
    ```bash
    docker-compose up -d
    ```

3.  Accéder au dashboard :
    [http://localhost:8080](http://localhost:8080)

## Sécurité & Résilience

- **Non-root** : L'API tourne avec un utilisateur système limité (`appuser`).
- **Isolation** : Seuls les ports nécessaires sont exposés. La DB et Redis ne sont accessibles que via le réseau interne `private_net`.
- **Graceful Degradation** : Le dashboard reste fonctionnel (avec des données dégradées) même si le cache Redis est indisponible.
