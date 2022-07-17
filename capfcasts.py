import requests
import csv
import re
import datetime
from datetime import date
from bs4 import BeautifulSoup
import iofuns

url = 'https://forecast.weather.gov/MapClick.php?CityName=Saratoga+Springs&state=NY&site=ALY&textField1=43.0676&textField2=-73.7788&e=0'
# url = 'https://en.wikipedia.org/wiki/History_of_Python'

page = requests.get(url).content
soup = BeautifulSoup(page, "html.parser")

flows = []
fhighs = []
alow = []
ahigh = []
flows.append(date.today())
fhighs.append(date.today())

fcasts = soup.find_all("div", class_="tombstone-container")

firstFcast = True;

for fcast in fcasts:
    if isinstance(fcast.find("p", class_="temp temp-high"), type(None)):
        temp = fcast.find("p", class_="temp temp-low")
        if firstFcast == True:
            fcastdate = date.today() + datetime.timedelta(days=1)
        nextIsSameDay = True
        flows.append((fcastdate, (re.search('[0-9][0-9]', temp.text).group())))
    else:
        temp = fcast.find("p", class_="temp temp-high")
        if firstFcast == True:
            fcastdate = date.today()
        nextIsSameDay = False            
        fhighs.append((fcastdate, (re.search('[0-9][0-9]', temp.text).group())))
    if nextIsSameDay == False:
        fcastdate += datetime.timedelta(days=1)
    firstFcast = False

iofuns.printfcasts('Low', flows)
iofuns.printfcasts('High', fhighs)
iofuns.writefcasts('Low', flows)
