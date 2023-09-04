import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(receiver_email, subject, message, attachment_path):
    SMTP_USERNAME = os.getenv("SMTP_USERNAME")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = os.getenv("SMTP_PORT")

    msg = MIMEMultipart()
    msg['From'] = SMTP_USERNAME
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    with open(attachment_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name="countries_data.xlsx")
        part['Content-Disposition'] = f'attachment; filename="countries_data.xlsx"'
        msg.attach(part)

    try:
        server = smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT))
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.connect(SMTP_SERVER, int(SMTP_PORT))
        server.sendmail(SMTP_USERNAME, receiver_email, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Fail to send email: {str(e)}")