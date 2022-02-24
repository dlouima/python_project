import smtplib
import datetime as dt
import random
from email.mime.text import MIMEText

current_date = dt.datetime.now()
week_day = current_date.weekday()

gmail = 'samplemail@gmail.com'
yahoo = 'destinationmail@yahoo.com'
password = 'password1234'

with open('quotes.txt', 'r') as file:
    data = file.readlines()
    msg = MIMEText(random.choice(data))
    msg['Subject'] = 'Weekly Motivation'
    msg['From'] = gmail
    msg['To'] = yahoo

if week_day == 3:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=gmail, password=password)
        connection.sendmail(gmail, yahoo, msg.as_string())
