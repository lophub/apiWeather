import requests
import json
import smtplib
import time
import schedule
from constants import emails, password, apiOW 

apiOW
apiOW_data = json.loads(apiOW.text)
apiOW_data = apiOW_data['weather']



def email():
    for apiOW_ticker in apiOW_data:
        weather = apiOW_ticker['description']
        #Writing the email body / forecast.
        content = ("'" + weather + "'" + " is today's forecast.")
        #The email is sent
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(emails, password)
        mail.sendmail(emails, emails, content)
        mail.close()

def main():
    schedule.every().day.at("8:00").do(email)
    while True:
        schedule.run_pending()
        time.sleep(60)
    
main()