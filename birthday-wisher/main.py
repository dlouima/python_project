import random
import datetime as dt
import pandas as pd
import smtplib

now = dt.datetime.now()
today = (now.month, now.day)

data = pd.read_csv('birthdays.csv')

birthday_data = {(data_row.month, data_row.day): data_row for  (index, data_row) in data.iterrows()}

if today in birthday_data:
    receiver_name = birthday_data[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path, ) as file:
        first_line = file.read()
        first_line = first_line.replace('[NAME]', receiver_name['name'])


    sender = 'samplemail@gmail.com'
    receiver = receiver_name['email']
    password = 'password'

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(sender, receiver, msg=f"Subject: Happy Birthday\n\n{first_line}")



