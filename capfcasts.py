import requests
# import csv
import re
import datetime
from datetime import datetime as dtm
from datetime import date
from bs4 import BeautifulSoup
import iofuns
import datatypes as dt

url = 'https://forecast.weather.gov/MapClick.php?CityName=Saratoga+Springs&state=NY&site=ALY&textField1=43.0676&textField2=-73.7788&e=0'
page = requests.get(url).content
soup = BeautifulSoup(page, "html.parser")

fcasts = []
fcasts_raw = soup.find_all("div", class_="tombstone-container")
firstFcast = True

for fcast_raw in fcasts_raw:
    if isinstance(fcast_raw.find("p", class_="temp temp-high"), type(None)):
        temp = fcast_raw.find("p", class_="temp temp-low")
        if firstFcast is True:
            fcastdate = date.today() + datetime.timedelta(days=1)
        nextIsSameDay = True
        fcasts.append(dt.Fcast(dtm.now(), fcastdate, date.today(), "Low",
                               (re.search('[0-9][0-9]', temp.text).group())))
    else:
        temp = fcast_raw.find("p", class_="temp temp-high")
        if firstFcast is True:
            fcastdate = date.today()
        nextIsSameDay = False
        fcasts.append(dt.Fcast(dtm.now(), fcastdate, date.today(), "High",
                               (re.search('[0-9][0-9]', temp.text).group())))

    if nextIsSameDay is False:
        fcastdate += datetime.timedelta(days=1)
    firstFcast = False

iofuns.printfcasts(fcasts)
iofuns.writefcasts(fcasts)
