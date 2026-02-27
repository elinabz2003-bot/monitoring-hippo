# Projet AMS Système

## Installation

Vérifiez que le mode connexion de votre machine virtuelle est "Accès par pont".
D'abord essayer de pinger depuis votre ordi local vers l'adresse ip de votre machine virtuelle.
Autoriser le port 22 avec :

```bash
sudo ufw allow 22
```

Installez python si nécéssaire :

```bash
sudo apt install openssh-server python3 python3-pip python3-psutil python3-feedparser python3-flask
```

Pour exécuter le script automatiquement avec cron :

```bash
crontab -e
```

Ajoutez à la fin du fichier :

```bash
*/2 * * * * /chemin/vers/ams-sys-web/collecte/stockage.sh
0 0 * * * /chemin/vers/ams-sys-web/collecte/rss.sh
```

Pour envoyer le projet vers la machine virtuelle :

```bash
rsync -avz . user@ip-de-la-vm:/home/user/ams-sys-web
```

## Utilisation

Pour exécuter le programme, exécutez la commande suivante :

```bash
./collecte/stockage.sh
```

Pour supprimer les données collectées, exécutez la commande suivante :

```bash
./probers/reset_data.sh
```
