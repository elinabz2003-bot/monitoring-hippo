#!/usr/bin/env python3

import os
import smtplib
from email.message import EmailMessage

def envoi_mail(contenu):

    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 465))
    email_login = os.getenv("SMTP_USER")
    email_password = os.getenv("SMTP_PASS")

    if not email_login or not email_password:
        raise ValueError("SMTP credentials not set in environment variables")

    msg = EmailMessage()
    msg['Subject'] = 'AMS Système - Alerte'
    msg['From'] = email_login
    msg['To'] = email_login
    msg.set_content(
        "Bonjour,\n"
        "Les sondes AMS ont détecté une surconsommation.\n\n"
        + contenu
    )

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
        smtp.login(email_login, email_password)
        smtp.send_message(msg)

    print("E-mail envoyé !")