#!/usr/bin/env python3

import psutil

ram_utilisation = psutil.virtual_memory()

# les valeurs sont en Mo après division
print(f"RAM_UTILISE:{ram_utilisation.used // (1024 ** 2)}")
print(f"RAM_LIBRE:{ram_utilisation.available // (1024 ** 2)}")
print(f"RAM_TOTAL:{ram_utilisation.total // (1024 ** 2)}")
print(f"RAM_UTILISE_POURCENTAGE:{ram_utilisation.percent}")
