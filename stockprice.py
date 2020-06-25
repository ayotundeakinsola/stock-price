import requests
import bs4
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://finance.yahoo.com/quote/RCL?p=RCL&.tsrc=fin-srch'

headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price =soup.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').get_text()
    converted_price=float(price)
    
    if(converted_price > 45):
        send_mail()
    
    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('aycooldrumz@gmail.com', 'jmtblbzjttqoxdou')
    
    subject =  'Price fell down'
    body = 'Check yahoo finance link: https://finance.yahoo.com/quote/RCL?p=RCL&.tsrc=fin-srch'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
            'aycooldrumz@gmail.com',
            'ayotundeakinsola@gmail.com',
            msg            
    )
    print('Hey EMAIL HAS BEEN SENT')
    
    server.quit()

while(True):    
    check_price()
    time.sleep(900)
