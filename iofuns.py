import csv
import socket
from datetime import datetime
import datatypes


def printfcasts(fcasts):
    for fcast in fcasts:
        if fcast.bound == "High":
            print(fcast.fcast_date, ' : High : ', fcast.temp)
    for fcast in fcasts:
        if fcast.bound == "Low":
            print(fcast.fcast_date, ' : Low : ', fcast.temp)


def writefcasts(fcasts):

    # need to determine if running on server (assume cronjob)
    if socket.gethostname() == "sparta":
        f = open('/home/johnnie/wxstat/fcasts.csv', 'a')
    else:    
        f = open('/home/johnnie/Projects/wxstat/fcasts.csv', 'a')

    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
    for fcast in fcasts:
        row = []
        row.append(fcast.timestamp)
        row.append(fcast.fcast_date.strftime('%Y-%m-%d'))
        row.append(fcast.origin_date.strftime('%Y-%m-%d'))
        row.append(fcast.bound)
        row.append(fcast.temp)
        writer.writerow(row)
    print(datetime.now(), ': Write complete - fcasts')
    f.close()


def writeactuals(actual):
    row = []
    row.append(datetime.now())
    for item in actual.mk_data_str():
        row.append(item)

    # need to determine if running on server (assume cronjob)
    if socket.gethostname() == "sparta":
        f = open('/home/johnnie/wxstat/actuals.csv', 'a')
    else:    
        f = open('actuals.csv', 'a')

    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(row)
    print(datetime.now(), ': Write complete - actuals')
    f.close()
