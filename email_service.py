#Función de envío de correos
import smtplib #Se conecta al servidor del correo
from email.mime.text import MIMEText #Genera el cuerpo del mensaje
from email.mime.multipart import MIMEMultipart #Permite usar txt,html,img,etc
from email.mime.base import MIMEBase 
from email import encoders
import os
import pandas as pd

#Función
def send_email(sender, password, recipients, subject, body="",dataframe=None, provider="gmail", attachments= None):
    #Validaciones
    if not sender:
        raise ValueError("Es necesario un remitente")
    if not password:
        raise ValueError("Ingresa la App Password para poder enviar el correo")
    if not recipients or not isinstance(recipients, list):
        raise ValueError("Es necesario ingresar un correo receptor")
    if not subject:
        raise ValueError("El asunto no debe estar vacío")


    
    #Opciones de servidor SMTP
    if provider.lower() == "gmail":
        smtp_server = "smtp.gmail.com"
        port = 587
    elif provider.lower() == "outlook":
        smtp_server = "smtp.outlook.com"
        port = 587
    else: 
        raise ValueError("Solo soporta Gmail-Outlook")

    #Protección de código
    try:
        #Creación del mensaje
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = ", ".join(recipients)
        message["Subject"] = subject

        #Insertar DataFrame en caso de existir
        if dataframe is not None:
            table_html = dataframe.to_html(index=False)

            body += f"""
                <br>
                <h3>Reporte generado</h3>
                {table_html}
            """

        #Cuerpo del mensaje
        message.attach(MIMEText(body, "html"))

        #Adjuntar archivos en caso de existir
        if attachments:
            for file_path in attachments:
                if os.path.exists(file_path):
                    with open(file_path, "rb") as f:
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f'attachment; filename="{os.path.basename(file_path)}"'
                    )
                    message.attach(part)
                else:
                    print(f'Archivo no encontrado: {file_path}')

        #Conexion  al servidor SMTP
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls() #Activación TLS Encryption
            #Login
            server.login(sender, password)
            #Enviar correo
            server.sendmail(sender, recipients, message.as_string())
        #Cerrar conexion. Aplicando el with, hace el cierre de conexion automatico y seguro
        #server.quit()

        #Mensaje de éxito
        print(f'Correo enviado con vía {provider.capitalize()}!')
        return True

    except Exception as e:
        print("Error al momento de enviar el correo: ",e)

        return False
