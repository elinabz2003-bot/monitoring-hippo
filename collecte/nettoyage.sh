#!/bin/bash

# On garde au maximum 5 fichiers en historique
# On supprime les fichiers les plus anciens si on dépasse la limite
LIMITE=5

if [ $(find ./collecte/donnees -type f -name "*.csv" | wc -l) -gt $LIMITE ]; then
    # Lister les fichiers les plus anciens
    fichier_donnee_a_supprimer=$(ls -t ./collecte/donnees/*.csv | tail -n +$((LIMITE + 1)))
    fichier_log_a_supprime=$(ls -t ./collecte/donnees/*.log | tail -n +$((LIMITE + 1)))
    
    # Supprimer les fichiers
    for fichier in $fichier_donnee_a_supprimer; do
        echo "Suppression du fichier: $fichier"
        rm "$fichier"
    done
    for fichier in $fichier_log_a_supprime; do
        echo "Suppression du fichier: $fichier"
        rm "$fichier"
    done
fi
