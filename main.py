from email_service import send_email
import pandas as pd
from nicegui import ui

#DataFrame de prueba
data = {
    "Empleado": ["Juan", "Maria", "Carlos"],
    "Ventas": [1200, 1500, 900],
    "Departamento": ["Ventas", "Marketing", "Soporte"],
    "Localidad": ["Saltillo", "Canada", "EUA"]
}

df = pd.DataFrame(data)

#Metodo
def enviar_correo():
    sender = "y2776430@gmail.com"
    password = "abiglmljfpnjhgmv" #Se debe generar una App Password Gmail.
    #sender = "y2776430@outlook.com"
    #password = "VJVLQPUGQL3N468HP8QU9CUVK"

    recipients = [
        "y2776430@outlook.com",
        "practicasryd@palliser.ca"
    ]

    subject = "Reporte de prueba con Pandas - 12/03/22"

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

    attachments = ["files/smtp.png", "files/guia.pdf"]

    success = send_email(sender, password, recipients, subject, body, dataframe=df, provider="gmail", attachments=attachments)

    #Notificacion
    if success:
        ui.notify("Correo enviado de manera exitosa.!", color="green")
    else:
        ui.notify("Error al enviar el correo.!", color="red")
    
ui.button("Enviar correo", on_click=enviar_correo)
ui.run()