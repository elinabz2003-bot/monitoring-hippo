#!/usr/bin/env python3

import feedparser

# URL du flux RSS du CERT-FR
rss_url = "https://www.cert.ssi.gouv.fr/feed/"

# Récupération du flux
feed = feedparser.parse(rss_url)

# Récupère le dernier item de la liste d'actualités (qui est la plus récente)
dernier_item = feed.entries[-1]

# Ecrit les informations du dernier item dans ./collecte/donnees/rss.txt
with open("./collecte/donnees/rss.txt", "w") as f:
    f.write("Titre : " + dernier_item.title + "\n")
    f.write("Lien : " + dernier_item.link + "\n")
    f.write("Date de publication : " + dernier_item.published + "\n")
    f.write("Résumé : " + dernier_item.summary)
