import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

# desire product url

Url = "https://www.amazon.com/Apple-Watch-SE-GPS-40mm/dp/B09G96SSLB/ref=sr_1_1_sspa?crid=3H125T9JWHO9L&keywords=apple+watch+se&qid=1646264044&sprefix=apple+watch+se%2Caps%2C68&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFKNTBMQUZEM0RVRjgmZW5jcnlwdGVkSWQ9QTA2NzAxNjExWVc0STc5OU9VNUMyJmVuY3J5cHRlZEFkSWQ9QTA3NzkzOTAxMTQzUk4wWVZWVVlaJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.109 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

html_text = requests.get(url=Url, headers=header).text

soup = BeautifulSoup(html_text, 'html.parser')

price = soup.find('span', class_="a-offscreen").get_text()

price_without_currency = float(price.split("$")[1])

from_add = "YOU_EMAIL"
to_add = "DESTINATION_EMAIL"
mail_server = "smtp.gmail.com"
port = 587
if price_without_currency < 300:

    with SMTP(mail_server, port=port) as connection:
        connection.starttls()
        connection.login(user=from_add, password="password")
        connection.sendmail(from_addr=from_add, to_addrs=to_add, msg=f"Subject: Price Alert! \n\n"
                                                                     f" Apple Watch price drop from amazon, Buy now")
