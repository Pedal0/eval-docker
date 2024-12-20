# Utilise l'image Python 3.11 comme base
FROM python:3.11-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie les fichiers de l'application dans le conteneur
COPY . .

# Installe les dépendances à partir de requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose le port sur lequel Flask écoute
EXPOSE 5000

# Commande pour démarrer l'application Flask
CMD ["flask", "run", "--host=0.0.0.0"]
