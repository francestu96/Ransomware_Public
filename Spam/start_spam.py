from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import csv
import socks
import os

# socks.setdefaultproxy(socks.SOCKS5, "localhost", 9050)
# socks.wrapmodule(smtplib)

sender = "ministero.salute@salute.gov.it"

email = MIMEMultipart()

message = MIMEText(open("email_template.html", "r").read(), "html")

image = MIMEImage(open("ministero.salute.jpg", "rb").read())
image.add_header('Content-ID', '<ministero.salute.jpg>')

email["From"] = "Ministero della Salute"
email["Subject"] = "Linee Guida COVID-19 anno accademico 2020/2021"
email.attach(message)
email.attach(image)

with open("targets_emails.csv", newline="") as csvfile_targets:
    targets = csvfile_targets.readlines()
    with open("good_smtp_servers.csv", newline="") as csvfile_servers:
        servers = csv.reader(csvfile_servers, delimiter="|")

        for server in servers:
            for target in list(targets):
                smtp_server = server[0]
                port = server[1]
                username = server[2]
                password = server[3]        

                email["To"] = target.strip()                
                try:
                    with smtplib.SMTP(smtp_server, port, timeout=5) as conn:
                        conn.login(username, password)
                        conn.sendmail(sender, target.strip(), email.as_string())

                    targets.remove(target)
                    print(server[0] + " --> " + target.strip() + ": EMAIL CORRECTLY SENT")
                except Exception as e:
                    print(server[0] + " --> " + target.strip() + ": " + str(e))
