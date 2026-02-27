#!/bin/bash

# Collecte du nombre d'utilisateurs connectés
nombre_users=$(who | wc -l)
echo "NOMBRE_USERS:$nombre_users"
