import yaml
from yaml.loader import SafeLoader

with open("config.yaml") as f:
    data = yaml.load(f, Loader=SafeLoader)

LocalURL = data['LocalURL']
NWSURL = data['NWSURL']
CSVFcasts = data['CSVFcasts']
CSVActuals = data['CSVActuals']
CSVDataOut = data['CSVDataOut']
PNGHistHigh = data['PNGHistHigh']
PNGHistLow = data['PNGHistLow']
