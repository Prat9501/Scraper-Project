from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CurrencyData
from .serializers import CurrencyDataSerializer


class CryptoListView(APIView):
    def get(self, request):
        queryset = CurrencyData.objects.all()
        read_serializer = CurrencyDataSerializer(queryset, many=True)
        print(read_serializer)
        return Response(read_serializer.data)


# url = "https://coinmarketcap.com/"


# def get_scraper_data(request):
#     page_data = requests.get(url)
#     soup = BeautifulSoup(page_data.content,'html.parser')
#     context = {
#         "data": []
#     }
#     table = soup.find('table')
#     CurrencyData.objects.all().delete()
#     # data = table.find_all('tr')
#     for row in table.find_all('tr'):
#         _td = row.find_all('td')
#         try:
#             image = row.find('img', class_='coin-logo').get('src')
#             name = row.find('p', class_='lhJnKD').text
#             symbol = row.find('p', class_='coin-item-symbol').text
#             price = row.find('div', class_='cLgOOr').text
#             time_1h = _td[4].text
#             time_24h = _td[5].text
#             time_7d = _td[6].text
#             market_cap = _td[7].find('span', class_='ieFnWP').text
#             volume_by_price = _td[8].find('p', class_='fVSMmK').text
#             volume_by_units = _td[8].find('p', class_='hueJdC').text
#             supply = _td[9].text
#         except AttributeError:
#             continue
        
#         p = CurrencyData(
#             image_link= image, name=name, symbol=symbol,
#             price=price, time_1h=time_1h, time_24h=time_24h,
#             time_7d=time_7d, market_cap= market_cap, 
#             volume_by_price=volume_by_price, 
#             volume_by_units=volume_by_units, supply=supply
#         )
#         p.save()
#         context['data'].append({
#             'image': image, 
#             'name': name, 
#             'symbol': symbol, 
#             'price': price, 'time_1h': time_1h, 'time_24h': time_24h, 
#             'time_7d': time_7d, 'market_cap': market_cap, 'volume_by_price': volume_by_price, 
#             'volume_by_units': volume_by_units, 'supply': supply
#         })
#     # import pdb; pdb.set_trace()
#     print(context)
#     return JsonResponse(context)

    