import requests
import csv
from io import StringIO


class Site(object):
    def __init__(self, name, country, aqi) -> None:
        super().__init__()
        self.site_name = name
        self.country = country
        try:
            self.aqi = int(aqi)
        except:
            self.aqi = 999

    def __repr__(self) -> str:
        return f"終點:{self.site_name}, 城市:{self.country}, aqi:{self.aqi}"


class Taiwan_AQI():
    API_KEY = '8b0006a7-5c61-4fc0-a6c1-363156de33de'

    @classmethod
    def download_aqi(cls) -> list:

        response = requests.get(
            f'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key={cls.API_KEY}&limit=1000&sort=ImportDate%20desc&format=CSV')

        if response.ok:
            # print(response.text)
            # file = open ('./lesson17/aqi.csv', mode='w',encoding='utf-8')
            # file.write(response.text)
            # file.close()
            file = StringIO(response.text, newline='')
            csvReader = csv.reader(file)
            next(csvReader)
            dataList = []
            for item in csvReader:
                site = Site(item[0], item[1], item[2])
                dataList.append(site)
            return dataList

        else:
            raise Exception("下載失敗")
