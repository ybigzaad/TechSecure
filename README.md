# TechSecure

## Présentation

TechSecure est une application web développée avec Flask et MySQL permettant la gestion des filiales d'une entreprise.

Ce projet a été réalisé dans le cadre d'un TP sur le développement d'une application web sécurisée avec Flask, MySQL, Docker, Git et GitHub.

## Fonctionnalités

* Page d'accueil
* Présentation des services
* Liste des filiales
* Ajout d'une filiale
* Page de contact
* Présentation de l'entreprise

## Technologies utilisées

* Python 3
* Flask
* HTML5
* CSS3
* MySQL
* Docker
* Git
* GitHub

## Structure du projet

```text
TechSecure/
│
├── app.py
├── config.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
│
├── database/
│ └── database.sql
│
├── static/
│ ├── IMAGE/
│ └── style.css
│
└── templates/
├── base.html
├── index.html
├── services.html
├── filiales.html
├── ajout_filiale.html
├── contact.html
└── entreprise.html
```

## Installation

Créer un environnement virtuel :

```bash
python -m venv venv
```

Activer l'environnement virtuel sous Windows :

```bash
venv\Scripts\activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Lancer l'application :

```bash
python app.py
```

L'application est accessible à l'adresse :

```text
http://127.0.0.1:5000

## Sécurité

Les mesures de sécurité mises en place dans l'application sont :

* Validation des données côté client avec les champs `required`.
* Validation des données côté serveur avec Flask.
* Utilisation de requêtes SQL paramétrées pour prévenir les injections SQL.
* Configuration de la connexion MySQL à l'aide d'un fichier `config.py` et de variables d'environnement.

## Déploiement avec Docker

Le projet peut être déployé avec Docker grâce aux fichiers suivants :

* `Dockerfile` : création de l'image de l'application Flask.
* `docker-compose.yml` : déploiement des conteneurs Flask et MySQL.

Commandes principales :

```bash
docker compose build
docker compose up -d
docker compose down
```

## Auteur

Yves BIGZAAD

Formation : Administrateur d'Infrastructures Sécurisées (AIS) Bac+3
