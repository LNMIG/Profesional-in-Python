from datetime import datetime
from unidecode import unidecode
import pytz

def timezone(city):
    city = unidecode(city)
    city = city[0:1].upper() + city[1::].lower()
    americas_city = "America/"+ city
    aux_timezone = pytz.timezone(americas_city)
    city_time = datetime.now(aux_timezone)
    return f'{city}: {city_time.strftime("%d-%m-%Y, %H/%M/%S")}'


def run():
    city = input("Ingrese el nombre de una ciudad LATAM: ")
    print(timezone(city))

if __name__ == '__main__':
    run()

