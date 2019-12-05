import smtplib
from config import RASP_EMAIL_ADDRESS, RASP_EMAIL_PASSWORD, RECIPIENT_EMAIL_ADDRESS
import logger

def send_mail(subject, message):
	with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login(RASP_EMAIL_ADDRESS, RASP_EMAIL_PASSWORD)
		msg = "Subject: " + subject  + "\n\n" + message
		smtp.sendmail(RASP_EMAIL_ADDRESS, RECIPIENT_EMAIL_ADDRESS, msg)
		logger.log("Mail sent with message: " + message)
