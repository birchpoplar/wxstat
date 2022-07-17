import pandas as pd
import requests
import time
import csv
import re
import datetime
from datetime import date
from bs4 import BeautifulSoup
import iofuns

actuals = []

url = 'http://sparta/weewx/'

page = requests.get(url).content
soup = BeautifulSoup(page, "html.parser")

act_figs = soup.find("td", class_="data new_row hilo_day")
found = re.findall('[0-9][0-9]\.[0-9]', act_figs.text)
actuals.append(date.today())
actuals.append(found[0])
actuals.append(found[1])

iofuns.writeactuals(actuals)
