#!/bin/bash

# Collecte du nombre de processus
nombre_processus=$(ps -e --no-headers | wc -l)
echo "NOMBRE_PROCESSUS:$nombre_processus"
