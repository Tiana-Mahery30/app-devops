#!/bin/bash

echo "🛑 Arrêt du projet DevOps..."

# Arrêter le conteneur Docker
if [ "$(docker ps -q -f name=app-devops-container)" ]; then
    docker stop app-devops-container
    echo "✅ Conteneur Docker arrêté"
else
    echo "ℹ️ Aucun conteneur en cours d'exécution"
fi

# Arrêter Jenkins
sudo systemctl stop jenkins
echo "✅ Jenkins arrêté"

# Arrêter Nginx
sudo systemctl stop nginx
echo "✅ Nginx arrêté"

echo "----------------------------------------"
echo "✅ Tous les services sont arrêtés."
