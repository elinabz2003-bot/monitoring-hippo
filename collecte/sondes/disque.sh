#!/bin/bash

capacite_disque_utilise=$(df -BG / | tail -n 1 | tr -s ' ' | cut -d ' ' -f 3 | tr -d 'G')
capacite_disque_totale=$(df -BG / | tail -n 1 | tr -s ' ' | cut -d ' ' -f 2 | tr -d 'G')
capacite_disque_utilise_pourcentage=$((capacite_disque_utilise / capacite_disque_totale * 100))

# Les mesures sont en Go
echo "DISQUE_UTILISE:${capacite_disque_utilise}"
echo "DISQUE_TOTAL:${capacite_disque_totale}"
echo "DISQUE_POURCENTAGE:${capacite_disque_utilise_pourcentage}"
