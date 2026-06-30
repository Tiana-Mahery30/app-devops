#!/bin/bash

echo "🚀 Lancement du projet DevOps..."

# Démarrer Jenkins
sudo systemctl start jenkins
echo "✅ Jenkins démarré"

# Démarrer Nginx
sudo systemctl start nginx
echo "✅ Nginx démarré"

# Vérifier le conteneur
if [ "$(docker ps -q -f name=app-devops-container)" ]; then
    echo "✅ Conteneur déjà en cours d'exécution"
else
    if [ "$(docker ps -aq -f name=app-devops-container)" ]; then
        docker start app-devops-container
    else
        docker run -d -p 8082:8000 --name app-devops-container app-devops
    fi
    echo "✅ Conteneur démarré"
fi

echo "----------------------------------------"
echo "🌐 Accède à l'application : http://localhost"
echo "🔧 Jenkins : http://localhost:8080"
echo "🐳 Docker : docker ps"
