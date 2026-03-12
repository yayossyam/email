from email_service import send_email


sender = "y2776430@gmail.com"
password = "abiglmljfpnjhgmv" #Se debe generar una App Password Gmail.
#sender = "y2776430@outlook.com"
#password = "VJVLQPUGQL3N468HP8QU9CUVK"

recipients = [
    "yahirhernandezolivaress@gmail.com",
    "y2776430@outlook.com"
]

subject = "Reporte de prueba - 12/03/22"

body = """
<html>
    <body style="font-family: Arial, sans-serif; color: #333333; line-height:1.5;">
        <h2 style="color:1a73e8;">Envio de correo </h2>
        <p>El motivo de este comunicado solo es con fines de pruebas</p>
        <p>Se recuerda <strong>esto es una prueba</strong> con diseño HTML</p>
        <br>
        <p>Saludos, equipo</p>
    </body>
</html>
"""
attachments = ["files/smtp.png"]

send_email(sender, password, recipients, subject, body, provider="gmail", attachments=attachments)