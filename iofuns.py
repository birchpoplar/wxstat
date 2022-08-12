import csv
import socket
from datetime import datetime

def printfcasts(fcasttype, fcasts):
    for fcast in fcasts:
        if type(fcast) == tuple:
            print(fcasttype + " :: " + str(fcast[0]) + " :: " + fcast[1])


def writefcasts(fcasttype, fcasts):
    # Comment/uncomment line depending on system
    # for sparta
    # f = open('/home/johnnie/wxstat/fcasts.csv', 'a')
    # for local
    
    f = open('fcasts.csv', 'a')
    print(socket.gethostname())
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
    f = open('/home/johnnie/wxstat/actuals.csv', 'a')
    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(actuals)
    print(datetime.now(), ': Write complete - actuals')
    f.close()
