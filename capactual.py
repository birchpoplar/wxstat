import requests
import re
from datetime import date
from datetime import datetime
from bs4 import BeautifulSoup
import iofuns
import datatypes as dt

url = 'http://sparta/weewx/'

page = requests.get(url).content
soup = BeautifulSoup(page, "html.parser")
act_figs = soup.find("td", class_="data new_row hilo_day")
found = re.findall('[0-9][0-9]\.[0-9]', act_figs.text)

actual = dt.Actual(datetime.now(), date.today(), found[0], found[1])

iofuns.writeactuals(actual)
