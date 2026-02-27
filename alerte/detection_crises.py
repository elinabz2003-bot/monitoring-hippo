#!/usr/bin/env python3

# Limites de consommation pour déclencher une alerte
limites = {
    'DISQUE_POURCENTAGE': 0,
    'PROCESSEUR_POURCENTAGE': 0,
    'RAM_UTILISE_POURCENTAGE': 0
}

def donnees_dernier_sondages():
    # Trouve et lis le dernier fichier CSV situé dans ./collecte/donnees/

    import os
    import glob

    dossier = "./collecte/donnees/"

    # Récupère tous les fichiers .csv dans le dossier
    fichiers_csv = glob.glob(os.path.join(dossier, "*.csv"))
    # Trouve le fichier le plus récent
    fichier_recent = max(fichiers_csv, key=os.path.getmtime)
    # Lecture du fichier
    with open(fichier_recent, "r", encoding="utf-8") as f:
        contenu = f.read()
    return contenu


def detection_crises(dernier_sondage):
    # Lis chaque ligne, sépare le texte par :
    # Si la valeur 1 dépasse celle de limite, alors return true
    # Sinon return false
    alertes_message = ""

    # Sépare le texte ligne par ligne
    lignes = dernier_sondage.splitlines()
    for ligne in lignes:
        # Ignore les lignes vides
        if ligne.strip() == "":
            continue
        # Sépare la ligne par ":"
        nom, valeur = ligne.split(":")
        valeur = float(valeur)
        if nom in limites and valeur >= limites[nom]:
            alertes_message += f"{nom} dépasse la limite ({valeur} > {limites[nom]})\n"
    
    # Retourne un texte contenant les messages d'alertes s'il y en a
    return alertes_message

if __name__ == "__main__":
    dernier_sondage = donnees_dernier_sondages()
    alertes_message = detection_crises(dernier_sondage)
    if alertes_message != "":
        from mail import envoi_mail
        # Envoi d'un mail
        envoi_mail(alertes_message)
