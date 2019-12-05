import smtplib
from config import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(RASP_EMAIL_ADDRESS, RASP_EMAIL_PASSWORD)
    
    subject = "RaspIP"
    body = "Testbody"

    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail(RASP_EMAIL_ADDRESS, RECIPIENT_EMAIL_ADDRESS, msg)