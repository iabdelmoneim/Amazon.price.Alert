import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/' \
      'Marvels-Spider-Man-Miles-Morales-Launch-PlayStation/dp/B08JHVG9ZJ/' \
      'ref=sr_1_2?dchild=1&keywords=PS5&qid=1605223557&sr=8-2'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    print(soup.prettify())

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if (converted_price < 1.700):
        send_email()

    print(title.strip())
    print(converted_price)

    if(converted_price > 49.1):
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('iabdelmoneim97@gmail.com', 'password')

    subject = 'price fell down'
    body = 'Check the link https://www.amazon.com/' \
      'Marvels-Spider-Man-Miles-Morales-Launch-PlayStation/dp/B08JHVG9ZJ/' \
      'ref=sr_1_2?dchild=1&keywords=PS5&qid=1605223557&sr=8-2'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'iabdelmoneim97@gmail.com',
        'iabdelmoneim97@gmail.com',
        msg
    )

    print('HEY EMAIL HAS BEEN SENT')

    server.quit()

while(True):
    check_price()
    time.sleep(400)
