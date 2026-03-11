from email_service import send_email


sender = "juan.perez@outlook.com"
password = "tu_app_password_aqui" #Se debe generar una App Password.

recipients = [
    "maria.garcia@gmail.com"
]

subject = "Prueba de correo"

body = """
Prueba 1 de correo 11/03/26
""""

send_email(sender, password, recipients, subject, body)