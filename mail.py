PASSWORD = "masked-16-digit-app-password"  # Enter your app password
SENDER = "user_name@gmail.com"   # Enter your gmail address

import ssl
import smtplib
import os
from email import encoders
from email.mime.base import MIMEBase
from email.message import EmailMessage
from base64 import b64encode, b64decode

def ec(password):
    return b64encode(password.encode()).decode()
def dc(encrypted_password):
    return b64decode(encrypted_password.encode()).decode()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # For SSL

def send_mail(recipients, subject, body, attachment_path=None):
    port = SMTP_PORT
    sender_email = SENDER
    smtp_server = SMTP_SERVER
    password = PASSWORD

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = ", ".join(recipients)

    # Always use absolute path for `attachment_path`!!!
    if attachment_path and os.path.isfile(attachment_path):
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(attachment_path)}",
            )
            msg.add_attachment(
                part.get_payload(decode=True),
                maintype=part.get_content_maintype(),
                subtype=part.get_content_subtype(),
                filename=os.path.basename(attachment_path),
            )
    elif attachment_path is not None:
        print(f"Attachment path {attachment_path} is invalid!")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, dc(password))
        server.send_message(msg)
        print(f"Email has just been successfully sent to {', '.join(recipients)}")


## Example usage
# RECIPIENTS = ["receiver@gmail.com"]
# send_mail(
#     RECIPIENTS,
#     "EMAIL-SUBJECT",
#     "MSG_CONTENT",
#     attachment_path="/ABSOLUTE/PATH/TO/ATTACHMENT/FILE.jpg",
# )
## or without attachment
# send_mail(RECIPIENTS, "EMAIL-SUBJECT", "MSG_CONTENT")