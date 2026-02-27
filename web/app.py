#!/usr/bin/env python3

import os
import glob
from flask import Flask, render_template
import pygal

app = Flask(__name__)

def actualite_rss():

    fichier_rss = './collecte/donnees/rss.txt'
    with open(fichier_rss, 'r') as f:
        return f.read()

def donnees_dernier_sondages():
    dossier = "./collecte/donnees/"
    # Récupère tous les fichiers .csv dans le dossier
    fichiers_csv = glob.glob(os.path.join(dossier, "*.csv"))
    # Trouve le fichier le plus récent
    fichier_recent = max(fichiers_csv, key=os.path.getmtime)


def generer_statistique(attribut):
    # On prend les valeurs de attribut dans chaque fichier de sondage
    dossier = "./collecte/donnees/"
    # Récupère tous les fichiers .csv dans le dossier
    fichiers_donnees_csv = glob.glob(os.path.join(dossier, "*.csv"))
    # Trier les fichiers par date de modification
    fichiers_donnees_csv.sort(key=os.path.getmtime)

    valeurs = []

    # On lit chaque fichier de sondage
    for fichier in fichiers_donnees_csv:
        with open(fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
            # Sépare le texte ligne par ligne
            lignes = contenu.splitlines()
            for ligne in lignes:
                # Ignore les lignes vides
                if ligne.strip() == "":
                    continue
                # Sépare la ligne par ":"
                nom, valeur = ligne.split(":")
                # Récupère la valeur correspondante à l'attribut recherché
                if nom == attribut:
                    valeurs.append(float(valeur))

    # Crée un graphique avec pygal
    graphique = pygal.Line()
    graphique.title = f"Statistiques de {attribut}"
    graphique.add(attribut, valeurs)
    graphique.render_to_file(f"./web/static/{attribut.lower()}.svg")

def consommation_ressources():
    # Génère les statistiques de consommation de ressources
    generer_statistique("DISQUE_POURCENTAGE")
    generer_statistique("PROCESSEUR_POURCENTAGE")
    generer_statistique("RAM_UTILISE_POURCENTAGE")
    generer_statistique("NOMBRE_PROCESSUS")
    generer_statistique("NOMBRE_USERS")

    # Lister tous les fichiers svg d'un dossier
    dossier = "./web/static/"
    # Retourne tous les fichiers .csv contenus dans le dossier static
    # On fixe le chemin pour éviter un bogue
    return [chemin.replace("./web/static/", "./static/") for chemin in glob.glob(os.path.join(dossier, "*.svg"))]

@app.route("/")
def home():
    return render_template("index.html", rss_texte=actualite_rss(), graphiques_ressources=consommation_ressources())

if __name__ == "__main__":
    print(consommation_ressources())
    app.run(debug=True, port=8275)
