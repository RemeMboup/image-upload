# Étape 1: Utiliser l'image officielle de Python
FROM python:3.10-slim

# Étape 2: Installer les dépendances système si nécessaire
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Étape 3: Définir un répertoire de travail dans le conteneur
WORKDIR /app

# Étape 4: Copier le fichier requirements.txt dans le conteneur
COPY ./requirements.txt /app/requirements.txt

# Étape 5: Installer les dépendances depuis requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Étape 6: Copier tout le code source de votre projet dans le conteneur
COPY . /app/

# Étape 7: Définir les variables d'environnement pour éviter le cache des fichiers pyc
ENV PYTHONUNBUFFERED=1

# Étape 8: Exposer le port 8000 (le port sur lequel Django fonctionne par défaut)
EXPOSE 8000

# Étape 9: Exécuter les commandes pour initialiser la base de données et démarrer le serveur
CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
