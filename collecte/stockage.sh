#!/bin/bash

# Fichier pour contenir les données des sondes
FICHIER_DONNEES="collecte/donnees/$(date +%Y-%m-%d_%H-%M-%S).csv"
touch $FICHIER_DONNEES
# Fichier pour contenir les erreurs pour le débogage
FICHIER_LOG="collecte/donnees/$(date +%Y-%m-%d_%H-%M-%S).log"
touch $FICHIER_LOG

# On appelle le nettoyeur pour supprimer les fichiers trop anciens
./collecte/nettoyage.sh >> $FICHIER_LOG

echo "Début de la collecte." >> $FICHIER_LOG
# On appelle tous les fichiers contenus dans le dossier sondes
for SONDE in ./collecte/sondes/*; do
    echo "Collecte de la sonde : $SONDE" >> $FICHIER_LOG
    ./$SONDE >> $FICHIER_DONNEES 2>> $FICHIER_LOG
done
echo "Fin de la collecte." >> $FICHIER_LOG
