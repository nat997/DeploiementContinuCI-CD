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

Pour documenter votre projet en français, incluant l'API Flask, le Dockerfile, et l'application Streamlit, ainsi que la configuration Docker Compose, voici une ébauche de documentation concise et claire. Cette documentation est destinée à expliquer les différents points d'entrée (endpoints) de votre application, les requêtes HTTP supportées (GET), les ports exposés, et la structure générale de votre projet.

# Documentation de l'API Flask
L'API Flask fournit deux endpoints principaux pour accéder aux données :

GET /degree : Renvoie les données des diplômes depuis la base de données. Chaque entrée contient un identifiant de diplôme et sa valeur correspondante.
GET /timestamp : Renvoie les données de timestamp depuis la base de données. Chaque entrée contient un identifiant de timestamp et le timestamp correspondant.
Dockerfile pour l'API Flask
Ce Dockerfile sert à construire une image Docker pour l'application Flask. Voici les étapes clés :

## Base Image : python:3.6
Port exposé : 5000 (L'application Flask écoute sur ce port)
Installation des dépendances : Les dépendances nécessaires sont installées à partir de requirements.txt.
Copie de l'application : Le fichier app.py contenant le code Flask est copié dans l'image.
Commande d'exécution : CMD python app.py lance l'application Flask.
## Application Streamlit
L'application Streamlit, servant de front-end, interroge l'API Flask et affiche les données sous forme graphique. Voici les points clés :

Récupération des données : Utilise requests.get() pour interroger les endpoints /degree et /timestamp de l'API Flask.
Traitement des données : Transforme les données JSON reçues en DataFrames pandas et les prépare pour la visualisation.
Visualisation : Utilise Matplotlib pour créer un graphique illustrant la relation entre les valeurs de diplôme et les timestamps.
Ports exposés : L'application Streamlit écoute sur le port 8501.
## Configuration Docker Compose
La configuration Docker Compose orchestre le déploiement de l'application complète, incluant l'API Flask, la base de données MySQL, l'application Streamlit, et un serveur Nginx comme reverse proxy.

## Services :
app : Application Flask, construite à partir du Dockerfile spécifié, écoutant sur le port 5000 interne, exposé au port 5001 externe.
db : Service de base de données MySQL, exposant le port 3306 interne au port 32000 externe. Utilise un volume pour persister les données et un autre pour initialiser la base de données.
frontend : Application Streamlit, construite à partir du contexte spécifié, écoutant sur le port 8501.
nginx : Serveur Nginx agissant comme reverse proxy, configuré pour rediriger les requêtes vers les services appropriés, exposant les ports 80 (HTTP) et 443 (HTTPS).
## Conclusion
Cette documentation offre un aperçu de la structure et des fonctionnalités de votre projet, incluant les endpoints de l'API, les commandes Docker/Docker Compose, et la manière dont les données sont traitées et visualisées via l'application Streamlit. C'est un guide utile pour les développeurs et les utilisateurs finaux souhaitant comprendre et interagir avec votre application.





