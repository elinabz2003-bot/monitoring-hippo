#!/usr/bin/env python3

import psutil

utilisation_cpu_pourcentage = psutil.cpu_percent(interval=1)
print(f"PROCESSEUR_POURCENTAGE:{utilisation_cpu_pourcentage}")
