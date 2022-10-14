from asyncore import read
from urllib import response
from celery import shared_task
import requests
from bs4 import BeautifulSoup

from .models import CurrencyData


url = "https://coinmarketcap.com/"

@shared_task(bind = True)
def update_details(self):
    page_data = requests.get(url)
    soup = BeautifulSoup(page_data.content,'html.parser')
    
    table = soup.find('table')
    data = table.find_all('tr')
    for row in table.find_all('tr'):
        _td = row.find_all('td')
        try:
            image = row.find('img', class_='coin-logo').get('src')
            name = row.find('p', class_='lhJnKD').text
            symbol = row.find('p', class_='coin-item-symbol').text
            price = row.find('div', class_='cLgOOr').text
            time_1h = _td[4].text
            time_24h = _td[5].text
            time_7d = _td[6].text
            market_cap = _td[7].find('span', class_='ieFnWP').text
            volume_by_price = _td[8].find('p', class_='fVSMmK').text
            volume_by_units = _td[8].find('p', class_='hueJdC').text
            supply = _td[9].text
        except AttributeError:
            continue
        
        query = CurrencyData.objects.filter(name=name)
        print(query)
        if query:
            CurrencyData.objects.filter(name=name).update(
                price=price, time_1h=time_1h,time_24h=time_24h, time_7d=time_7d,
                market_cap= market_cap, volume_by_price=volume_by_price, volume_by_units=volume_by_units,
                supply=supply)
        else:
            p = CurrencyData(
                image_link= image, name=name, symbol=symbol,
                price=price, time_1h=time_1h, time_24h=time_24h,
                time_7d=time_7d, market_cap= market_cap, 
                volume_by_price=volume_by_price, 
                volume_by_units=volume_by_units, supply=supply
            )
            p.save()
    return 'Done'