#Función de envío de correos
import smtplib #Se conecta al servidor del correo
from email.mime.text import MIMEText #Genera el cuerpo del mensaje
from email.mime.multipart import MIMEMultipart #Permite usar txt,html,img,etc
from email.mime.base import MIMEBase 
from email import encoders
import os

#Función
def send_email(send_email, password, recipients, subject, body, provider="gmail", attachments= None):
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
        message["From"] = send_email
        message["To"] = ", ".join(recipients)
        message["Subject"] = subject

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
        server = smtplib.SMTP(smtp_server, port)
        server.starttls() #Activación TLS Encryption
        #Login
        server.login(send_email, password)
        #Enviar correo
        server.sendmail(send_email, recipients, message.as_string())
        #Cerrar conexion
        server.quit()

        #Mensaje de éxito
        print(f'Correo enviado con vía {provider.capitalize()}!')
        return True

    except Exception as e:
        print("Error al momento de enviar el correo: ",e)

        return False
