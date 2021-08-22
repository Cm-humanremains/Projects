# credit goes to John Watson Rooney found on YouTube who has an extensive and great beginners to advanced tutorials on using python.

import requests
from bs4 import BeautifulSoup
import csv
import json

# under mystocks, jsut add the stock symbols you want. Anymore then 25 per request and the server my kick you. In that case for more than 25, add a delay.
mystocks= ['AMD',
           'GME'
           ]
stockdata=[]

def getData(symbol):
    headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{symbol}'
    r = requests.get(url, headers=headers)
    
    #print(r.status_code)
    
    soup = BeautifulSoup(r.text, 'html.parser')
    stocks ={
    #print(soup.title.text)
    'symbol': symbol,
    'price': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[0].text,
    'change': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[1].text.split(),
    }
    return stocks

    #print(price)
    
    #print(change)
    
    #print(price,change)
    
#print(getData('AAPL'))

for item in mystocks:
        stockdata.append(getData(item))
        print('Getting: ', item)

#print(stockdata)


with open('stockdata.json', 'w') as f:
        json.dump(stockdata, f, indent=2)

print('Fin.')
