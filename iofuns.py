import csv
from datetime import datetime

def printfcasts(fcasttype, fcasts):
    for fcast in fcasts:
        if type(fcast) == tuple:
            print(fcasttype + " :: " + str(fcast[0]) + " :: " + fcast[1])


def writefcasts(fcasttype, fcasts):
    f = open('/home/johnnie/Projects/wxstat/fcasts.csv', 'a')
    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
    for fcast in fcasts:
        row = []
        if type(fcast) != tuple:
            origin_date = fcast
        else:
            row.append(fcast[0].strftime('%Y-%m-%d'))
            row.append(origin_date.strftime('%Y-%m-%d'))
            row.append(fcasttype)
            row.append(fcast[1])
            writer.writerow(row)
    print(datetime.now(), ': Write complete - fcasts')
    f.close()

def writeactuals(actuals):
    f = open('/home/johnnie/Projects/wxstat/actuals.csv', 'a')
    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(actuals)
    print(datetime.now(), ': Write complete - actuals')
    f.close()
