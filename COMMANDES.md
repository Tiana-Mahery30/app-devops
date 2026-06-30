# Commandes du projet DevOps

## Démarrer l'application (Docker)
docker run -d -p 8082:8000 --name app-devops-container app-devops

## Arrêter le conteneur
docker stop app-devops-container && docker rm app-devops-container

## Reconstruire l'image
docker build -f docker/Dockerfile -t app-devops .

## Démarrer Jenkins (si arrêté)
sudo systemctl start jenkins

## Démarrer Nginx
sudo systemctl start nginx

## Voir les logs Jenkins
sudo journalctl -u jenkins -f

## Accéder à Jenkins
http://localhost:8080

## Accéder à l'application
http://localhost (via Nginx) ou http://localhost:8082 (direct)
