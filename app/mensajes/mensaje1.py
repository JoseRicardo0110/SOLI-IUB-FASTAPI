import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
import ssl



def Mensaje1(para):
    """ "josearh1229@gmail.com" """
    contrasena = "iqju puip jgft oxdm"
    usuario = "joseangelrh1229@gmail.com"
    asunto = "Se agrego una respuesta a tu solicitud"
    destinatario = para
    mensaje = "Se ha agregado una nueva respuesta para tu solicitud ingresa al aplicaivo para visualizar tu respuesta"

    # Creamos el objeto mensaje
    message = EmailMessage()
    message['From'] = usuario
    message['Subject'] = asunto
    message['To'] = destinatario
    message.set_content(mensaje)

    context= ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(usuario,contrasena)
        smtp.sendmail(usuario,destinatario,message.as_string())


def Mensaje2(para):
    """ "josearh1229@gmail.com" """
    contrasena = "iqju puip jgft oxdm"
    usuario = "joseangelrh1229@gmail.com"
    asunto = "Tu solicitud ha sido asignada"
    destinatario = para
    mensaje = "se ha signado una persona a tu solicitud, estate  atento a las respuestas que den sobre tu solicitud"

    # Creamos el objeto mensaje
    message = EmailMessage()
    message['From'] = usuario
    message['Subject'] = asunto
    message['To'] = destinatario
    message.set_content(mensaje)

    context= ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(usuario,contrasena)
        smtp.sendmail(usuario,destinatario,message.as_string())


def Mensaje3(para):
    """ "josearh1229@gmail.com" """
    contrasena = "iqju puip jgft oxdm"
    usuario = "joseangelrh1229@gmail.com"
    asunto = "Tu solicitud ha sido finalizada"
    destinatario = para
    mensaje = "Se ha fnalizado tu solicitud, puedes ingresar al aplicativo y verificar la ultima respuesta que te brindaron"

    # Creamos el objeto mensaje
    message = EmailMessage()
    message['From'] = usuario
    message['Subject'] = asunto
    message['To'] = destinatario
    message.set_content(mensaje)

    context= ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(usuario,contrasena)
        smtp.sendmail(usuario,destinatario,message.as_string())