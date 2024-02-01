# Projet de Déploiement Continu

Ce dépôt contient une application Docker multi-conteneurs, composée d'un backend Flask, d'un frontend Streamlit et d'une base de données MySQL. Le projet est configuré pour l'intégration et le déploiement continus en utilisant GitHub Actions.

## Badges

[![Configuration MYSQL](https://github.com/nat997/DeploiementContinuCI-CD/actions/workflows/mysqlsetup.yml/badge.svg)](https://github.com/nat997/DeploiementContinuCI-CD/actions/workflows/mysqlsetup.yml)

[![Construction de l'Image Docker Frontend](https://github.com/nat997/DeploiementContinuCI-CD/actions/workflows/frontend_build.yml/badge.svg)](https://github.com/nat997/DeploiementContinuCI-CD/actions/workflows/frontend_build.yml)

[![Construction de l'Image Docker Backend](https://github.com/nat997/DeploiementContinuCI-CD/actions/workflows/backend_build.yml/badge.svg)](https://github.com/nat997/DeploiementContinuCI-CD/actions/workflows/backend_build.yml)

[![FlaskAPI TEST](https://github.com/nat997/DeploiementContinuCI-CD/actions/workflows/test_flaskapi.yml/badge.svg)](https://github.com/nat997/DeploiementContinuCI-CD/actions/workflows/test_flaskapi.yml)

[![Streamlit Frontend Test](https://github.com/nat997/DeploiementContinuCI-CD/actions/workflows/test_streamlit.yml/badge.svg)](https://github.com/nat997/DeploiementContinuCI-CD/actions/workflows/test_streamlit.yml)

## Structure du Projet

- `frontend/` : Contient l'application frontend Streamlit.
- `app/` : Contient l'application backend Flask.
- `db/` : Contient les scripts SQL pour configurer la base de données MySQL.
- `docker-compose.yml` : Définit la configuration multi-conteneurs avec Docker Compose.

## Configuration et Exécution

### Prérequis
- Docker
- Docker Compose

### Exécution de l'Application

1. Cloner le dépôt :
```
git clone https://github.com/nat997/DeploiementContinuCI-CD.git
cd DeploiementContinuCI-CD
```
2. Démarrer les services en utilisant Docker Compose :
```
docker-compose up -d
```
### Accès aux Applications
- Le frontend Streamlit est accessible à `http://localhost:8501`.
- L'API backend Flask peut être accédée à `http://localhost:5001`.

## Docker Hub

Les images Docker pour le frontend et le backend sont construites et publiées sur Docker Hub via GitHub Actions. Elles sont disponibles dans le dépôt Docker Hub sous les tags `frontend-latest` et `backend-latest`.
https://hub.docker.com/repository/docker/nat997/autodeployfromgithubtest/general

## Tests

- Les tests backend et frontend sont automatiquement exécutés via GitHub Actions à chaque push ou pull request sur la branche principale.

## Organigramme l'interaction 
![image](https://github.com/nat997/DeploiementContinuCI-CD/assets/67456959/9f20e3ab-df08-4fea-b1ac-96e70e011bf0)

## Demonstation clone git et lancement d'application
![README md-Project-VisualStudioCode2024-01-3119-17-31-ezgif com-crop](https://github.com/nat997/DeploiementContinuCI-CD/assets/67456959/083bfb64-2151-49d6-9cc9-9a8fc332000c)

![ezgif com-video-to-gif-converter](https://github.com/nat997/DeploiementContinuCI-CD/assets/67456959/f9ef7dbe-dce4-4534-835d-efa8e890d32d)
