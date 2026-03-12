#Función de envío de correos
import smtplib #Se conecta al servidor del correo
from email.mime.text import MIMEText #Genera el cuerpo del mensaje
from email.mime.multipart import MIMEMultipart #Permite usar txt,html,img,etc

#Función
def send_email(send_email, password, recipients, subject, body):
    smtp_server = "smtp.gmail.com"
    port = 587

    #Protección de código
    try:
        #Creación del mensaje
        message = MIMEMultipart()
        message["From"] = send_email
        message["To"] = ", ".join(recipients)
        message["Subject"] = subject

        #Cuerpo del mensaje
        message.attach(MIMEText(body, "html"))

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
        print("Correo enviado de manera exitosa.!")


        return True
    except Exception as e:
        print("Error al momento de enviar el correo: ",e)

        return False
