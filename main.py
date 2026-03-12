from email_service import send_email


sender = "y2776430@gmail.com"
password = "abiglmljfpnjhgmv" #Se debe generar una App Password Gmail.

recipients = [
    "yahirhernandezolivaress@gmail.com"
]

subject = "Prueba de correo"

body = """
<html>
    <body style="font-family: Arial, sans-serif; color: #333333; line-height:1.5;">
        <h2 style="color:abc;">Envio de correo </h2>
        <p>El motivo de este comunicado solo es con fines de pruebas</p>
    </body>
</html>
"""

send_email(sender, password, recipients, subject, body)