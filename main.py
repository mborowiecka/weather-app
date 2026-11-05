
from services.openweather import get_weather
from services.files import save_to_excel, read_excel
import time

read_excel()

while True:
    weather = get_weather()
    save_to_excel([weather])
    time.sleep(15)




